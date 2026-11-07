#!/usr/bin/env python3
"""
Dossier Completeness & Quality Auditor
Validates that an agent's synthesized research output meets structural and evidence standards.
"""

import sys
import re

REQUIRED_SECTIONS = [
    r"Bottom Line|Executive Verdict",
    r"Comparison|Comparative Matrix|Candidate",
    r"Traps to Avoid|Fatal Flaw|Failure Modes",
    r"What To Do Next|Action Plan"
]

def audit_markdown_content(text: str) -> dict:
    findings = []
    
    # 1. Section presence
    for pattern in REQUIRED_SECTIONS:
        if not re.search(pattern, text, re.IGNORECASE):
            findings.append(f"MISSING_SECTION: Pattern '{pattern}' not identified.")

    # 2. Evidence markers
    has_metrics = bool(re.search(r"(\$|\%|\d+\s*(hours|days|ms|years|mi))", text))
    if not has_metrics:
        findings.append("LACKS_QUANTITATIVE_DATA: No prices, percentages, or measurable units found.")

    # 3. Hedge-word check (flags unverified hand-waving)
    fluff_matches = re.findall(r"\b(game-changer|revolutionary|disruptive|unmatched)\b", text, re.IGNORECASE)
    if len(fluff_matches) > 1:
        findings.append(f"MARKETING_FLUFF_DETECTED: Found ungrounded promotional terms: {set(fluff_matches)}")

    passed = len(findings) == 0
    return {
        "status": "PASSED" if passed else "FAILED",
        "score": max(0, 100 - (len(findings) * 25)),
        "issues": findings
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python verify_dossier.py <dossier.md>")
        sys.exit(1)

    file_path = sys.argv[1]
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    result = audit_markdown_content(content)
    print(f"Audit Result: {result['status']} (Score: {result['score']}/100)")
    for issue in result["issues"]:
        print(f"  - {issue}")

    sys.exit(0 if result["status"] == "PASSED" else 1)

