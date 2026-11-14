#!/usr/bin/env python3
"""把 GTM Brain 的远程 HTTP MCP 桥接成本地 stdio MCP。

给没有 headersHelper 的客户端用（Codex、Cursor、Claude Desktop …）：
它们只能给远程 MCP 填固定 token，而 gbrain 的 token 一小时就过期。
这个桥接每次请求都用 headers.py 的缓存 token（快过期自动续签），
客户端那边只需要配置「运行这个脚本」。

协议：stdin 每行一条 JSON-RPC → POST 到 /mcp → 响应（JSON 或 SSE）逐条写回 stdout。
服务端重启会让 MCP 会话失效（404），这里会自动重放 initialize 再重试，客户端无感。
长连接偶尔会被中途掐断（实测 IncompleteRead），也会自动重试 —— 凭证是只读的，重试没有副作用。
只用标准库，兼容 Python 3.7+（macOS 自带的 python3 是 3.9）。
"""
from __future__ import annotations

import http.client
import json
import socket
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import headers  # noqa: E402  同目录的 headers.py

ENV = headers.load_env()
MCP_URL = ENV["GTM_BRAIN_URL"].rstrip("/") + "/mcp"

# 连接层的瞬时故障：服务端断连、超时。读操作重试安全（只读凭证，不会写两遍）
TRANSIENT = (http.client.IncompleteRead, http.client.RemoteDisconnected,
             urllib.error.URLError, socket.timeout, ConnectionError)

session_id: str | None = None
init_request: dict | None = None  # 记住客户端的 initialize，会话失效时重放


def parse_sse(body: str) -> list[dict]:
    """按 SSE 规范解析：事件之间空行分隔，一个事件可以有多行 data:，要拼起来再 json.loads。"""
    messages, data = [], []
    for line in body.splitlines() + [""]:
        if line == "":
            if data:
                payload = "\n".join(data)
                if payload.strip():
                    messages.append(json.loads(payload))
                data = []
        elif line.startswith("data:"):
            value = line[5:]
            data.append(value[1:] if value.startswith(" ") else value)
    return messages


def parse_body(body: str, content_type: str) -> list[dict]:
    if not body.strip():
        return []
    if "text/event-stream" in content_type:
        return parse_sse(body)
    parsed = json.loads(body)
    return parsed if isinstance(parsed, list) else [parsed]


def post(msg: dict, force_refresh: bool = False) -> list[dict]:
    """发一条消息，返回服务端回的所有 JSON-RPC 消息（通知类返回空列表）。"""
    global session_id
    hd = {"Authorization": f"Bearer {headers.get_token(force_refresh)}",
          "Content-Type": "application/json",
          "Accept": "application/json, text/event-stream"}
    if session_id:
        hd["Mcp-Session-Id"] = session_id
    req = urllib.request.Request(MCP_URL, data=json.dumps(msg).encode("utf-8"), headers=hd)
    with urllib.request.urlopen(req, timeout=120, context=headers.SSL_CTX) as r:
        session_id = r.headers.get("Mcp-Session-Id") or session_id
        body = r.read().decode("utf-8", errors="replace")
        content_type = r.headers.get("Content-Type") or ""
    return parse_body(body, content_type)


def error_replies(e: urllib.error.HTTPError, msg: dict) -> list[dict] | None:
    """服务端用 4xx/5xx 回了一条 JSON-RPC 错误时，原样转给客户端（而不是吞成一句「桥接出错」）。"""
    try:
        body = e.read().decode("utf-8", errors="replace")
        replies = parse_body(body, e.headers.get("Content-Type") or "")
    except (ValueError, OSError):
        return None
    if replies and all(isinstance(r, dict) and "jsonrpc" in r for r in replies):
        return replies
    return None


def reinitialize() -> None:
    global session_id
    session_id = None
    if init_request:
        post(init_request)
        post({"jsonrpc": "2.0", "method": "notifications/initialized"})


def handle(msg: dict) -> list[dict]:
    global init_request
    if msg.get("method") == "initialize":
        init_request = msg
    for attempt in range(3):
        try:
            return post(msg)
        except urllib.error.HTTPError as e:
            if e.code == 401:                  # token 被提前作废：强制续签重试一次
                return post(msg, force_refresh=True)
            if e.code == 404 and session_id and msg.get("method") != "initialize":
                reinitialize()                 # 服务端重启，会话丢了
                return post(msg)
            passthrough = error_replies(e, msg)
            if passthrough is not None:
                return passthrough
            raise
        except TRANSIENT:
            # HTTPError 是 URLError 的子类，所以这个分支只会接到真正的连接层故障
            if attempt == 2:
                raise
            time.sleep(1 + attempt)
    raise RuntimeError("unreachable")


def main() -> None:
    # 客户端（尤其是 GUI 启动的、或 Windows 上的）可能没给 UTF-8 的 stdio；
    # 中文内容在非 UTF-8 的 stdout 上会直接 UnicodeEncodeError。统一按 UTF-8 收发。
    stdin = open(sys.stdin.fileno(), "r", encoding="utf-8", errors="replace", closefd=False)
    stdout = open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False)
    for line in iter(stdin.readline, ""):
        if not line.strip():
            continue
        try:
            msg = json.loads(line)
        except ValueError:
            continue  # 不是 JSON 的行没法回应（没有 id），跳过而不是整个桥接崩掉
        try:
            replies = handle(msg)
        except Exception as e:  # 出错也要给客户端一个回应，不能让它干等
            if "id" not in msg:
                continue
            replies = [{"jsonrpc": "2.0", "id": msg["id"],
                        "error": {"code": -32000, "message": f"gtm-brain 桥接出错: {e}"[:500]}}]
        for reply in replies:
            stdout.write(json.dumps(reply, ensure_ascii=False) + "\n")
            stdout.flush()


if __name__ == "__main__":
    main()
