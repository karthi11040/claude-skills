# KIMI.md — Moonshot Kimi Agent Project Guide

## Overview
This repository contains **Amour**, an iOS mobile dating application created in **FigCraft**, paired with multi-agent skills formatted for **Moonshot AI Kimi** (Kimi K2.6 Turbo, Kimi Code, and FirePass).

---

## 1. Direct Download & Skills Installation

### Direct Download Archive
- **PowerShell**:
  ```powershell
  Invoke-WebRequest -Uri "https://github.com/karthi11040/amour-dating-app/archive/refs/heads/main.zip" -OutFile "amour.zip"; Expand-Archive "amour.zip" -DestinationPath .
  ```
- **macOS / Linux**:
  ```bash
  curl -L "https://github.com/karthi11040/amour-dating-app/archive/refs/heads/main.zip" -o amour.zip && unzip amour.zip
  ```

### Install Skills for Kimi
Deploy skills to `~/.kimi/skills/`:
```bash
python install.py --platform kimi
```

---

## 2. Kimi Agent Skills Directory

Kimi agent environments read skills from `.kimi/skills/` or the root `skills/` directory:

- **`figcraft`** (`.kimi/skills/figcraft/SKILL.md`):
  - Interface design automation, headless rendering, frame export, and layer manipulation for `.figcraft` vector archives.
- **`dating-app-design`** (`.kimi/skills/dating-app-design/SKILL.md`):
  - Dating app UX guidelines: dark mode palette, swipe card gesture states, badges, match feeds, and profile optimization.
- **`deep-research-synthesizer`** (`.kimi/skills/deep-research-synthesizer/SKILL.md`):
  - Deep investigative workflows, evidence triangulation, source reliability grading, and structured decision dossier output.

---

## 3. Tool Integration & FigCraft CLI

Kimi code runner or terminal tools can execute the native `figcraft-cli` binary:

```bash
# Path to executable
FIGCRAFT="D:/applications/FigCraft/FigCraft/figcraft-cli.exe"

# 1. Inspect design structure
"$FIGCRAFT" info love.figcraft

# 2. Render canvas preview
"$FIGCRAFT" render --out love_preview.png love.figcraft

# 3. Export high-resolution PNGs for each artboard
"$FIGCRAFT" export --out exports/ love.figcraft

# 4. Run procedural design batch scripts
"$FIGCRAFT" run script.json --in love.figcraft --out love.figcraft
```

---

## 4. Project Structure

```
love/
├── love.figcraft               # FigCraft native vector document (6 screens, 435 nodes)
├── love_preview.png            # Visual composite render of all frames
├── install.py                  # Universal skills installer
├── exports/                    # Exported individual screen PNGs
│   ├── Home.png
│   ├── Dashboard.png
│   ├── Match.png
│   ├── Profile.png
│   ├── Match Celebration.png
│   └── Discovery Filters.png
├── skills/                     # Canonical skills directory
│   ├── figcraft/
│   ├── dating-app-design/
│   └── deep-research-synthesizer/
├── .kimi/skills/               # Kimi-specific skill mount directory
├── KIMI.md                     # This instructions file
├── AGENTS.md                   # Universal agent instructions
├── CLAUDE.md                   # Claude Code instructions
├── GEMINI.md                   # Gemini / Antigravity instructions
├── CODEX.md                    # OpenAI Codex instructions
└── ZDA.md                      # Z.ai / GLM instructions
```

---

## 5. Operating Guidelines for Kimi

1. When editing `love.figcraft`, ensure all node hierarchies, layer IDs, fills, strokes, and typography nodes are kept valid according to the FigCraft schema.
2. After applying modifications to `love.figcraft`, always re-run `figcraft-cli render --out love_preview.png love.figcraft` and `figcraft-cli export --out exports/ love.figcraft` to ensure visual outputs match the source file.
