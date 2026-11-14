"""Generate docs/images/architecture.{en,zh}.svg (run: python3 docs/images/gen_architecture.py docs/images) from one layout so the two never drift."""
import sys
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(sys.argv[1])

T = {
    "en": dict(
        title="SV GTM Advisor — Architecture",
        loop="Learn → Digest → Evolve (weekly · text + images)",
        learn=("Learn", "collect"), digest=("Digest", "slim · chunk · embed"),
        evolve=("Evolve", "incremental, keeps growing"),
        src=("Primary sources", "newsletters · playbooks · cases"),
        bot=("Grok Bot", "new posts + images"),
        vault=("Obsidian vault", "single source of truth"),
        weekly=("Weekly sync", "slim · upload · ingest"),
        db=("Supabase storage", "text embeddings + images"),
        gb=("GBrain retrieval", "semantic search · read-only keys"),
        mcp="MCP → Any agent to access",
        clients="Claude Code · Codex · Cursor …",
        tanka="Tanka (planned)",
        ask="Ask anytime · cited answers · full article on request",
        contrib=("Contribution loop", "open a PR · suggest new sources"),
        note="Note: Tanka is planned; image-to-image search is not built yet; "
             "images are returned as links.",
    ),
    "zh": dict(
        title="SV GTM Advisor 架构",
        loop="自我学习 → 消化 → 进化（每周更新 · 文字 + 图像）",
        learn=("自我学习", "收录"), digest=("消化", "瘦身 · 切块 · 向量化"),
        evolve=("进化", "增量入库，越来越厚"),
        src=("一手来源", "Newsletter · 手册 · 案例"),
        bot=("Grok Bot", "收录新文章 + 原图"),
        vault=("Obsidian 知识库", "唯一真源"),
        weekly=("每周更新", "瘦身 · 上传 · 入库"),
        db=("Supabase 线上存储", "正文向量 + 配图"),
        gb=("GBrain 检索", "语义检索 · 只读凭证"),
        mcp="MCP → Any agent to access",
        clients="Claude Code · Codex · Cursor …",
        tanka="Tanka（规划中）",
        ask="任何人随时问，答案带出处，可调取全文",
        contrib=("贡献回路", "提 PR · 推荐新来源"),
        note="注：Tanka 接入规划中；以图搜图暂未做，配图以原图链接随答案返回",
    ),
}

BLUE, PINK, INK, MUTED = "#2b3a8f", "#d6336c", "#1f2a5a", "#5b6275"
FONT = ("-apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', "
        "'Hiragino Sans GB', 'Noto Sans SC', 'Microsoft YaHei', sans-serif")


def text(x, y, s, size, fill=INK, weight=400, anchor="middle"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" '
            f'text-anchor="{anchor}">{escape(s)}</text>')


def fit(s, width, size):
    """Shrink font size so the string fits: CJK ≈ 1em wide, Latin ≈ 0.55em."""
    ems = sum(1.0 if ord(c) > 0x2E80 else 0.5 for c in s)
    return min(size, int(width / ems))


def box(x, y, w, h, icon, head, sub, color=BLUE):
    cx = x + w / 2
    return "\n".join([
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#ffffff" fill-opacity="0.85" '
        f'stroke="{color}" stroke-width="3.5"/>',
        text(x + 34, y + 52, icon, 34, anchor="middle"),
        text(cx, y + h / 2 - 2, head, fit(head, w - 40, 38), color, 600),
        text(cx, y + h / 2 + 52, sub, fit(sub, w - 40, 26), MUTED),
    ])


def arrow(x1, y1, x2, y2, color=BLUE, dashed=False):
    d = ' stroke-dasharray="14 10"' if dashed else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="3.5"'
            f'{d} marker-end="url(#ah-{"p" if color == PINK else "b"})"/>')


