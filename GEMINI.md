# GEMINI.md — Gemini & Antigravity Agent Guide

## Overview
This repository contains **Amour**, a high-fidelity iOS mobile dating application created in **FigCraft**, equipped with reusable skills for **Google Gemini CLI**, **Google Antigravity**, and the **Google GenAI SDK**.

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

### Install Skills for Gemini / Antigravity
Deploy skills directly to your Gemini/Antigravity global config:
```bash
python install.py --platform gemini
```
Or manually copy skills to:
- `~/.gemini/config/skills/`
- `~/.gemini/antigravity/skills/`

---

## 2. Available Skills for Gemini / Antigravity

Gemini and Antigravity automatically discover skills located under `.gemini/skills/` or `skills/`:

- **`figcraft`** (`.gemini/skills/figcraft/SKILL.md`):
  - Automates headless vector design manipulation, inspections, layer queries, and rendering for `.figcraft` archives via `figcraft-cli`.
- **`dating-app-design`** (`.gemini/skills/dating-app-design/SKILL.md`):
  - Full mobile UX architecture: Obsidian dark theme, match queues, discovery card physics, and interaction paradigms.
- **`deep-research-synthesizer`** (`.gemini/skills/deep-research-synthesizer/SKILL.md`):
  - Multi-perspective evidence verification, truth-testing algorithms, and structured decision dossier generation.

---

## 3. MCP Server Configuration (Antigravity & Gemini)

To connect FigCraft as a Model Context Protocol (MCP) server in your `antigravity.json` or Gemini environment:

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

## 4. Essential Commands

Run these commands in PowerShell / Terminal:

```powershell
# Inspect the design file and layer statistics
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" info love.figcraft

# Render full canvas preview
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" render --out love_preview.png love.figcraft

# Export all individual screen frames to PNG
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" export --out exports/ love.figcraft

# Convert binary FigCraft format to JSON schema
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" convert love.figcraft love.json
```

---

## 5. Mobile Screens Reference (`love.figcraft`)

1. **Home** (`393 × 852` pt, x: 0): Main swipe card discovery stack with Chloe (24), badges, quote prompt, and 5 floating action buttons.
2. **Dashboard** (`393 × 852` pt, x: 440): Activity feed, Today's Spotlight, Top Picks grid, and Live Radar.
3. **Match** (`393 × 852` pt, x: 880): Stories bar with gold likes disk, match celebration banner, and message conversations.
4. **Profile** (`393 × 852` pt, x: 1320): Profile picture, VIP badge, 92% completion meter, stats, and lifestyle tags.
5. **Match Celebration** (`393 × 852` pt, x: 1760): "It's a Match!" celebration modal with overlapping avatars, heart badge, and icebreaker input.
6. **Discovery Filters** (`393 × 852` pt, x: 2200): Interactive bottom sheet preferences with dual range sliders and verified toggles.
