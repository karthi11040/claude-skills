# ZDA.md — Z.ai Developer Agent (GLM) Tool Skills Guide

## Overview
This repository provides production-grade **AI Tool Skills** for **Z.ai Developer Agent (ZDA)**, **GLM-4 / CodeGeeX**, and Z.ai developer tools.

---

## 1. Quick Installation

### Via `npx skills add`:
```bash
npx skills add karthi11040/claude-skills
```

### Via Python:
```bash
python install.py --platform zda
```

---

## 2. Available Tool Skills

1. **`figcraft`** (`.zda/skills/figcraft/SKILL.md`): Vector node manipulation, layer queries, rendering, and headless exports.
2. **`dating-app-design`** (`.zda/skills/dating-app-design/SKILL.md`): Mobile design tokens, card swipe physics, and micro-interactions.
3. **`deep-research-synthesizer`** (`.zda/skills/deep-research-synthesizer/SKILL.md`): Multi-source research synthesis and evidence verification.

---

## 3. Tool Execution Reference

```powershell
$CLI = "D:\applications\FigCraft\FigCraft\figcraft-cli.exe"

# Query file metadata
& $CLI info love.figcraft

# Generate composite preview image
& $CLI render --out love_preview.png love.figcraft

# Export all artboard frames
& $CLI export --out exports/ love.figcraft
```
