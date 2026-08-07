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
ROLE = "Technical Director · Full-Stack Architect · 11y"
PITCH1 = "Architect who ships AI under real fire —"
PITCH2 = "RAG & multimodal systems on distributed, attack-hardened infra."
PITCH_CN = "从算法到硬件，独当一面。"
CHIPS = ["medical-AI", "RAG", "multimodal CV", "forecasting", "software–hardware"]

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
        card="#0e1524", card2="#111a2e", border="#1f2b45",
        text="#e6f2ff", muted="#9fb2c9", accent="#38bdf8", amber="#f5b451",
        chip_bg="#12203a", chip_border="#274063", glow="#38bdf8",
    ),
    "light": dict(
        card="#ffffff", card2="#f8fafc", border="#e2e8f0",
        text="#0f172a", muted="#475569", accent="#0284c7", amber="#b45309",
        chip_bg="#f1f5f9", chip_border="#cbd5e1", glow="#0284c7",
    ),
}

SANS = "ui-sans-serif,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def hero_svg(p: dict) -> str:
    W, H = 880, 244
    x0 = 34  # left content edge (after accent bar)
    chip_h, chip_y = 24, 200
    # lay out chips left-to-right (monospace ~7.35px/char at 12.5px)
    chips, cx = [], x0
    for c in CHIPS:
        w = int(len(c) * 7.35) + 24
        chips.append((cx, w, c))
        cx += w + 9
    chip_rects = "".join(
        f'<rect x="{x}" y="{chip_y}" width="{w}" height="{chip_h}" rx="12" '
        f'fill="{p["chip_bg"]}" stroke="{p["chip_border"]}"/>'
        f'<text x="{x + w/2:.0f}" y="{chip_y + 16}" font-family="{MONO}" '
        f'font-size="12.5" fill="{p["accent"]}" text-anchor="middle">{esc(c)}</text>'
        for x, w, c in chips
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{esc(NAME_EN)} — {esc(ROLE)}">
  <defs>
    <linearGradient id="acc" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{p['accent']}"/><stop offset="1" stop-color="#22d3ee"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.92" cy="0.08" r="0.7">
      <stop offset="0" stop-color="{p['glow']}" stop-opacity="0.12"/>
      <stop offset="1" stop-color="{p['glow']}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="18" fill="{p['card']}" stroke="{p['border']}" stroke-width="1.5"/>
  <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="18" fill="url(#glow)"/>
  <rect x="16" y="22" width="5" height="200" rx="2.5" fill="url(#acc)"/>
  <text x="{x0}" y="60" font-family="{SANS}" font-size="33" font-weight="700" fill="{p['text']}">{esc(NAME_EN)}</text>
  <text x="{x0+232}" y="60" font-family="{SANS}" font-size="18" fill="{p['muted']}">{esc(NAME_CN)}</text>
  <text x="{x0}" y="90" font-family="{MONO}" font-size="14.5" fill="{p['accent']}">{esc(ROLE)}</text>
  <text x="{x0}" y="128" font-family="{SANS}" font-size="17" font-weight="600" fill="{p['text']}">{esc(PITCH1)}</text>
  <text x="{x0}" y="152" font-family="{SANS}" font-size="15" fill="{p['text']}">{esc(PITCH2)}</text>
  <text x="{x0}" y="178" font-family="{SANS}" font-size="13.5" fill="{p['muted']}">{esc(PITCH_CN)}</text>
  {chip_rects}
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
