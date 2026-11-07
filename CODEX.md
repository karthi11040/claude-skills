# CODEX.md — OpenAI Codex & GitHub Copilot Agent Guide

## Overview
This repository contains **Amour**, an iOS mobile dating application designed in **FigCraft**, equipped with AI agent skills and automation workflows for **OpenAI Codex**, **GitHub Copilot CLI**, and universal AI developer harnesses.

---

## 1. Codex Agent Skills Directory

Codex agents discover skills from `.codex/skills/` or the root `skills/` directory:

1. **`figcraft`** (`.codex/skills/figcraft/SKILL.md`):
   - Automates inspecting, editing, converting, running, and exporting `.figcraft` vector design files via `figcraft-cli`.
2. **`dating-app-design`** (`.codex/skills/dating-app-design/SKILL.md`):
   - Mobile product design guidelines: swipe stacks, micro-interactions, conversation feeds, verification badges, and dark-mode color tokens.
3. **`deep-research-synthesizer`** (`.codex/skills/deep-research-synthesizer/SKILL.md`):
   - Multi-source research synthesis, confidence scoring, evidence matrix mapping, and structured reporting.

---

## 2. FigCraft CLI Automation Commands

Codex can execute the local `figcraft-cli` binary directly:

```powershell
# Inspect design document
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" info love.figcraft

# Render full canvas composite
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" render --out love_preview.png love.figcraft

# Export all artboard frames
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" export --out exports/ love.figcraft

# Convert to JSON and back
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" convert love.figcraft love.json
```

---

## 3. Directory Layout

```
love/
├── love.figcraft               # FigCraft native vector document (6 screens, 435 nodes)
├── love_preview.png            # Visual composite render of all frames
├── exports/                    # Exported individual screen PNGs
├── skills/                     # Canonical skills directory
├── .codex/skills/              # OpenAI Codex skill mount directory
├── CODEX.md                    # This instructions file
├── AGENTS.md                   # Universal agent instructions
├── CLAUDE.md                   # Claude Code instructions
├── GEMINI.md                   # Gemini / Antigravity instructions
├── KIMI.md                     # Moonshot Kimi instructions
└── ZDA.md                      # Z.ai Developer Agent instructions
```
