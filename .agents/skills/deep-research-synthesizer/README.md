# Deep Research Synthesizer Skill

A cross-platform agent skill for **Claude**, **Codex / OpenCode**, and **Antigravity**. It performs multi-perspective investigations on complex queries, cross-verifies conflicting claims, evaluates evidence reliability, and generates structured, bias-checked decision dossiers.

## Directory Structure
```text
deep-research-synthesizer/
├── SKILL.md                          # Claude & Antigravity spec
├── AGENTS.md                         # OpenAI Codex / OpenCode spec
├── scripts/
│   ├── score_evidence.py            # Evidence reliability scorer
│   └── verify_dossier.py            # Automated output quality auditor
├── templates/
│   ├── executive-brief.md            # Template for non-technical users
│   └── technical-deep-dive.md        # Template for engineering users
└── install_skill.py                  # One-command installer
```

## Quick Installation

Run the included install script:
```bash
python install_skill.py
```
This automatically links the skill into your active Claude, Codex, and Antigravity skill directories.

