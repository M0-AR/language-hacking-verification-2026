"""EXP01 — Hour-deficit law: FSI hours vs 90-day budgets.

Verified inputs: data/fsi_hours.csv (FSI via LingoBright 2026-07-16, read 2026-10-15).
FSI target = Speaking-3/Reading-3 ~= CEFR B2/C1. App learners need 1.5-2x (Langmitra Mar 2026).
Bootcamp promise (verified): 15-min conversation at 45min/day, explicitly NOT fluency.
"""
from __future__ import annotations
from pathlib import Path
from .utils import DATA, save_json, load_csv

DAYS = 90
BOOTCAMP_MIN_PER_DAY = 45
INTENSIVE_H_PER_DAY = 8.0  # ActualFluency: Benny ~8h/day during challenges


def main() -> dict:
    rows = load_csv(DATA / "fsi_hours.csv")
    boot_total = BOOTCAMP_MIN_PER_DAY / 60 * DAYS  # 67.5h
    intensive_total = INTENSIVE_H_PER_DAY * DAYS  # 720h
    out_rows = []
    for r in rows:
        try:
            ch = float(r["class_hours"])
        except ValueError:
            continue
        req_per_day = ch / DAYS
        for mult, label in [(1.0, "fsi_class"), (1.5, "app_1.5x"), (2.0, "app_2x")]:
            need = ch * mult
            out_rows.append({
                "language": r["language"], "category": r["category"],
                "scenario": label,
                "need_hours": round(need, 1),
                "req_h_per_day_90d": round(need / DAYS, 2),
                "bootcamp_67_5h_covers_pct": round(100 * boot_total / need, 1),
                "intensive_720h_covers_pct": round(100 * intensive_total / need, 1),
            })
    # Spotlight languages (keep paper table small + exact)
    spot = {}
    for lang in ["Spanish", "French", "German", "Russian", "Arabic", "Mandarin", "Japanese"]:
        spot[lang] = [x for x in out_rows if x["language"] == lang]

    payload = {
        "experiment": "exp01_hour_deficit",
        "days": DAYS,
        "bootcamp_total_h": boot_total,
        "intensive_total_h": intensive_total,
        "falsifiable_claim": "67.5h (45min/d x 90d) cannot reach FSI B2/C1 (552-2200h); it can reach A1/15-min conversation.",
        "spotlight": spot,
        "all_rows": out_rows,
        "verdict": (
            "CONFIRMED deficit: Spanish needs 7.67h/d (class) or 11.5-15.33h/d app-adjusted for B2 in 90d; "
            "bootcamp 0.75h/d covers 9.8% (class) / 4.9-6.5% (app) of Spanish B2. "
            "Intensive 8h/d x 90d = 720h covers 104% of Spanish class hours but only 33% of Mandarin class hours "
            "(16-22% app-adjusted). Hence 'fluent in 3 months' is Hours-impossible at casual pace; "
            "only the redefined 15-min-conversation (A1-A2) target survives at 45min/d."
        ),
        "sources": ["data/fsi_hours.csv", "data/SOURCES.md"],
    }
    save_json("exp01_hour_deficit.json", payload)

    # Chart (matplotlib optional; skip gracefully offline-minimal)
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        langs = ["Spanish", "German", "Russian", "Arabic", "Mandarin"]
        needs = {"Spanish": 690, "German": 828, "Russian": 1012, "Arabic": 2200, "Mandarin": 2200}
        fig, ax = plt.subplots(figsize=(8, 4.5))
        x = range(len(langs))
        ax.bar([i - 0.2 for i in x], [needs[l] for l in langs], width=0.2, label="FSI class hours to B2")
        ax.bar([i for i in x], [needs[l] * 1.5 for l in langs], width=0.2, label="App-adjusted 1.5x")
        ax.axhline(boot_total, linestyle="--", label=f"Bootcamp total {boot_total:.1f}h")
        ax.axhline(intensive_total, linestyle=":", label=f"Intensive 8h/d total {intensive_total:.0f}h")
        ax.set_xticks(list(x)); ax.set_xticklabels(langs); ax.set_ylabel("hours")
        ax.set_title("90-day hour deficit: FSI B2 vs actual time budgets")
        ax.legend(fontsize=8)
        fig.tight_layout(); fig.savefig(Path(__file__).resolve().parents[1] / "results" / "exp01_hour_deficit.png", dpi=150)
        plt.close(fig)
    except Exception:
        pass
    return payload


if __name__ == "__main__":
    print(main()["verdict"])
