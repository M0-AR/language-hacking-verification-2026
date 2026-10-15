"""Build docs/demo.gif — deterministic 90-day hour-deficit animation.

Verified inputs only: FSI class hours (Spanish 690, German 828, Russian 1012,
Arabic/Mandarin 2200), bootcamp budget 67.5h, intensive 720h.
Output: docs/demo.gif (<=3MB target per README-GIF best practice: short, ~6s, 10fps, 128 colors).
Run: python scripts/build_demo_gif.py  (or: python -m scripts.build_demo_gif)
"""
from __future__ import annotations
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
import io

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "demo.gif"
OUT.parent.mkdir(parents=True, exist_ok=True)

LANGS = ["Spanish", "German", "Russian", "Arabic", "Mandarin"]
NEEDS = [690, 828, 1012, 2200, 2200]
BOOT = 67.5
INTENSIVE = 720.0
FRAMES = 30  # 3s at 10fps


def frame(i: int) -> Image.Image:
    frac = (i + 1) / FRAMES
    fig, ax = plt.subplots(figsize=(8, 4.2))
    shown = [n * frac for n in NEEDS]
    bars = ax.bar(LANGS, shown, color="#2563eb", label="FSI class hours to B2")
    ax.axhline(BOOT, color="#dc2626", linestyle="--", linewidth=2, label=f"45 min/day total {BOOT:.1f}h")
    ax.axhline(INTENSIVE, color="#059669", linestyle=":", linewidth=2, label=f"8 h/day total {INTENSIVE:.0f}h")
    ax.set_ylim(0, 2400)
    ax.set_ylabel("hours")
    ax.set_title(f"90-day hour deficit — progress {frac:3.0%}  (15-min talk: plausible / B2 at 45min/day: refuted)")
    ax.legend(fontsize=8, loc="upper left")
    for b, n in zip(bars, NEEDS):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 40, f"{n}h", ha="center", fontsize=9, fontweight="bold")
    fig.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=100)
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf).convert("P", palette=Image.ADAPTIVE, colors=128)


def main() -> Path:
    imgs = [frame(i) for i in range(FRAMES)]
    imgs[0].save(OUT, save_all=True, append_images=imgs[1:], duration=100, loop=0, optimize=True)
    size_kb = OUT.stat().st_size // 1024
    print(f"wrote {OUT} ({size_kb} KB, {FRAMES} frames)")
    assert size_kb < 3072, f"GIF too big: {size_kb} KB (keep <=3MB per best practice)"
    return OUT


if __name__ == "__main__":
    main()
