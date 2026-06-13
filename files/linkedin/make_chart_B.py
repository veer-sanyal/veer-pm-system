"""Reproducible generator for chart_B_ip_licensing_v2.png (LinkedIn post v5).

Series is India's payments for use of intellectual property (WTO Digitally
Delivered Services dataset), taken from the product repo's site/data.js key
`ipImp` (USD million) -- the same auto-generated, computed-from-source values
the live dashboard uses. 2005: $0.67B -> 2025: $19.8B = 29.4x.

Re-run if site/data.js updates: paste the new `ipImp` array into ip_m below.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

years = [2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,
         2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
ip_m = [671.83,845.95,1159.82,1528.83,1860.07,2438.3,2819.29,3990.06,3903.91,
        4848.71,5009.03,5466.04,6515.41,7905.96,7889.69,7241.11,8631.57,
        10427.79,14349.45,16263.06,19759.13]               # USD million, from data.js ipImp
ip = [v/1000.0 for v in ip_m]                               # USD billion
start, end = ip[0], ip[-1]
mult = end/start
guess10 = start*10                                          # where a hardcoded ~10x sits

PAPER="#f5f0e6"; INK="#1b2440"; INDIGO="#34478f"; GREY="#9a9387"; URLBLUE="#3b5bbf"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":13,"text.color":INK,
    "axes.edgecolor":"#d8d2c4","axes.labelcolor":INK,
    "xtick.color":INK,"ytick.color":INK})

fig, ax = plt.subplots(figsize=(11.2,6.5), dpi=160)
fig.patch.set_facecolor(PAPER); ax.set_facecolor(PAPER)

ax.axhline(guess10, ls=(0,(6,4)), lw=1.6, color="#b9b2a3", zorder=1)
ax.text(2005.2, guess10+0.45, "a hardcoded ~10x guess", color="#8a8273",
        style="italic", fontsize=12.5, va="bottom")

ax.plot(years, ip, color=INDIGO, lw=3.4, solid_capstyle="round", zorder=3)
ax.scatter(years, ip, color=INDIGO, s=22, zorder=4)

ax.annotate("2005: $0.67B", xy=(2005,start), xytext=(2006.2,start+1.5),
    fontsize=12.5, color=GREY, arrowprops=dict(arrowstyle="-", color=GREY, lw=1))
ax.text(2025.25, end-0.2, f"2025: $19.8B\n{mult:.1f}x", color=INDIGO,
        fontweight="bold", fontsize=14, va="center")

fig.text(0.066,0.965,"I compute every figure from source instead of hardcoding it.",
         fontsize=18, fontweight="bold", color=INK, va="top")
fig.text(0.066,0.905,"A typed-in “~10x” would be wrong and frozen. The data says 29.4x.",
         fontsize=15.5, color=INK, va="top")

ax.set_xlabel("Year", fontsize=13)
ax.set_ylabel("Payments for use of intellectual property, USD billion", fontsize=12.5)
ax.set_xlim(2004.3,2028.6); ax.set_ylim(0,21.5)
ax.set_xticks([2006,2008,2010,2012,2014,2016,2018,2020,2022,2024,2026,2028])
ax.grid(axis="y", color="#e4ddcd", lw=1); ax.set_axisbelow(True)
for s in ["top","right"]: ax.spines[s].set_visible(False)

fig.text(0.066,0.035,
    "Source: WTO Digitally Delivered Services dataset, 2005-2025. Every figure computed from the raw data.",
    fontsize=10.5, color=GREY)
fig.text(0.934,0.035,"veer-sanyal.github.io/india-msme-digital-trade-exposure",
    fontsize=10.5, color=URLBLUE, ha="right")

fig.subplots_adjust(left=0.082, right=0.985, top=0.82, bottom=0.165)
out="/sessions/sharp-stoic-wozniak/mnt/veer-pm-project/files/linkedin/chart_B_ip_licensing_v2.png"
fig.savefig(out, facecolor=PAPER)
print("saved", out, "| mult=%.2f"%mult)
