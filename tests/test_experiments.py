"""Pytest gate: every number in the paper must recompute here."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load(name: str) -> dict:
    return json.loads((ROOT / "results" / name).read_text(encoding="utf-8"))


def test_exp01_spanish_math():
    from experiments import exp01_hour_deficit as e
    p = e.main()
    sp = {x["scenario"]: x for x in p["spotlight"]["Spanish"]}
    assert sp["fsi_class"]["req_h_per_day_90d"] == round(690 / 90, 2) == 7.67
    assert sp["fsi_class"]["bootcamp_67_5h_covers_pct"] == round(100 * 67.5 / 690, 1)
    assert p["bootcamp_total_h"] == 67.5 and p["intensive_total_h"] == 720.0


def test_exp02_zipf_band():
    from experiments import exp02_zipf_coverage as e
    p = e.main()
    cov1000 = p["results"]["s=1.0"]["cov_1000"]
    assert 68 <= cov1000 <= 86, cov1000


def test_exp03_spaced_beats_massed():
    from experiments import exp03_srs_simulator as e
    s = e.simulate()
    assert s["ret_spaced_d30"] > s["ret_massed_d30"]
    assert s["lift_pp"] > 0


def test_exp04_cognate_mechanism_and_qualifier():
    from experiments import exp04_cognate_overlap as e
    p = e.main()
    assert p["n_sample"] >= 20
    assert p["fr_cognate_like_rate"] >= 0.70
    assert p["false_friend_present"] is True


def test_exp05_production_ranking():
    from experiments import exp05_output_specificity as e
    p = e.main()
    g = p["grid"]
    assert g["speak-day-one+feedback"]["60d"]["P"] >= g["balanced-70-30"]["60d"]["P"] >= g["input-only"]["60d"]["P"]
    assert g["input-only"]["7d"]["C"] >= g["speak-day-one+feedback"]["7d"]["C"]


def test_exp06_always_writes():
    from experiments import exp06_live_market_check as e
    p = e.main()
    assert "live" in p and "snapshot" in p
    assert p["snapshot"]["fsi_catIV_hours"] == 2200


def test_summary_exists_after_run():
    import subprocess, sys
    r = subprocess.run([sys.executable, "-m", "experiments.run_all"], cwd=str(ROOT), capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[-2000:]
    assert (ROOT / "results" / "summary.json").exists()
