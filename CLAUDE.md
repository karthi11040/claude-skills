# CLAUDE.md — Claude Code Tool Skills & Plugin Guide

## Overview
This repository provides production-grade **AI Tool Skills** for **Claude Code** and **Claude Desktop**, teaching Claude how to drive external design and research tools.

---

## 1. Installation via Claude Code Marketplace

```bash
# Add this repository to Claude Code
/plugin marketplace add karthi11040/claude-skills

# Install the all-in-one bundle:
/plugin install engineering-skills@claude-code-skills

# Or install individual skills:
/plugin install figcraft@claude-code-skills
/plugin install dating-app-design@claude-code-skills
/plugin install deep-research-synthesizer@claude-code-skills
```

---

## 2. Available Tool Skills for Claude

- **`figcraft`** (`skills/figcraft/SKILL.md`): Direct CLI and MCP automation for vector design creation, layer queries, rendering, and PNG export.
- **`dating-app-design`** (`skills/dating-app-design/SKILL.md`): Mobile design system tokens, swipe physics, and interaction architectures.
- **`deep-research-synthesizer`** (`skills/deep-research-synthesizer/SKILL.md`): Multi-perspective investigation, evidence verification, and decision dossiers.

---

## 3. How Claude Executes the Tools

### Driving FigCraft via CLI:
```powershell
# Inspect design
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" info love.figcraft

# Render visual preview
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" render --out love_preview.png love.figcraft

# Export individual screens
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" export --out exports/ love.figcraft
```

### Driving FigCraft via MCP:
```bash
claude mcp add figcraft -- D:/applications/FigCraft/FigCraft/figcraft-cli.exe mcp
```
For live interactive control with the open desktop window:
```bash
claude mcp add figcraft-live -- D:/applications/FigCraft/FigCraft/figcraft-cli.exe mcp --attach 7979
```
