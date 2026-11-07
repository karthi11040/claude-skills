#!/usr/bin/env python3
"""
Evidence Credibility & Cross-Validation Scorer
Assists AI agents and analysts in scoring reliability weights across diverse inputs.
"""

import sys
import json
from typing import List, Dict, Any

SOURCE_WEIGHTS = {
    "academic_peer_reviewed": 1.0,
    "official_documentation": 0.95,
    "independent_benchmark": 0.85,
    "practitioner_forum": 0.70,
    "reputable_journalism": 0.65,
    "vendor_whitepaper": 0.40,
    "sponsored_review": 0.15,
    "unknown": 0.30
}

def calculate_claim_confidence(confirming_sources: List[str], dissenting_sources: List[str]) -> Dict[str, Any]:
    pos_score = sum(SOURCE_WEIGHTS.get(s, 0.3) for s in confirming_sources)
    neg_score = sum(SOURCE_WEIGHTS.get(s, 0.3) for s in dissenting_sources)
    total = pos_score + neg_score
    
    if total == 0:
        return {"status": "INSUFFICIENT_DATA", "confidence": 0.0, "verdict": "Unverified"}
    
    confidence = (pos_score / total) * min(1.0, (len(confirming_sources) / 2.0))
    
    if confidence >= 0.75:
        verdict = "High Confidence Factual"
    elif confidence >= 0.45:
        verdict = "Contested / Context-Dependent"
    else:
        verdict = "Unreliable / Marketing Claim"
        
    return {
        "confidence_score": round(confidence, 3),
        "confirming_weight": round(pos_score, 2),
        "dissenting_weight": round(neg_score, 2),
        "verdict": verdict
    }

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        sample = calculate_claim_confidence(
            confirming_sources=["official_documentation", "practitioner_forum"],
            dissenting_sources=["vendor_whitepaper"]
        )
        print(json.dumps(sample, indent=2))
    else:
        print("Usage: python score_evidence.py --demo")

