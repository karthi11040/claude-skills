# Agent Instructions: FigCraft Automation

## Trigger Condition
Activate when the user asks to inspect, create, edit, or export `.figcraft` design files or automate FigCraft.

## Execution Rules
1. **Engine Path**:
   - `D:\applications\FigCraft\FigCraft\figcraft-cli.exe`
2. **Commands**:
   - Inspect: `figcraft-cli info <file.figcraft>`
   - Convert: `figcraft-cli convert <file.figcraft> <file.json>`
   - Run script: `figcraft-cli run <script.json> --out <file.figcraft>`
   - Render preview: `figcraft-cli render --out <preview.png> <file.figcraft>`
   - Export frames: `figcraft-cli export --out <folder/> <file.figcraft>`
3. **Sequential ID Rule**:
   - In a fresh document, Page 1 is `id: 1`. Each create command receives sequential integer IDs (`2`, `3`, `4`...).
   - Nested elements reference their parent via `"parent": <id>`.
4. **MCP Server**:
   - `figcraft-cli mcp` for headless operation.
   - `figcraft --control 7979` + `figcraft-cli mcp --attach 7979` for live UI control.

