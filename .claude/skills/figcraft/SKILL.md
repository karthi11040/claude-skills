---
name: figcraft
description: Automate, generate, inspect, convert, and render FigCraft (.figcraft) interface designs and prototypes using figcraft-cli and the FigCraft Model Context Protocol (MCP) server. Use when an AI agent (Antigravity, Claude Code, Claude Desktop, ChatGPT, OpenAI Codex) needs to inspect, create, edit, or export .figcraft files or drive a live FigCraft desktop design session.
---

# FigCraft Agent Skill & Automation Guide

FigCraft is an open-source, local-first interface design and prototyping tool built in pure Rust as an independent alternative to Figma. FigCraft saves designs directly on disk as `.figcraft` archives (ZIP-based files enclosing `document.json` and assets) and provides both a graphical desktop application and a headless automation engine (`figcraft-cli`).

This skill teaches AI agents (**Antigravity**, **Claude Code**, **Claude Desktop**, **ChatGPT / Codex**, and custom agents) how to interact with, create, modify, inspect, and export FigCraft designs programmatically.

---

## 1. Engine & CLI Locations

On Windows, the FigCraft binaries are located at:
- **CLI Tool:** `D:\applications\FigCraft\FigCraft\figcraft-cli.exe` (or in `PATH` / AppData)
- **Desktop App:** `D:\applications\FigCraft\FigCraft\figcraft.exe`

*(On macOS / Linux, `figcraft` and `figcraft-cli` are typically in `/usr/local/bin` or `~/.local/bin`.)*

To check CLI availability:
```powershell
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" --version
```

---

## 2. Model Context Protocol (MCP) Server Setup

FigCraft features a native built-in MCP server directly in `figcraft-cli mcp`. Any MCP-compatible AI agent can connect to it to inspect layers, create shapes, modify styles, and execute commands over `stdio`.

### A. Claude Code
Register FigCraft with Claude Code in one command:
```bash
claude mcp add figcraft -- D:/applications/FigCraft/FigCraft/figcraft-cli.exe mcp
```

