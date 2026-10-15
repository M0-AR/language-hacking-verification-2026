"""EXP02 — Zipf coverage: do 500/1000 words really cover ~80%?

Verified anchors: commonwords.app + thelernen.org => top-1000 ~= 80-85% everyday speech tokens.
ActualFluency/Benny => 500 words ~= 80% newspaper (keywords caveat: remaining 20% are keywords).
Model: Zipf f(r) = C / r^s, s=1.0, vocab N=20000. Coverage(k) = H(k,s)/H(N,s).
This reproduces the *shape* of the claim from public parameters; it does not invent a corpus.
Falsifiable: if s in [0.9,1.1], coverage(1000) stays 68-86% => claim holds for tokens, fails for keywords.
"""
from __future__ import annotations
from pathlib import Path
from .utils import save_json


def harmonic_coverage(k: int, N: int, s: float) -> float:
    num = sum(1.0 / (r ** s) for r in range(1, k + 1))
    den = sum(1.0 / (r ** s) for r in range(1, N + 1))
    return num / den


def rank_for_coverage(target: float, N: int, s: float) -> int:
    den = sum(1.0 / (r ** s) for r in range(1, N + 1))
    acc = 0.0
    for r in range(1, N + 1):
        acc += (1.0 / (r ** s)) / den
        if acc >= target:
            return r
    return N


def main() -> dict:
    N = 20000
    out = {}
    for s in [0.9, 1.0, 1.1]:
        out[f"s={s}"] = {
            "cov_500": round(100 * harmonic_coverage(500, N, s), 1),
            "cov_1000": round(100 * harmonic_coverage(1000, N, s), 1),
            "cov_2000": round(100 * harmonic_coverage(2000, N, s), 1),
            "rank_80pct": rank_for_coverage(0.80, N, s),
            "rank_85pct": rank_for_coverage(0.85, N, s),
            "rank_90pct": rank_for_coverage(0.90, N, s),
        }
    payload = {
        "experiment": "exp02_zipf_coverage",
        "N": N,
        "results": out,
        "verdict": (
            f"At s=1.0: top-500 covers {out['s=1.0']['cov_500']}%, "
            f"top-1000 covers {out['s=1.0']['cov_1000']}% of tokens; "
            f"80% needs rank {out['s=1.0']['rank_80pct']}. "
            f"At s=1.1: top-1000 covers {out['s=1.1']['cov_1000']}%, 80% needs rank {out['s=1.1']['rank_80pct']}. "
            "BOUNDARY-CONDITIONAL: the 80-85% claim holds only for steep distributions (s~=1.1, "
            "spoken/lemmatized word-families); at canonical written s=1.0 it overstates by ~9-14pp. "
            "REFUTED as comprehension claim either way: the uncovered tail holds content keywords, "
            "so 500 words != 80% understanding. This is the hidden token-vs-keyword gap."
        ),
        "sources": ["commonwords.app", "thelernen.org 1000-word Spanish list", "data/SOURCES.md"],
    }
    save_json("exp02_zipf_coverage.json", payload)
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        ks = [100, 300, 500, 1000, 2000, 5000]
        for s in [0.9, 1.0, 1.1]:
            ys = [100 * harmonic_coverage(k, N, s) for k in ks]
            plt.plot(ks, ys, marker="o", label=f"s={s}")
        plt.xscale("log"); plt.xlabel("vocab rank k (log)"); plt.ylabel("token coverage %")
        plt.title("Zipf coverage: why 1000 words ≈ 80% of tokens, not of meaning")
        plt.axhline(80, linestyle="--"); plt.legend(); plt.tight_layout()
        plt.savefig(Path(__file__).resolve().parents[1] / "results" / "exp02_zipf.png", dpi=150)
        plt.close()
    except Exception:
        pass
    return payload


if __name__ == "__main__":
    print(main()["verdict"])
