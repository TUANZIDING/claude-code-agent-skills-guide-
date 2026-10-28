# 来源与致谢 · Sources and Credits

[← 返回首页](../README.md) ｜ [仓库核对表](repo-catalog-v0.1.md)

## 原始线索 · Original pointers

| 来源 | 本仓库用了什么 | 没用什么 |
| --- | --- | --- |
| X 用户 [@thedelost](https://x.com/thedelost)，2026-10-24 的帖子 | 10 个仓库的清单；「第一支小队要有明确终点、只算保留的产出与成本、扩编要证明价值」的建议 | 原帖文字与配图（本仓库均为独立重写和自绘） |
| 该帖引用的 [@hanakoxbt](https://x.com/hanakoxbt) 长文 | 角色分工、提出者不评分、共享台账记录失败结果、固定判定类别、按时间切分的留出验证等通用方法 | 文中的产品推广、链接、交易与投资相关内容，已全部删除 |

## 被收录的仓库 · The ten repos

感谢以下仓库的作者与贡献者。所有代码、文档与图片归其各自作者所有，许可以各仓库为准（核对日期 2026-10-28）：

| # | 仓库 | 作者 / 组织 | 许可 |
| --- | --- | --- | --- |
| 01 | [wshobson/agents](https://github.com/wshobson/agents) | wshobson | MIT |
| 02 | [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | VoltAgent | MIT |
| 03 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | rohitg00 | Apache-2.0 |
| 04 | [anthropics/skills](https://github.com/anthropics/skills) | Anthropic | 混合：多数 Apache-2.0，4 个源码可见 |
| 05 | [netresearch/claude-code-marketplace](https://github.com/netresearch/claude-code-marketplace) | Netresearch | MIT |
| 06 | [disler/claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery) | disler | 未声明 |
| 07 | [karanb192/claude-code-hooks](https://github.com/karanb192/claude-code-hooks) | karanb192 | MIT |
| 08 | [affaan-m/claude-swarm](https://github.com/affaan-m/claude-swarm) | affaan-m | MIT |
| 09 | [am-will/swarms](https://github.com/am-will/swarms) | am-will | README 写 MIT，无 LICENSE 文件 |
| 10 | [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain) | eugeniughelbur | MIT |

## 官方文档 · Official docs

- [Create custom subagents](https://code.claude.com/docs/en/sub-agents)（2026-10-28 访问）
- [Extend Claude with skills](https://code.claude.com/docs/en/skills)
- [Hooks reference](https://code.claude.com/docs/en/hooks)

## 核对方法 · Verification

1. GitHub REST API `GET /repos/{owner}/{repo}`：描述、Stars、许可、最近推送、是否归档、是否 fork。
2. `git clone --depth 1` 后用文件数粗略核对作者自述的数量，并查看每个仓库的 LICENSE 文件。
3. 安装命令摘自各仓库 README，本仓库未在真实环境中逐一安装测试。

## 本仓库的许可 · This repo's license

本仓库原创的文档、SVG 图示与脚本采用 [MIT](../LICENSE) 许可，© 2026 Haixiang Ding (TUANZIDING)。MIT 只覆盖本仓库原创内容，不覆盖被收录仓库的任何内容。
