#!/usr/bin/env python3
"""
Amour Multi-Agent Skills Universal Installer
Installs all bundled skills ('figcraft', 'dating-app-design', 'deep-research-synthesizer')
directly into your local AI agent directories (Claude, Gemini / Antigravity, Codex, Kimi, ZDA).
"""

import sys
import shutil
import argparse
from pathlib import Path

SKILLS = ["figcraft", "dating-app-design", "deep-research-synthesizer"]

def get_platform_targets():
    home = Path.home()
    return {
        "claude": [
            home / ".claude" / "skills",
        ],
        "gemini": [
            home / ".gemini" / "config" / "skills",
            home / ".gemini" / "antigravity" / "skills",
        ],
        "codex": [
            home / ".codex" / "skills",
        ],
        "kimi": [
            home / ".kimi" / "skills",
        ],
        "zda": [
            home / ".zda" / "skills",
        ],
        "universal": [
            home / ".agents" / "skills",
        ]
    }

def install_skills(platforms=None, custom_path=None):
    root_dir = Path(__file__).resolve().parent
    source_skills_dir = root_dir / "skills"
    
    if not source_skills_dir.exists():
        print(f"Error: Skills source directory '{source_skills_dir}' not found.")
        return 1

    targets = []
    platform_map = get_platform_targets()

    if custom_path:
        targets.append(Path(custom_path).resolve())
    elif platforms:
        for p in platforms:
            p_clean = p.lower().strip()
            if p_clean in platform_map:
                targets.extend(platform_map[p_clean])
            else:
                print(f"Warning: Unknown platform '{p_clean}'. Available: {list(platform_map.keys())}")
    else:
        # Default: install to all available/detected platform folders
        for plist in platform_map.values():
            targets.extend(plist)

    total_installed = 0
    for target_base in targets:
        try:
            target_base.mkdir(parents=True, exist_ok=True)
            for skill in SKILLS:
                src = source_skills_dir / skill
                dst = target_base / skill
                if src.exists():
                    if dst.exists():
                        shutil.rmtree(dst)
                    shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".git*", "__pycache__*", "*.pyc"))
                    print(f"  ✓ Installed '{skill}' -> {dst}")
                    total_installed += 1
        except Exception as e:
            print(f"  ✗ Failed to install to {target_base}: {e}")

    print(f"\nDone! Successfully deployed {total_installed} skill packages.")
    return 0

def main():
    parser = argparse.ArgumentParser(description="Install Amour AI Skills directly into agent environments.")
    parser.add_argument("--platform", "-p", nargs="+", help="Specific platforms to target (claude, gemini, codex, kimi, zda, universal)")
    parser.add_argument("--dest", "-d", help="Custom destination directory to install skills into")
    args = parser.parse_args()

    return install_skills(platforms=args.platform, custom_path=args.dest)

if __name__ == "__main__":
    sys.exit(main())

