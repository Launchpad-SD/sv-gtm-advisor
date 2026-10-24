# SV GTM Advisor

把硅谷最近几年的增长一手复盘，变成一个随叫随到的增长顾问，接进你的 **Claude Code 或 Codex**。
问一句 GTM 问题，它先去上千篇真实案例里找最接近你处境的那几篇，再基于原文回答，并告诉你出自哪篇。

> **你不需要 clone 这个仓库，也不需要懂代码。** 装好只要两分钟，从头到尾照下面做就行。
> 服务在大家电脑上注册的名字仍是 `gtm-brain`（改名不影响已经装好的人）。

---

## 为什么不直接问 Claude / Codex？

旗舰模型什么都懂一点，但它给你的是**通用套路**：做社区、写内容、发 Product Hunt。
每条都对，每条都不知道**你这个处境下哪条会翻车**。

做 GTM 的人——创始人、产品、市场——不一定有十年经验，也不可能天天盯着外面的 case study。
你真正缺的是**一个顾问**：他恰好知道过去两年所有值得知道的增长故事，能有依据地告诉你
什么有效、什么已经被验证是坑、哪家公司的处境跟你最像。他指方向、给证据，**但不替你执行**。

这个库就是那个顾问。而且它不是一个人：

- **上千篇一手复盘**，来自多个持续更新的来源，篇数每周增加，来源也在持续扩充。
  **每一篇背后通常是一家公司的操盘手在讲他刚做过的事**——Figma 怎么找到前十个用户、
  Cockroach Labs 怎么从开源走到云、上百家 B2B 公司的首页定位改版前后对比。
- 相当于**上千次和增长操盘手的对话**，被压缩成一次提问。你问一句，它替你把这上千篇筛一遍，
  只把最接近你处境的几篇摆到你面前。
- **每周六自动更新**。三个月前刚被验证过的做法，往往比一整本经典教科书更有用——
  尤其在 AI 产品的定价、免费额度、分发这些每个季度都在变的地方。

**它不做什么**：不替你写文案、不替你跑广告、不替你发邮件。它只负责让你在动手之前，
先站在「别人已经踩过这个坑」的位置上。

下面第五节有一个真实对比：同一个模型、同一个问题，接不接这个库，回答差在哪里。

---

---

## 一、库里有什么

目前收录的来源如下，全是一手的 GTM 实操内容。**每周六同步更新**；新来源会陆续加进来。

> **最近一次同步**：2026-10-24 15:09 PT · 库内合计 **1,689** 篇笔记（配图已同步）。

| 来源 | 篇数 | 时间跨度 | 适合找什么 |
|---|---|---|---|
| **Lenny's Newsletter** | 502 | 2019 – 至今 | 产品、增长、PLG、定价、团队与职业；大量访谈和数据 |
| **Growth Unhinged** | 241 | 2021 – 至今 | B2B SaaS 增长实操：免费试用、定价、PLG 转化、指标 |
| **Marketing Ideas** | 202 | 2023 – 至今 | 每周具体的营销打法和案例，拿来就能用的点子 |
| **Fletch PMM** | 137 | — | **网站定位改版前后对比**：改之前哪里不好、改之后好在哪，附整页截图 |
| **MRR Unlocked** | 128 | 2021 – 至今 | 创始人视角的早期 GTM：冷邮件、LinkedIn、销售演示、定位工作表 |
| **Behind the Craft** | 118 | 2016 – 至今 | Peter Yang 的产品与 AI 实战：AI 产品怎么做、怎么用 AI 工具、产品经理成长 |
| **Elena's Growth Scoop** | 59 | 2023 – 至今 | Elena Verna 的增长方法：PLG、免费增值、定价、AI 时代的增长团队 |
| **MKT1** | 42 | 2020 – 至今 | Emily Kramer 的 B2B 营销实操：Claude / MCP 工作流、团队与策略 |
| **Growth Memo** | 31 | 2018 – 至今 | Kevin Indig 的 SEO 与 AI 搜索：排名因素、内容策略、AI 搜索流量变化 |
| **GTM Strategist** | 6 | 2026 – 至今 | Maja Voje 的 B2B GTM：病毒发布、LinkedIn、广告与推荐 |
| **Playbooks** | 216 | — | 成体系的手册（含 PR：newsjack、Chuwu-PR-OS）：定价、发布、GEO、公关与危机 |
| **案例拆解与行业观察** | 4 | 2026 – 至今 | 单家公司的 GTM 拆解（如 Meshy、Corgi、X 上的爆款发布） |
| **Product** | 3 | 2026 – 至今 | AI / Agent 方向的产品观察与创业缝隙 |

