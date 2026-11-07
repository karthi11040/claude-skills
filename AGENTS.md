# AGENTS.md — Universal AI Agent Tool Skills Guide

Welcome to the **Claude & AI Agent Tool Skills** repository. This project is a production-grade collection of **Agent Tool Skills** designed to teach AI models (**Claude Code**, **OpenAI Codex**, **Google Gemini / Antigravity**, **Cursor**, **Moonshot Kimi**, **Z.ai GLM**, and universal coding agents) how to control external tools, construct vector design systems, and execute verified deep research.

---

## 1. Quick Installation for Models & Agents

### Claude Code (Plugin Marketplace)
```bash
/plugin marketplace add karthi11040/claude-skills
/plugin install engineering-skills@claude-code-skills
```

### Codex, Cursor, Gemini CLI, Copilot & Other Agents
```bash
npx skills add karthi11040/claude-skills
```

### Local Cross-Platform Deployment
```bash
python install.py
```

---

## 2. How AI Models Use These Tool Skills

Agent skills use **Progressive Disclosure** and **Active Tool Execution**:

1. **Triggering**: The model indexes only the YAML frontmatter (`name`, `description`). Full instructions in `SKILL.md` are loaded on-demand only when a user prompt matches the trigger.
2. **Execution**: The skill provides precise CLI commands, MCP tool signatures, and Python scripts that the model runs directly in the user's terminal/workspace.
3. **Verification**: Models verify all actions by checking exit codes, inspecting rendered preview images (`figcraft-cli render`), and computing algorithmic scores (`verify_dossier.py`) before delivering final output.

---

## 3. Tool Skills Inventory

1. **`figcraft`** (`skills/figcraft/SKILL.md`):
   - **Target Tool**: Local `figcraft-cli` binary & FigCraft MCP server (`figcraft-cli mcp`).
   - **Capabilities**: Inspecting vector layer hierarchies, executing procedural JSON modifications, rendering composite previews, and exporting artboards to PNG.

2. **`dating-app-design`** (`skills/dating-app-design/SKILL.md`):
   - **Target Tool / Domain**: High-conversion mobile UX architecture, dark obsidian tokens (`#0D0E16`, `#FF385C`, `#8B5CF6`), swipe gesture physics, card overlays, and interactive prototype linking.

3. **`deep-research-synthesizer`** (`skills/deep-research-synthesizer/SKILL.md`):
   - **Target Tool**: Algorithmic evidence verification scripts (`scripts/score_evidence.py`, `scripts/verify_dossier.py`).
   - **Capabilities**: Multi-source investigations, source credibility grading, dispute resolution, and structured decision dossier compilation.

---

## 4. Reference Case Study

To demonstrate model execution in practice, this repository includes [`love.figcraft`](./love.figcraft) — a complete 6-screen mobile dating application created entirely by an AI model using the `figcraft` tool skill and `dating-app-design` skill:
- Preview: [`love_preview.png`](./love_preview.png)
- Screen Artboards: [`exports/`](./exports/) (`Home.png`, `Dashboard.png`, `Match.png`, `Profile.png`, `Match Celebration.png`, `Discovery Filters.png`)

---

## 5. Development & Contribution Rules

- Always ensure `SKILL.md` frontmatter includes standard `name:` and `description:` fields.
- When adding new capabilities to `skills/`, run `python install.py` to synchronize all platform directories (`.claude/`, `.gemini/`, `.codex/`, `.kimi/`, `.zda/`, and `.agents/`).