def render(t):
    W, H = 2000, 1125
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         f'font-family="{FONT}" role="img" aria-label="{escape(t["title"])}">',
         f'<title>{escape(t["title"])}</title>',
         '<defs>',
         '<pattern id="grid" width="25" height="25" patternUnits="userSpaceOnUse">'
         '<path d="M25 0H0V25" fill="none" stroke="#dfe3ec" stroke-width="1"/></pattern>',
         '<pattern id="hatch" width="16" height="16" patternUnits="userSpaceOnUse" '
         'patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="16" stroke="#f3c4d4" '
         'stroke-width="2"/></pattern>',
         f'<marker id="ah-b" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="9" markerHeight="9" '
         f'orient="auto-start-reverse"><path d="M1 1L10 6L1 11" fill="none" stroke="{BLUE}" stroke-width="2"/></marker>',
         f'<marker id="ah-p" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="9" markerHeight="9" '
         f'orient="auto-start-reverse"><path d="M1 1L10 6L1 11" fill="none" stroke="{PINK}" stroke-width="2"/></marker>',
         '</defs>',
         f'<rect width="{W}" height="{H}" fill="#fbfbf7"/>',
         f'<rect width="{W}" height="{H}" fill="url(#grid)"/>',
         f'<line x1="28" y1="0" x2="28" y2="{H}" stroke="#f2a9bd" stroke-width="2"/>',
         text(50, 78, t["title"], 50, BLUE, 600, "start"),
         f'<line x1="50" y1="97" x2="{50 + int(sum(1.0 if ord(c) > 0x2E80 else 0.5 for c in t["title"]) * 50)}" y2="97" stroke="{PINK}" stroke-width="4" stroke-linecap="round"/>',
         # learn / digest / evolve band
         f'<rect x="450" y="125" width="1500" height="150" rx="4" fill="none" stroke="{PINK}" '
         f'stroke-width="3" stroke-dasharray="16 10"/>',
         text(478, 168, t["loop"], 32, PINK, 500, "start")]
    for (head, sub), x in ((t["learn"], 478), (t["digest"], 900), (t["evolve"], 1510)):
        p.append(f'<text x="{x}" y="232" font-size="30" fill="{BLUE}" font-weight="600">{escape(head)}'
                 f'<tspan font-size="25" fill="{MUTED}" font-weight="400" dx="18">{escape(sub)}</tspan></text>')
    # top row
    p += [box(50, 312, 340, 212, "📰", *t["src"]),
          box(462, 312, 314, 212, "🤖", *t["bot"]),
          box(850, 312, 338, 212, "📓", *t["vault"]),
          box(1525, 312, 425, 212, "🗄️", *t["db"]),
          box(1525, 712, 425, 200, "🔍", *t["gb"]),
          arrow(390, 415, 458, 415), arrow(776, 415, 846, 415),
          arrow(1188, 415, 1521, 415),
          text(1356, 380, t["weekly"][0], 34, PINK, 600),
          text(1356, 470, t["weekly"][1], 26, MUTED),
          arrow(1738, 524, 1738, 708),
          arrow(1525, 808, 1180, 808)]
    # MCP box
    p += [f'<rect x="50" y="676" width="1126" height="312" rx="4" fill="#fdeef3"/>',
          f'<rect x="50" y="676" width="1126" height="312" rx="4" fill="url(#hatch)" fill-opacity="0.45"/>',
          f'<rect x="50" y="676" width="1126" height="312" rx="4" fill="none" stroke="{PINK}" stroke-width="3.5"/>',
          text(92, 728, "🔌", 34),
          text(613, 765, t["mcp"], 54, PINK, 600),
          text(613, 836, t["clients"], 34, BLUE),
          text(613, 892, t["tanka"], 32, BLUE),
          text(613, 952, t["ask"], 30, INK),
          # contribution loop
          arrow(106, 672, 106, 530, PINK, dashed=True),
          text(132, 588, t["contrib"][0], 32, PINK, 500, "start"),
          text(132, 628, t["contrib"][1], 26, PINK, 400, "start"),
          text(50, 1076, t["note"], 23, MUTED, 400, "start"),
          '</svg>']
    return "\n".join(p) + "\n"


for lang, t in T.items():
    (OUT / f"architecture.{lang}.svg").write_text(render(t), encoding="utf-8")
    print("wrote", OUT / f"architecture.{lang}.svg")
