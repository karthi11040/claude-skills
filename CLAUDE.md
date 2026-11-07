# CLAUDE.md — Claude Code Project Guide

## Overview
This repository contains **Amour**, an iOS mobile dating application designed in **FigCraft**, paired with reusable AI agent skills for Claude Code and Claude Desktop.

---

## Direct Download & Skills Installation

### Direct Download Archive
- **PowerShell**:
  ```powershell
  Invoke-WebRequest -Uri "https://github.com/karthi11040/amour-dating-app/archive/refs/heads/main.zip" -OutFile "amour.zip"; Expand-Archive "amour.zip" -DestinationPath .
  ```
- **macOS / Linux**:
  ```bash
  curl -L "https://github.com/karthi11040/amour-dating-app/archive/refs/heads/main.zip" -o amour.zip && unzip amour.zip
  ```

### Install Skills for Claude
Run the installer to deploy directly into `~/.claude/skills/`:
```bash
python install.py --platform claude
```
Or copy manually:
```bash
cp -r skills/* ~/.claude/skills/
```

---

## Available Claude Skills
- **`figcraft`** (`.claude/skills/figcraft/SKILL.md`): Inspect, edit, render, and export `.figcraft` design files.
- **`dating-app-design`** (`.claude/skills/dating-app-design/SKILL.md`): UX patterns, design tokens, and components for dating apps.
- **`deep-research-synthesizer`** (`.claude/skills/deep-research-synthesizer/SKILL.md`): Multi-perspective research synthesis and evidence scoring.

---

## Connecting FigCraft MCP Server
```bash
claude mcp add figcraft -- D:/applications/FigCraft/FigCraft/figcraft-cli.exe mcp
```
For live interactive mode with the desktop app:
```bash
claude mcp add figcraft-live -- D:/applications/FigCraft/FigCraft/figcraft-cli.exe mcp --attach 7979
```

---

## Useful CLI Commands
- Inspect design: `& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" info love.figcraft`
- Render canvas: `& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" render --out love_preview.png love.figcraft`
- Export individual screens: `& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" export --out exports/ love.figcraft`
