# ZDA.md — Z.ai Developer Agent (GLM) Guide

## Overview
This repository contains **Amour**, an iOS mobile dating application designed in **FigCraft**, equipped with AI agent skills tailored for **Z.ai Developer Agent (ZDA)**, **GLM-4 / CodeGeeX**, and the Z.ai CLI tools.

---

## 1. Available ZDA Skills

ZDA agents automatically discover skills configured in `.zda/skills/` or the root `skills/` directory:

1. **`figcraft`** (`.zda/skills/figcraft/SKILL.md`):
   - Command-line automation for FigCraft (`.figcraft`) design projects, vector node editing, layer queries, rendering, and headless exports.
2. **`dating-app-design`** (`.zda/skills/dating-app-design/SKILL.md`):
   - Mobile product design guidelines: swipe stacks, micro-interactions, conversation feeds, verification badges, and dark-mode color tokens.
3. **`deep-research-synthesizer`** (`.zda/skills/deep-research-synthesizer/SKILL.md`):
   - Multi-source research synthesis, confidence scoring, evidence matrix mapping, and structured reporting.

---

## 2. Command Reference

Execute FigCraft tasks via the Windows CLI:

```powershell
$CLI = "D:\applications\FigCraft\FigCraft\figcraft-cli.exe"

# Query file metadata, artboard dimensions, and node counts
& $CLI info love.figcraft

# Generate composite preview image
& $CLI render --out love_preview.png love.figcraft

# Export all artboard frames into the exports/ folder
& $CLI export --out exports/ love.figcraft

# Convert between binary archive and human-readable JSON
& $CLI convert love.figcraft love.json
& $CLI convert love.json love_rebuilt.figcraft
```

---

## 3. Screen Inventory

| Screen | Dimensions | Position (X, Y) | Description |
|---|---|---|---|
| **Home** | `393 × 852` pt | (0, 0) | Swipe discovery card with Chloe (24), badges, bio prompt, and 5 action buttons |
| **Dashboard** | `393 × 852` pt | (440, 0) | Activity search, vibe pills, Today's Spotlight, Top Picks grid, and Live Radar |
| **Match** | `393 × 852` pt | (880, 0) | Story circles with gold likes counter, celebration banner, and 5 chat threads |
| **Profile** | `393 × 852` pt | (1320, 0) | Avatar with camera badge, VIP Platinum, completion bar, metrics, and tags |
| **Match Celebration** | `393 × 852` pt | (1760, 0) | Celebration modal with dual overlapping avatars, heart badge, and icebreaker input |
| **Discovery Filters** | `393 × 852` pt | (2200, 0) | Interactive bottom sheet with distance and age sliders and verification toggles |

---

## 4. Best Practices for ZDA Agents

- When updating vector layers, always validate that colors use valid 8-digit RGBA hex notation (e.g., `#FF4B72FF`, `#0D0E15FF`).
- Run `& $CLI export --out exports/ love.figcraft` after making design modifications to synchronize the exported PNG files.
- Maintain consistency across all skill directories (`.zda/`, `.claude/`, `.gemini/`, `.codex/`, `.kimi/`, and `.agents/`).
