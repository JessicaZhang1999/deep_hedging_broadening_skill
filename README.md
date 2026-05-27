# Deep Hedging Broadening Literature Skill

专为 Jessica 设计，用于**拓宽**已完成的三篇 Deep Hedging 论文（FunNN + empirical Esscher + diffusion model）的研究领域。

**使用方法**：
1. 把整个文件夹放入您的 AI Agent 项目
2. 把 `research_profile.md` + `system_prompt.md` 喂给大模型
3. 把 `tool_schemas.json` 注册为 function calling tools
4. 让 AI 直接调用 `search_broadening_papers`（可指定 focus_area 进一步定向拓宽）

所有下载的文件自动保存在 `my_deep_hedging_broadening_papers/` 文件夹，并以论文标题命名。
