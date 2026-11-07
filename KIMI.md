# KIMI.md — Moonshot Kimi Tool Skills Guide

## Overview
This repository provides modular **AI Tool Skills** configured for **Moonshot AI Kimi** (Kimi K2.6 Turbo, Kimi Code, and FirePass).

---

## 1. Quick Installation

### Via `npx skills add`:
```bash
npx skills add karthi11040/claude-skills
```

### Via Python:
```bash
python install.py --platform kimi
```

---

## 2. Available Tool Skills

- **`figcraft`** (`.kimi/skills/figcraft/SKILL.md`): Vector design automation, frame queries, and headless rendering.
- **`dating-app-design`** (`.kimi/skills/dating-app-design/SKILL.md`): Mobile product design tokens, card stack mechanics, and feeds.
- **`deep-research-synthesizer`** (`.kimi/skills/deep-research-synthesizer/SKILL.md`): Multi-perspective investigation and evidence grading.

---

## 3. Tool Execution

```bash
FIGCRAFT="D:/applications/FigCraft/FigCraft/figcraft-cli.exe"

# Query design
"$FIGCRAFT" info love.figcraft

# Render visual preview
"$FIGCRAFT" render --out love_preview.png love.figcraft

# Export frames
"$FIGCRAFT" export --out exports/ love.figcraft
```