### B. Claude Desktop
Edit `%APPDATA%\Claude\claude_desktop_config.json` (or `~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):
```json
{
  "mcpServers": {
    "figcraft": {
      "command": "D:\\applications\\FigCraft\\FigCraft\\figcraft-cli.exe",
      "args": ["mcp"]
    }
  }
}
```

### C. Antigravity IDE & CLI
In Antigravity or VS Code MCP configuration (`mcp_config.json` / settings):
```json
{
  "mcpServers": {
    "figcraft": {
      "command": "D:\\applications\\FigCraft\\FigCraft\\figcraft-cli.exe",
      "args": ["mcp"],
      "env": {}
    }
  }
}
```

### D. ChatGPT / OpenAI Codex / Custom Agents
For tools that use standard JSON-RPC over stdio or subprocess execution:
Spawn `figcraft-cli.exe mcp` as a subprocess with standard input/output redirection to invoke the 400+ commands exposed by FigCraft's engine.

---

## 3. Two Modes of Agent Operation

### Mode 1: Headless Mode (Autonomous File Generation & Modification)
The agent operates directly on files (`.figcraft`, `.json`, `.svg`) without launching any UI window:
- Run a batch script: `figcraft-cli run script.json --in app.figcraft --out app.figcraft`
- Convert formats: `figcraft-cli convert app.figcraft app.json`
- Render visual snapshots: `figcraft-cli render --out preview.png app.figcraft`
- Export individual frames: `figcraft-cli export --out exports/ app.figcraft`

### Mode 2: Attached Mode (Real-Time Live UI Collaboration)
The human user opens the desktop app, and the agent drives the open canvas live so the user watches changes occur in real time:
1. **Start FigCraft with control port:**
   ```powershell
   & "D:\applications\FigCraft\FigCraft\figcraft.exe" --control 7979
   ```
2. **Attach MCP server to the running app:**
   ```bash
   claude mcp add figcraft-live -- D:/applications/FigCraft/FigCraft/figcraft-cli.exe mcp --attach 7979
   ```

---

## 4. Headless Scripting via `figcraft-cli run`

The most powerful way for an agent to create or edit designs is using `figcraft-cli run`.
The script is a JSON array of commands executed as a single atomic transaction:
```json
[
  { "command": "frame.create", "params": { "name": "Screen", "width": 393, "height": 852, "props": { "fill": "#0D0E16" } } },
  { "command": "text.create", "params": { "parent": 2, "text": "Hello World", "x": 40, "y": 60, "props": { "fontSize": 24, "fill": "#FFFFFF" } } }
]
```

Run the script:
```powershell
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" run script.json --out output.figcraft
```

### Node ID Sequencing Rule
- When starting a new document, `Page 1` is assigned `id: 1`.
- Every subsequent create command (`frame.create`, `shape.rectangle`, `text.create`, `vector.create`, etc.) receives the next sequential integer ID: `2`, `3`, `4`...
- Nested layers reference their container via `"parent": <id>`.

---

## 5. Core Command Reference for Agents

### `frame.create`
Creates a container frame (screen, card, or component):
```json
{
  "command": "frame.create",
  "params": {
    "name": "Home Screen",
    "x": 60,
    "y": 100,
    "width": 393,
    "height": 852,
    "props": {
      "fill": "#0E0F17",
      "cornerRadius": 44,
      "clip": true
    }
  }
}
```
*Standard mobile presets available:* `iPhone 16` (`393 x 852`), `iPhone 16 Pro` (`402 x 874`), `iPhone 16 Pro Max` (`440 x 956`), `Android Compact` (`412 x 917`).

### `shape.rectangle`
Creates cards, buttons, status bars, and dividers:
```json
{
  "command": "shape.rectangle",
  "params": {
    "parent": 2,
    "name": "ActionCard",
    "x": 20,
    "y": 140,
    "width": 353,
    "height": 180,
    "props": {
      "fill": "#1B1D2C",
      "stroke": "#FFFFFF15",
      "strokeWeight": 1,
      "cornerRadius": 20
    }
  }
}
```

### Linear & Radial Gradients
Gradients are specified in `props.fills`:
```json
"props": {
  "fills": [
    {
      "type": "linearGradient",
      "stops": ["#FF385C", "#FF6584"],
      "from": [0, 0],
      "to": [1, 1]
    }
  ]
}
```

### `shape.ellipse`
Creates circular avatars, status dots, and badges:
```json
{
  "command": "shape.ellipse",
  "params": {
    "parent": 2,
    "name": "AvatarCircle",
    "x": 30,
    "y": 50,
    "width": 60,
    "height": 60,
    "props": {
      "fills": [{"type": "linearGradient", "stops": ["#FF416C", "#FF4B2B"], "from": [0,0], "to": [1,1]}],
      "stroke": "#FFFFFF",
      "strokeWeight": 2
    }
  }
}
```

### `text.create`
Creates typography layers:
```json
{
  "command": "text.create",
  "params": {
    "parent": 2,
    "text": "Chloe Bennett, 24",
    "x": 36,
    "y": 460,
    "props": {
      "fontSize": 24,
      "fontFamily": "Inter",
      "fontStyle": "Bold",
      "fill": "#FFFFFF"
    }
  }
}
```

### `vector.create`
Creates crisp icons directly from standard SVG path strings:
```json
{
  "command": "vector.create",
  "params": {
    "parent": 2,
    "name": "HeartIcon",
    "path": "M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z",
    "x": 256,
    "y": 684,
    "width": 30,
    "height": 30,
    "props": {
      "fill": "#FFFFFF"
    }
  }
}
```

### `proto.interaction.add`
Links frames and elements for interactive prototypes:
```json
{
  "command": "proto.interaction.add",
  "params": {
    "id": 14,
    "dest": 78,
    "trigger": { "type": "onClick" },
    "action": { "type": "navigate" },
    "transition": { "type": "smartAnimate", "direction": "left" }
  }
}
```

---

## 6. Inspecting, Exporting & Verifying Designs

### Inspect Document Structure:
```powershell
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" info design.figcraft
```
Outputs total node counts, pages, top-level frames, and dimensions.

### Convert to Human-Readable JSON:
```powershell
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" convert design.figcraft design.json
```

### Render Full Canvas Snapshot to PNG:
```powershell
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" render --out snapshot.png design.figcraft
```

### Export Individual Frames to PNG / SVG / PDF:
```powershell
& "D:\applications\FigCraft\FigCraft\figcraft-cli.exe" export --out exports/ design.figcraft
```

---

## 7. Recommended Python Automation Boilerplate for Agents

Agents can write a lightweight Python script to construct clean, complex designs deterministically:

```python
import json
import subprocess

commands = []
current_id = 1  # Page 1 is ID 1

def add_command(cmd, params):
    global current_id
    commands.append({"command": cmd, "params": params})
    if cmd in ["frame.create", "shape.rectangle", "shape.ellipse", "text.create", "vector.create"]:
        current_id += 1
        return current_id
    return None

# Build UI elements
frame_id = add_command("frame.create", {
    "name": "Mobile Screen",
    "width": 393, "height": 852, "x": 0, "y": 0,
    "props": {"fill": "#0E0F17", "cornerRadius": 44, "clip": True}
})

add_command("shape.rectangle", {
    "parent": frame_id, "name": "HeroCard",
    "x": 20, "y": 120, "width": 353, "height": 500,
    "props": {"fill": "#1A1D2B", "cornerRadius": 24}
})

add_command("text.create", {
    "parent": frame_id, "text": "Explore Tonight ✨",
    "x": 40, "y": 520,
    "props": {"fontSize": 24, "fontFamily": "Inter", "fontStyle": "Bold", "fill": "#FFFFFF"}
})

# Save and compile
with open("build.json", "w", encoding="utf-8") as f:
    json.dump(commands, f, indent=2)

subprocess.run(["D:/applications/FigCraft/FigCraft/figcraft-cli.exe", "run", "build.json", "--out", "app.figcraft"])
subprocess.run(["D:/applications/FigCraft/FigCraft/figcraft-cli.exe", "render", "--out", "preview.png", "app.figcraft"])
print("FigCraft build completed successfully!")
```

