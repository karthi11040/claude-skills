# AGENTS.md — Universal Multi-Agent Workspace Guide

Welcome to the **Amour Dating App & Agentic Design System** repository. This repository is configured to be fully agentic, supporting **OpenAI Codex**, **Claude**, **Gemini / Antigravity**, **Kimi (Moonshot)**, **ZDA (Z.ai / GLM)**, and **OpenCode**.

---

## 1. Project Overview & Artifacts

- **Core Design File**: `love.figcraft` (Native FigCraft local archive, containing 6 mobile screens for an iOS dating app).
- **Screens Render**: `love_preview.png` (High-res snapshot of all 6 frames side-by-side).
- **Exported PNGs**: `exports/` (`Home.png`, `Dashboard.png`, `Match.png`, `Profile.png`, `Match Celebration.png`, `Discovery Filters.png`).
- **Skills Directory**: `skills/` (and platform-specific mirrors in `.claude/skills/`, `.gemini/skills/`, `.codex/skills/`, `.zda/skills/`, `.kimi/skills/`, `.agents/skills/`).

---

## 2. Available Agent Skills

This repository provides 3 production-grade agent skills:

1. **`figcraft`** (`skills/figcraft/`):
   - Automates inspecting, editing, converting, running, and exporting `.figcraft` vector design files via `figcraft-cli`.
   - Supports both headless CLI automation and live desktop UI control via MCP (`figcraft-cli mcp`).

2. **`dating-app-design`** (`skills/dating-app-design/`):
   - Full mobile UX architecture, dark obsidian color tokens, swipe physics, card hierarchies, and micro-interactions for modern dating platforms.

3. **`deep-research-synthesizer`** (`skills/deep-research-synthesizer/`):
   - Investigates complex queries, scores source evidence credibility, reconciles conflicting viewpoints, and outputs structured decision dossiers.

---

## 3. Tooling & CLI Reference

FigCraft is powered by the local Rust binary `figcraft-cli`:
- **Path on Windows**: `D:\applications\FigCraft\FigCraft\figcraft-cli.exe`
- **Inspect**: `figcraft-cli info love.figcraft`
- **Render canvas**: `figcraft-cli render --out love_preview.png love.figcraft`
- **Export frames**: `figcraft-cli export --out exports/ love.figcraft`
- **Convert format**: `figcraft-cli convert love.figcraft love.json`
- **Execute script**: `figcraft-cli run script.json --in love.figcraft --out love.figcraft`

---

## 4. Development & Contribution Rules

- Always preserve existing design layers, node IDs, and prototype interaction links when updating `love.figcraft`.
- Ensure exported snapshots in `exports/` match changes made to `love.figcraft`.
- Keep all skill mirrors in `.claude/`, `.gemini/`, `.codex/`, `.zda/`, and `.kimi/` synchronized with `skills/`.
