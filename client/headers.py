#!/usr/bin/env python3
"""GTM Brain 的 Claude Code headersHelper。

Claude Code 每次连接 MCP 时运行它，把 stdout 当请求头：
    {"Authorization": "Bearer <access token>"}

用 client_credentials 换 token，缓存在同目录的 token.json，过期前 5 分钟续签。
这样凭证配一次就永远不用管 —— 不像写死的 Bearer token 一小时就过期。

只用标准库：同事机器上有 python3 就能跑，不用装任何东西。
兼容 Python 3.7+（macOS 自带的 /usr/bin/python3 是 3.9，不能用 3.10 的 `X | None` 语法）。
Claude Code 给 helper 的时限是 10 秒，所以每个网络请求 4 秒超时。
"""
from __future__ import annotations

import json
import os
import ssl
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
CACHE = HERE / "token.json"


def load_env() -> dict[str, str]:
    env = {}
    for line in (HERE / ".env").read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k = k.strip()
        if k.startswith("export "):
            k = k[len("export "):].strip()
        env[k] = v.strip().strip('"').strip("'")
    return env


def ssl_context() -> ssl.SSLContext:
    """python.org 安装包版的 Python 默认没有 CA 证书，HTTPS 会报 CERTIFICATE_VERIFY_FAILED。

    系统证书库为空时，依次退到 certifi（装了的话）和 macOS 自带的 /etc/ssl/cert.pem。
    """
    ctx = ssl.create_default_context()
    if ctx.cert_store_stats().get("x509_ca", 0) == 0:
        try:
            import certifi  # type: ignore
            ctx.load_verify_locations(certifi.where())
        except ImportError:
            if os.path.exists("/etc/ssl/cert.pem"):
                ctx.load_verify_locations("/etc/ssl/cert.pem")
    return ctx


SSL_CTX = ssl_context()


def fetch_token(env: dict[str, str]) -> tuple[str, float]:
    base = env["GTM_BRAIN_URL"].rstrip("/")
    # 从发现文档拿 token 端点，不写死路径（gbrain 用 /token，不是常见的 /oauth/token）
    with urllib.request.urlopen(
            f"{base}/.well-known/oauth-authorization-server", timeout=4, context=SSL_CTX) as r:
        endpoint = json.load(r)["token_endpoint"]
    body = urllib.parse.urlencode({
        "grant_type": "client_credentials",
        "client_id": env["GTM_BRAIN_CLIENT_ID"],
        "client_secret": env["GTM_BRAIN_CLIENT_SECRET"],
        "scope": "read",
    }).encode()
    req = urllib.request.Request(
        endpoint, data=body, headers={"Content-Type": "application/x-www-form-urlencoded"})
    with urllib.request.urlopen(req, timeout=4, context=SSL_CTX) as r:
        d = json.load(r)
    return d["access_token"], time.time() + int(d.get("expires_in", 3600))


def write_cache(token: str, expires_at: float) -> None:
    # 先写临时文件（创建时就是 0600）再原子替换：token 不会有一瞬间是别人可读的，
    # 并发的另一个进程也不会读到写了一半的文件
    tmp = CACHE.with_name(f"{CACHE.name}.{os.getpid()}.tmp")
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f:
        json.dump({"access_token": token, "expires_at": expires_at}, f)
    os.replace(tmp, CACHE)


def get_token(force_refresh: bool = False) -> str:
    """返回有效的 access token：优先用缓存，快过期或 force_refresh 时重新换。"""
    if not force_refresh:
        try:
            cached = json.loads(CACHE.read_text())
            if cached["expires_at"] - 300 > time.time():
                return cached["access_token"]
        except (OSError, ValueError, KeyError):
            pass
    token, expires_at = fetch_token(load_env())
    write_cache(token, expires_at)
    return token


def main() -> None:
    print(json.dumps({"Authorization": f"Bearer {get_token()}"}))


if __name__ == "__main__":
    main()
