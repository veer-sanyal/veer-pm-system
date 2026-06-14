"""Reproducible generator for chart_A_consulting.png (LinkedIn post v7 lead image).

Restyled 2026-06-14 to match the live dashboard's visual language:
- Fonts: IBM Plex Serif (title), IBM Plex Sans (body/axes), IBM Plex Mono (subtitle/source)
- Palette pulled from the dashboard's own tokens / live Plotly traces:
  paper #FBFAF7, ink #1A1D24, grid #ECEAE3, consulting line #2E6FB0 (indigo-500),
  remainder line #858B96 (ink-400). Line widths mirror the live chart (2.6 / 2.0, scaled up for a poster).

Data is the dashboard's "What actually drove the surge" chart: the two Mode 1 export
sub-codes of EBOPS SJXSJ34 (other business services), USD billion, 2005-2022, read
directly off the live Plotly traces (same computed-from-source values the site uses).
Consulting: $6.83B (2005) -> $91.86B (2022) = 13.4x. Remainder: ~flat.

IBM Plex is not bundled with matplotlib. To make it available locally without root:
    cd /tmp && apt-get download fonts-ibm-plex && dpkg-deb -x fonts-ibm-plex_*.deb /tmp/plex
The font search below checks that location plus standard font dirs, and falls back to
matplotlib defaults if IBM Plex is missing (so the script still runs, just off-brand).
"""
import os, glob
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# --- locate IBM Plex faces (graceful fallback) ---
SEARCH = ["/tmp/plex/usr/share/fonts/truetype/ibm-plex",
          "/usr/share/fonts/truetype/ibm-plex",
          os.path.expanduser("~/.fonts"), os.path.expanduser("~/.local/share/fonts")]
def face(stem, fallback_family):
    for d in SEARCH:
        hits = glob.glob(os.path.join(d, stem + ".ttf"))
        if hits:
            fm.fontManager.addfont(hits[0])
            return fm.FontProperties(fname=hits[0])
    return fm.FontProperties(family=fallback_family)

serif_sb = face("IBMPlexSerif-SemiBold", "serif")     # title
sans_reg = face("IBMPlexSans-Regular",  "sans-serif") # axes / labels
sans_sb  = face("IBMPlexSans-SemiBold", "sans-serif") # emphasis labels
mono_reg = face("IBMPlexMono-Regular",  "monospace")  # subtitle / source
try:
    plt.rcParams["font.family"] = sans_reg.get_name()
except Exception:
    pass

# --- dashboard palette ---
PAPER="#FBFAF7"; INK="#1A1D24"; INK500="#5E646F"; INK400="#858B96"
GRID="#ECEAE3"; INDIGO="#2E6FB0"; REMAIN="#858B96"

# --- data (USD billion), read off the live dashboard Plotly traces ---
years = list(range(2005, 2023))
consulting = [6.83173,10.16609,12.74933,16.33565,15.77131,18.25927,20.20304,25.67487,
              26.2518,27.13475,29.08125,30.52841,33.13686,36.61942,42.58266,56.63808,
              68.4342,91.86231]
remainder  = [7.33507,9.07506,10.32011,11.10007,5.50873,8.29042,9.64259,10.73808,
              9.74638,10.0891,9.36229,10.97456,11.70556,11.28993,11.82686,13.33943,
              14.61521,16.48685]
mult = consulting[-1]/consulting[0]   # ~13.4x

fig, ax = plt.subplots(figsize=(12.6, 7.1), dpi=160)
fig.patch.set_facecolor(PAPER); ax.set_facecolor(PAPER)

ax.plot(years, remainder, color=REMAIN, lw=2.4, marker="o", ms=4.5,
        solid_capstyle="round", zorder=2)
ax.plot(years, consulting, color=INDIGO, lw=3.4, marker="o", ms=5,
        solid_capstyle="round", zorder=3)

# end-of-line labels (carry the $ payload)
ax.text(2022.35, consulting[-1], "Consulting & professional\nservices exports: $92B",
        color=INDIGO, fontproperties=sans_sb, fontsize=15, va="center")
ax.text(2022.35, remainder[-1]-0.5, "Everything else in\n“other business services”: $16B",
        color=INK400, fontproperties=sans_reg, fontsize=13.5, va="center")

# title (IBM Plex Serif, like the dashboard headings) + mono subtitle
fig.text(0.055, 0.965, "India’s consulting exports grew 13x since 2005.",
         fontproperties=serif_sb, fontsize=22, color=INK, va="top")
fig.text(0.055, 0.905, "The rest of “other business services” barely moved.",
         fontproperties=serif_sb, fontsize=22, color=INK, va="top")
fig.text(0.056, 0.845, "India  ·  cross-border (Mode 1) exports  ·  USD billion  ·  2005–2022",
         fontproperties=mono_reg, fontsize=11.5, color=INK500, va="top")

ax.set_xlabel("Year", fontproperties=sans_reg, fontsize=13, color=INK500)
ax.set_ylabel("Cross-border services exports, USD billion",
              fontproperties=sans_reg, fontsize=12.5, color=INK500)
ax.set_xlim(2004.2, 2028.8); ax.set_ylim(0, 100)
ax.set_xticks([2005, 2010, 2015, 2020])
ax.set_yticks([0, 20, 40, 60, 80, 100])
for lab in ax.get_xticklabels()+ax.get_yticklabels():
    lab.set_fontproperties(sans_reg); lab.set_color(INK500)
ax.grid(axis="y", color=GRID, lw=1.1); ax.set_axisbelow(True)
ax.tick_params(length=0)
for s in ["top","right"]: ax.spines[s].set_visible(False)
for s in ["left","bottom"]: ax.spines[s].set_color(GRID)

fig.text(0.056, 0.035,
         "Source: WTO TiSMoS, 2005–2022. Every figure computed from the raw data.",
         fontproperties=mono_reg, fontsize=10.5, color=INK400)
fig.text(0.944, 0.035, "veer-sanyal.github.io/india-msme-digital-trade-exposure",
         fontproperties=mono_reg, fontsize=10.5, color=INDIGO, ha="right")

fig.subplots_adjust(left=0.075, right=0.985, top=0.80, bottom=0.135)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chart_A_consulting.png")
fig.savefig(out, facecolor=PAPER)
print("saved", out, "| mult=%.2fx" % mult)