文章里的配图（图表、截图、框架图）都保留着，是可以直接打开的链接。

**库里没有的**：实时新闻、某家公司的内部数据、GTM 以外的话题。
问到这些，它会告诉你库里没有，再用自己的知识或网络补充。

---

## 二、找 Bei 要安装文件

这个仓库的代码是公开的，但**知识库服务只对开通了的同事开放**。**私信 Bei（Bei Zhang，GitHub [@beizhangnina](https://github.com/beizhangnina)）说一声**，
告诉他你想用，以及你的英文名（比如 `alice`）。

他会发你一个文件：**`你的名字-install.sh`**。

- 这是**只给你一个人用的**：里面有你的个人凭证。**别转发，也别放进群聊、邮件、网盘或 git。**
- 凭证是**只读**的：只能搜和读，改不了库里的东西。
- 通常是 AirDrop 或私聊发给你。**装好之后把那条消息删掉。**

---

## 三、安装（一次，约两分钟）

**需要**：装了 Claude Code 或 Codex（ChatGPT 桌面 App 里那个）其中之一。Mac 自带的 `python3` 就够，不用装别的。

1. 打开 Mac 的 **「终端」（Terminal）** App
2. 进入安装文件所在的文件夹，比如下载目录：
   ```bash
   cd ~/Downloads
   ```
3. 运行（把 `alice` 换成你的名字）：
   ```bash
   bash alice-install.sh
   ```
4. 看到这句就装好了：
   ```
   ✓ 完成，已装进 Claude Code 和 Codex。
   ```
   （只装了其中一个的话，就只显示那一个）

> 必须在「终端」里运行，不要在 Claude Code 的对话框里跑。

**它做了什么**（都只动你自己电脑，而且只动 gtm-brain 相关的那一段，不碰你其他的配置）：

- 把凭证存到 `~/.config/gtm-brain/`，只有你自己能读
- 装了 Claude Code 就配进 Claude Code，装了 Codex 就配进 Codex，两个都有就两个都配
- 在 `~/.claude/CLAUDE.md` / `~/.codex/AGENTS.md` 里加一条规则：**问 GTM 问题时自动先查这个库**
- 凭证会自动续期，**装一次就永远不用管**

---

## 四、怎么用

**先重启一次**：新开一个 Claude Code 会话；用 Codex 的话，**彻底退出并重新打开 ChatGPT App**。

然后**直接用中文或英文问就行**。几个例子，以及你大概会看到什么：

| 你问 | 它会去找的（实测结果） |
|---|---|
| B2B SaaS 首页定位有哪些好的改版案例？给我三个，说说改前改后的区别 | Fletch PMM 的 Survicate、lemlist、Blue Triangle 等改版前后对比 |
| 免费试用怎么优化转化？ | Growth Unhinged 的免费试用优化、reverse trial 指南，MRR Unlocked 的免费试用 8 条要点 |
| 定价策略怎么做？ | Growth Unhinged 的定价项目方法、Playbooks 的定价策略手册、Lenny's 的 B2B 增长引擎 |
| 产品发布前要准备什么？ | Playbooks 的发布策略和 Product Hunt 发布指南 |

> **要不要说「gtm-brain」？** 不说也行：安装时已经加了规则，问 GTM 相关的问题它会自动先查库。
> 但它有时会判断「这题不用查」而直接凭自己的知识回答。**想确保它一定先查库，就在问题里加一句「用 gtm-brain」**，
> 比如「用 gtm-brain 查一下，免费试用怎么优化转化？」

**你会得到**：基于原文的回答，带出处（系列 + 文章标题），需要时附上原文里的图片链接。
**中文提问也能搜到英文文章**。每次查库大约 4–6 秒。

**问得越具体，答得越好**。几个好用的问法：

- 「PLG 公司怎么加上销售团队？ClickUp、Calendly 这些是怎么做的」
- 「AI 搜索 / GEO 应该怎么做？有哪些具体步骤」
- 「Fletch PMM 里 fintech 公司的改版案例，总结它们共同的问题」
- 「activation 指标怎么定？列出相关文章，每篇一句话总结」

想确认它连上了：在 Claude Code 里输入 `/mcp`，列表里有 **gtm-brain ✔ connected** 就对了。

---

## 五、举个例子：同一个问题，接不接库的差别

**问题**：EverOS（AI agent 的记忆层，Apache 2.0 开源 + 托管云服务，免费版 5 万 MCU，Pro $25/月，官网还没有公开客户案例）**该怎么做冷启动？**

同一个模型（Claude Opus 5），同一个问题，唯一的区别是有没有接 gtm-brain。右栏是 2026-09-22 的真实检索结果。

| | 不接库 | 接了库 |
|---|---|---|
| **开源怎么转成付费云** | 「先把开源社区做起来，再引导到云服务」 | Cockroach Labs 是一开始就开源，之后才加自托管专有版和专用云。创始人提醒：**企业段的安全合规和销售周期比预期长好几个月**，社区和企业销售要两条线并行，别指望社区自然转化 · [出处](https://www.growthunhinged.com/p/scaling-to-5b-with-cockroach-labs) |
| **免费额度怎么定** | 「免费额度给足，观察用户怎么用，再决定付费点」 | 传统 SaaS 多一个免费用户成本近似为零，**AI 每次免费调用都在烧 GPU**，免费额度给不对会烧穿现金。5 万 MCU 要按「单个免费用户的真实计算成本 × 转化率」倒推，不能照抄 SaaS · [出处](https://www.lennysnewsletter.com/p/why-saas-freemium-playbooks-dont) |
| **前 10 个客户从哪来** | 「写技术博客发 Hacker News、接 LangChain 生态借分发」 | 二十多家高速增长的 B2B 公司靠的是三条杠杆：**个人网络、去客户扎堆的地方找、拿到媒体报道**。Figma 的 Dylan Field 先在 Twitter 上筛出最有影响力的设计师，再逐个冷邮件或要引荐 · [出处](https://www.lennysnewsletter.com/p/how-todays-fastest-growing-b2b-businesses) · [更细的打法](https://www.lennysnewsletter.com/p/how-to-win-your-first-10-b2b-customers) |
| **免费送哪些功能** | 「先免费引流，再想变现」 | 送哪些功能是有方法的，不是「先免费再说」 · [出处](https://www.growthunhinged.com/p/why-you-should-give-away-your-features) |
| **冷启动要花多少钱** | 没提 | 2026 年基准：约 $1K 换来几百个注册（小额 YouTube 广告 + 二十来个细分 subreddit + 私信流程）；约 $5K 可冲到 24 小时 1,800 票，但有案例当天第一被事后复核撤销——花钱前先看清平台规则 |
| **一句话总结** | 每条都对，但都是通用套路：没有真实公司、没有数字、没有出处，也不会告诉你哪条在你的处境下会翻车 | 具体公司怎么做的、哪一步会踩坑、数字是多少，每条都能点开原文核对 |

最关键的是第二行：「AI 的免费额度会烧 GPU」来自 2026 年 5 月的一篇文章，**是模型自身知识里不一定有、也不一定会主动提起的**。而这恰恰是 EverOS 定免费额度时最该先知道的事。

<details>
<summary>展开看两边的完整回答</summary>

**不接库的回答（同一个模型，没查库）**

> 建议分四步走：
> 1. **先把开源做起来**：把 README 和 quickstart 打磨好，让人五分钟能跑通；在 GitHub 上积累 star 和 issue 互动。
> 2. **内容营销**：写技术博客讲你的记忆架构和 benchmark，发到 Hacker News、Reddit r/LocalLLaMA、X 的 AI 开发者圈。
> 3. **生态集成**：接进 LangChain、LlamaIndex 这类框架的生态，借它们的分发。
> 4. **早期用户**：找几十个种子用户深聊，把免费额度给足，观察他们怎么用，再决定付费点。
>
> 定价上，免费版引流、Pro 订阅变现的思路是对的，可以再考虑按用量计费。

**接了库的回答**

> **1. 开源转云，先看 Cockroach Labs 怎么走的。** 他们一开始就开源（创始人 Spencer Kimball 说他自己都不会用闭源数据库），之后才加上自托管专有版和专用云。他的提醒：企业段的安全合规比你预期的久得多，销售周期会长好几个月——所以开源社区和企业销售要当两条线并行，不能指望社区自然转化。
> 出处：Growth Unhinged《Lessons learned scaling to $5B with Cockroach Labs' CEO》
>
> **2. 你的免费版和传统 SaaS 的免费版不是一回事。** 传统 SaaS 多一个免费用户，成本几乎为零；AI 产品每一次免费调用都在烧 GPU，免费额度给不对会直接烧穿现金。所以 5 万 MCU 这个额度要按「单个免费用户的真实计算成本 × 转化率」倒推，而不是照抄 SaaS 的免费额度。
> 出处：Lenny's Newsletter《Why SaaS freemium playbooks don't work in AI, and what to do instead》
>
> **3. 前 10 个客户靠的是三条杠杆，不是内容营销。** 二十多家高速增长的 B2B 公司（Figma、Stripe、Slack、Airtable 等）的共同做法：用个人网络、去客户扎堆的地方找、拿到媒体报道。Figma 的 Dylan Field 是在 Twitter 上先找出最有影响力的设计师，筛一遍名单，再逐个冷邮件或要引荐。
> 出处：Lenny's Newsletter《How today's fastest growing B2B businesses found their first ten customers》
>
> **4. 免费送哪些功能是有方法的**，不是「先免费再说」。
> 出处：Growth Unhinged《Why you should give away your features》
>
> **5. 冷启动预算的真实回报**（库里 playbook 的 2026 年基准）：约 $1K 能换来几百个注册；约 $5K 可以冲到 24 小时 1,800 票，但有案例当天第一被事后复核撤销。

</details>

> 两边都是真实输出：左栏是同一个模型不查库时的真实回答，右栏是真实检索结果。我们没有刻意把左栏写差。

---

## 六、遇到问题

| 现象 | 怎么办 |
|---|---|
| 安装时报「凭证换不到 token」 | 凭证可能已经失效。找 Bei 重新发一个安装文件 |
| 安装时报「没找到 Claude Code 也没找到 Codex」 | 先装其中一个，再重新运行安装文件 |
| Claude / Codex 回答时没有去查库 | 1）问题里加一句「用 gtm-brain」，确保优先查库；2）确认重启过（新会话 / 重开 App）；3）Claude Code 里输入 `/mcp` 看是否 connected |
| 其他报错 | 在终端运行 `python3 ~/.config/gtm-brain/headers.py`，把输出发给 Bei（不会显示你的密码） |
| 换了新电脑 | 在新电脑上再运行一次同一个安装文件就行 |
| Codex 里偶尔报连接错误 | 更新一下本地脚本（不动你的凭证）：<br>`curl -fsSL https://raw.githubusercontent.com/beizhangnina/sv-gtm-advisor/main/client/stdio_bridge.py -o ~/.config/gtm-brain/stdio_bridge.py`<br>然后重启 ChatGPT App |
| 不想用了 / 离职 | 告诉 Bei，他会注销你的凭证，立刻生效 |

---

## 七、使用规范

这是一个**内部使用的工具**，不对外提供、不做商业用途。库里有**付费订阅内容**（Lenny's 等），版权归原作者：

- **不要把正文、图片链接贴到公开的地方**（社交媒体、公开文档、对外材料）
- 引用观点可以，大段复制原文不行
- 安装文件和凭证只给你自己用

更详细的安装说明（原理、每一步做了什么）：[docs/INSTALL-FOR-TEAMMATES.md](docs/INSTALL-FOR-TEAMMATES.md)
