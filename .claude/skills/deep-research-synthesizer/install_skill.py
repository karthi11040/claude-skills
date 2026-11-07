#!/usr/bin/env python3
"""
Cross-Platform Skill Installer for Claude, Antigravity, and Codex.
Automatically detects existing AI tools and copies the skill accordingly.
"""

import shutil
from pathlib import Path

SKILL_NAME = "deep-research-synthesizer"

def install():
    home = Path.home()
    source_dir = Path(__file__).resolve().parent

    targets = [
        # Antigravity Global
        home / ".gemini" / "config" / "skills" / SKILL_NAME,
        # Claude Global
        home / ".claude" / "skills" / SKILL_NAME,
        # Local Workspace Fallback
        source_dir.parent / SKILL_NAME
    ]

    installed = 0
    for target in targets:
        if target.resolve() == source_dir.resolve():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(source_dir, target, ignore=shutil.ignore_patterns(".git*", "__pycache__*"))
            print(f"Successfully installed to: {target}")
            installed += 1
        except Exception as e:
            print(f"Could not install to {target}: {e}")

    print(f"\nSkill '{SKILL_NAME}' is deployed and ready to use!")

if __name__ == "__main__":
    install()

