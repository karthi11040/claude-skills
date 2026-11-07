# CODEX.md — OpenAI Codex & GitHub Copilot Tool Skills Guide

## Overview
This repository provides production-grade **AI Tool Skills** for **OpenAI Codex**, **GitHub Copilot CLI**, and universal AI developer agents.

---

## 1. Quick Installation

### Via `npx skills add`:
```bash
npx skills add karthi11040/claude-skills -a codex
```

### Via Python Installer:
```bash
python install.py --platform codex
```

---

## 2. Available Tool Skills

1. **`figcraft`** (`skills/figcraft/SKILL.md`): Inspect, edit, render, and export vector design files programmatically.
2. **`dating-app-design`** (`skills/dating-app-design/SKILL.md`): Mobile design system tokens, gesture physics, and interaction models.
3. **`deep-research-synthesizer`** (`skills/deep-research-synthesizer/SKILL.md`): Algorithmic evidence verification, dispute resolution, and decision reporting.

---

## 3. How Codex Executes Tools

```powershell
# Inspect design document
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" info love.figcraft

# Render visual preview
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" render --out love_preview.png love.figcraft

# Export all artboards
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" export --out exports/ love.figcraft
```
