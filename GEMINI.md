# GEMINI.md — Gemini & Antigravity Tool Skills Guide

## Overview
This repository provides reusable **Agent Tool Skills** for **Google Gemini CLI**, **Google Antigravity**, and the **Google GenAI SDK**, enabling models to automate vector design and execute deep research workflows.

---

## 1. Quick Installation

### Via open-source `skills` CLI:
```bash
npx skills add karthi11040/claude-skills -a gemini
```

### Via Python Installer:
```bash
python install.py --platform gemini
```

---

## 2. Available Tool Skills

- **`figcraft`** (`.gemini/skills/figcraft/SKILL.md`): Headless vector design automation, layer inspections, and frame rendering via `figcraft-cli`.
- **`dating-app-design`** (`.gemini/skills/dating-app-design/SKILL.md`): UX architecture, obsidian dark tokens, and card stack interaction models.
- **`deep-research-synthesizer`** (`.gemini/skills/deep-research-synthesizer/SKILL.md`): Automated evidence scoring and structured dossier compilation.

---

## 3. FigCraft MCP Configuration (Antigravity & Gemini)

Add to your `antigravity.json`:
```json
{
  "mcpServers": {
    "figcraft": {
      "command": "D:\\applications\\FigCraft\\FigCraft\\figcraft-cli.exe",
      "args": ["mcp"]
    },
    "figcraft-live": {
      "command": "D:\\applications\\FigCraft\\FigCraft\\figcraft-cli.exe",
      "args": ["mcp", "--attach", "7979"]
    }
  }
}
```

---

## 4. How the Model Executes Commands

```powershell
# Inspect design document
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" info love.figcraft

# Generate visual canvas preview
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" render --out love_preview.png love.figcraft

# Export all artboards to PNG
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" export --out exports/ love.figcraft
```
