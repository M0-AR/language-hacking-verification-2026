"""Run all experiments -> results/summary.json (deterministic, offline-safe)."""
from __future__ import annotations
import json
from pathlib import Path
from . import exp01_hour_deficit, exp02_zipf_coverage, exp03_srs_simulator, exp04_cognate_overlap, exp05_output_specificity, exp06_live_market_check

ROOT = Path(__file__).resolve().parents[1]


def main() -> dict:
    results = {
        "exp01": exp01_hour_deficit.main(),
        "exp02": exp02_zipf_coverage.main(),
        "exp03": exp03_srs_simulator.main(),
        "exp04": exp04_cognate_overlap.main(),
        "exp05": exp05_output_specificity.main(),
        "exp06": exp06_live_market_check.main(),
    }
    summary = {
        "lab": "language-hacking-verification-2026",
        "question": "Which Benny Lewis Language-Hacking claims survive confrontation with FSI hours, SLA meta-analyses, and public market data?",
        "one_line": (
            "15-min conversation in 90d: PLAUSIBLE (A1-A2, output+feedback); "
            "B2/C1 fluency in 90d at 45min/d: REFUTED by 8-32x hour deficit; "
            "at 8h/d: PLAUSIBLE for Cat I only."
        ),
        "experiments": {k: v.get("verdict", "") for k, v in results.items()},
    }
    out = ROOT / "results" / "summary.json"
    out.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return summary


if __name__ == "__main__":
    main()
