#!/usr/bin/env python3
"""
gen.py — generate the crafted, theme-adaptive README hero + impact SVGs.

Outputs 4 files into ../../img/:
  hero-light.svg  hero-dark.svg  impact-light.svg  impact-dark.svg

The README references them via <picture media="prefers-color-scheme">, so GitHub
shows the right variant in light or dark theme. Edit the DATA below and re-run:

    python3 tools/readme-assets/gen.py

No dependencies — pure stdlib string building.
"""
import html
import os

# ─────────────────────────── content (edit here) ───────────────────────────
NAME_EN = "Pengliang Liu"
NAME_CN = "刘鹏亮"
ROLE_CAPS = "TECHNICAL DIRECTOR / FULL-STACK ARCHITECT · 11Y"
PITCH = "I build medical-AI systems end to end — from algorithms to hardware."
PITCH_CN = "从算法到硬件，独当一面。"
FOCUS = ["medical-AI", "RAG", "multimodal CV", "forecasting"]

IMPACT = [
    ("600G + 15G", "DDoS + CC defended"),
    ("10T / 550G", "zero-downtime migration"),
    ("8×", "growth on one arch"),
    ("−80%", "search latency"),
    ("5M", "vector retrieval"),
]

# ─────────────────────────────── palettes ──────────────────────────────────
THEMES = {
    "dark": dict(
        card2="#111a2e", border="#1f2b45",
        text="#e6f2ff", muted="#9fb2c9", faint="#6b7d94",
        accent="#38bdf8", amber="#f5b451",
    ),
    "light": dict(
        card2="#f8fafc", border="#e2e8f0",
        text="#0f172a", muted="#475569", faint="#64748b",
        accent="#0284c7", amber="#b45309",
    ),
}

SANS = "ui-sans-serif,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def hero_svg(p: dict) -> str:
    """Refined editorial hero: transparent bg, big name, hairline accent rule,
    letter-spaced mono sublabel, one plain positioning line, focus + 中文 tails.
    No card / gradient / chips — restraint is the craft."""
    W, H = 880, 206
    x0 = 10
    focus = "   ·   ".join(FOCUS)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{esc(NAME_EN)} — {esc(ROLE_CAPS)}">
  <text x="{x0}" y="56" font-family="{SANS}" font-size="38" font-weight="700" fill="{p['text']}">{esc(NAME_EN)}</text>
  <text x="{x0+312}" y="56" font-family="{SANS}" font-size="18" fill="{p['muted']}">{esc(NAME_CN)}</text>
  <rect x="{x0+2}" y="74" width="208" height="3" rx="1.5" fill="{p['accent']}"/>
  <text x="{x0}" y="106" font-family="{MONO}" font-size="12.5" letter-spacing="2.4" fill="{p['accent']}">{esc(ROLE_CAPS)}</text>
  <text x="{x0}" y="144" font-family="{SANS}" font-size="16.5" fill="{p['text']}">{esc(PITCH)}</text>
  <text x="{x0}" y="172" font-family="{MONO}" font-size="13" fill="{p['muted']}">{esc(focus)}</text>
  <text x="{x0}" y="194" font-family="{SANS}" font-size="12.5" fill="{p['faint']}">{esc(PITCH_CN)}</text>
</svg>'''


def impact_svg(p: dict) -> str:
    W, H = 880, 96
    pad, gap, n = 6, 8, len(IMPACT)
    cw = (W - 2 * pad - (n - 1) * gap) / n
    cells = []
    for i, (val, cap) in enumerate(IMPACT):
        x = pad + i * (cw + gap)
        cxm = x + cw / 2
        color = p["accent"] if i % 2 == 0 else p["amber"]
        cells.append(
            f'<rect x="{x:.1f}" y="6" width="{cw:.1f}" height="84" rx="13" '
            f'fill="{p["card2"]}" stroke="{p["border"]}"/>'
            f'<text x="{cxm:.1f}" y="46" font-family="{MONO}" font-size="21" '
            f'font-weight="700" fill="{color}" text-anchor="middle">{esc(val)}</text>'
            f'<text x="{cxm:.1f}" y="68" font-family="{SANS}" font-size="10.5" '
            f'fill="{p["muted"]}" text-anchor="middle">{esc(cap)}</text>'
        )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Impact metrics">
  {''.join(cells)}
</svg>'''


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    img = os.path.normpath(os.path.join(here, "..", "..", "img"))
    os.makedirs(img, exist_ok=True)
    for theme, p in THEMES.items():
        for name, svg in (("hero", hero_svg(p)), ("impact", impact_svg(p))):
            path = os.path.join(img, f"{name}-{theme}.svg")
            with open(path, "w", encoding="utf-8") as f:
                f.write(svg)
            print(f"wrote {path}  ({len(svg)} bytes)")


if __name__ == "__main__":
    main()
