#!/usr/bin/env python3
"""Compose the 22 Nov 2026 world-news poster v4 (1024x1024) for the make.fun entry.

v4 = v2 with two of the strongest text briefs promoted to illustrated cards:
  - "Beijing: Takaichi must retract"   (ASIA-PACIFIC)
  - "Zelensky: 2,700 drones in a week" (EUROPE)
Totals stay at 36 stories and 7 regions; illustrated 13 -> 15, briefs 23 -> 21.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (250, 247, 240)
INK = (24, 24, 26)
NAVY = (18, 30, 56)
RED = (168, 38, 38)
MAGENTA = (229, 0, 125)
GREY = (96, 96, 100)
RULE = (206, 200, 188)
WHITE = (255, 255, 255)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS_R = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
NARROW_B = "/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Bold.ttf"
NARROW_R = "/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Regular.ttf"

_cache = {}


def f(path, size):
    key = (path, size)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(path, size)
    return _cache[key]


REGION_COLOR = {
    "EUROPE": (37, 99, 168),
    "MIDDLE EAST": (176, 42, 42),
    "ASIA-PACIFIC": (186, 128, 16),
    "AMERICAS": (26, 118, 118),
    "AFRICA": (52, 118, 56),
    "OCEANIA": (108, 68, 148),
    "WORLD": (88, 88, 92),
}

# ---------------------------------------------------------------- stories
# (region, headline, detail, illustration slug or None)
ILLUSTRATED = [
    ("WORLD", "COP31 COLLAPSES", "Antalya \u00b7 longest COP ever ends with no deal on fossil fuels", "n22b_illo_v6"),
    ("EUROPE", "KYIV BLOCK DESTROYED", "Dymer \u00b7 11 dead, 14 missing after overnight strike", "n22b_illo_v5"),
    ("AFRICA", "MERKURY SUNK OFF LIBYA", "Benghazi \u00b7 sea drones, Ka-27 destroyed, MV Angara hit", "n22b_illo"),
    ("EUROPE", "SPARTA II ABLAZE", "Gulf of Finland \u00b7 80 drones downed, oil-spill watch", "n22b_illo_v12"),
    ("MIDDLE EAST", "HORMUZ TANKERS BURN", "Two ablaze in a \u201crestricted area\u201d east of the strait", "n22b_illo_v2"),
    ("MIDDLE EAST", "RABIGH REFINERY HIT", "Houthi projectile \u00b7 two drones downed over Riyadh", "n22b_illo_v4"),
    ("AMERICAS", "CHAPO ISIDRO CAUGHT", "Guasave \u00b7 4 soldiers and 7 gunmen dead, roadblocks burned", "n22b_illo_v9"),
    ("EUROPE", "LISBON MARCHES IN RAIN", "CGTP \u00b7 wages, pensions, housing; budget vote Tuesday", "n22b_illo_v11"),
    ("AFRICA", "KHARTOUM DRONE STRIKES", "4 killed \u00b7 UN building damaged, airport targeted", "n22b_illo_v3"),
    ("AFRICA", "BAYELSA BOAT CAPSIZE", "29 mourners dead \u00b7 unseaworthy boat, unapproved jetty", "n22b_illo_v8"),
    ("EUROPE", "ALCARAZ TAKES TURIN", "First ATP Finals title \u00b7 career trophy No. 30", "n22b_illo_v13"),
    ("EUROPE", "MISSILE DEBRIS IN POLAND", "3 sites \u00b7 Kh-101 found; NATO council meets Monday", "n22b_illo_v10"),
    ("WORLD", "AI ROUT WIPES GAINS", "TAIEX \u221217.5% \u00b7 Nasdaq \u221210.4% \u00b7 KOSPI \u22127.9%", "n22b_illo_v7"),
    # promoted from the brief block in v4
    ("ASIA-PACIFIC", "BEIJING: RETRACT OR ELSE", "Takaichi's Taiwan remarks stall China\u2013Japan ties", "n22b_illo_v14"),
    ("EUROPE", "2,700 DRONES IN A WEEK", "Zelensky \u00b7 1,460 glide bombs, 165 missiles", "n22b_illo_v15"),
]

BRIEFS = [
    ("MIDDLE EAST", "Gaza: 3 killed in new strikes", "truce violations now 1,675 dead"),
    ("ASIA-PACIFIC", "Mistral opens APAC HQ", "Singapore base, defence-AI partnership"),
    ("ASIA-PACIFIC", "Fukushima village cut off", "1,000+ isolated by heavy snow"),
    ("ASIA-PACIFIC", "UP draft voter list: 13.58 crore", "Yogi Adityanath's mother cremated"),
    ("WORLD", "Trump posts Xi\u2013Putin handshake", "image from the Apex summit in China"),
    ("EUROPE", "NATO calls emergency council", "North Atlantic Council meets Monday"),
    ("EUROPE", "Zaporizhzhia: 20 glide bombs", "roughly one hour, bridge possibly hit"),
    ("EUROPE", "Krasnodar Rosgvardia HQ hit", "Ukrainian drones, 360 km from front"),
    ("EUROPE", "Sixth weekend of protests", "France, Spain, Italy, Portugal"),
    ("EUROPE", "Rome students clash with police", "outside the Education Ministry"),
    ("AFRICA", "Sudan: executions alleged", "RSF accused in Blue Nile state"),
    ("AFRICA", "Tinubu orders boats for rivers", "cash support for Bayelsa families"),
    ("AFRICA", "Upington taxi-rank protest", "burning tyres; storm warnings issued"),
    ("MIDDLE EAST", "Iran imposes power cuts", "IRGC warns of \u201cenemies\u201d stoking unrest"),
    ("MIDDLE EAST", "Gunboats shell Gaza City coast", "buildings blown up east of Yellow Line"),
    ("AMERICAS", "Sinaloa: 11 dead in clashes", "burnt-out vehicles block highways"),
    ("AMERICAS", "Army to detonate 5 tons", "explosive material in Iowa; families protest"),
    ("AMERICAS", "Flight delays hit US airports", "wide ground stops reported"),
    ("OCEANIA", "ASX set to slide at open", "NZX 50 down 1% in early trade"),
    ("OCEANIA", "PNG name FIFA squad", "series in Brisbane, Australia"),
    ("OCEANIA", "Melbourne International closes", "badminton, 13 nations, final day"),
]

assert len(ILLUSTRATED) == 15, len(ILLUSTRATED)
assert len(BRIEFS) == 21, len(BRIEFS)
TOTAL = len(ILLUSTRATED) + len(BRIEFS)
assert TOTAL == 36, TOTAL

canvas = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(canvas)

M = 14


def fit(text, path, size, maxw, minsize=6):
    s = size
    while s > minsize and d.textlength(text, font=f(path, s)) > maxw:
        s -= 1
    return s


def wrap(text, path, size, maxw):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f(path, size)) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# ---------------------------------------------------------------- top bar
d.rectangle([0, 0, W, 20], fill=NAVY)
d.text((M, 4), f"{TOTAL} STORIES \u00b7 7 REGIONS \u00b7 EVERY ONE DATED SUNDAY 22 NOVEMBER 2026",
       font=f(NARROW_B, 12), fill=(226, 230, 238))
d.text((W - M, 4), "PRESS TIME 23:00 UTC", font=f(NARROW_B, 12), fill=(226, 230, 238), anchor="ra")

# ---------------------------------------------------------------- masthead
d.text((M, 24), "Sunday 22 November 2026", font=f(SERIF_B, 58), fill=INK)
d.text((M + 2, 86), "The world in one day \u2014 every story below happened on this date",
       font=f(SERIF_I, 15), fill=RED)

# ---------------------------------------------------------------- stats bar
STATS = [("36", "STORIES"), ("7", "REGIONS"), ("15", "ILLUSTRATED"),
         ("2,700", "DRONES / WEEK"), ("29", "DEAD, BAYELSA"), ("0", "COP31 DEAL")]
sy0, sy1 = 102, 140
d.rectangle([M, sy0, W - M, sy1], fill=(255, 255, 255), outline=RULE, width=1)
bw = (W - 2 * M) / len(STATS)
for i, (num, lab) in enumerate(STATS):
    x = M + i * bw
    if i:
        d.line([x, sy0 + 4, x, sy1 - 4], fill=RULE, width=1)
    d.text((x + bw / 2, sy0 + 4), num, font=f(SERIF_B, 22), fill=NAVY, anchor="ma")
    d.text((x + bw / 2, sy1 - 15), lab, font=f(NARROW_B, 9), fill=GREY, anchor="ma")

# ---------------------------------------------------------------- region bar
ry0, ry1 = 144, 164
d.rectangle([M, ry0, W - M, ry1], fill=(238, 234, 224))
counts = {}
for r, _, _, _ in ILLUSTRATED:
    counts[r] = counts.get(r, 0) + 1
for r, _, _ in BRIEFS:
    counts[r] = counts.get(r, 0) + 1
order = ["EUROPE", "MIDDLE EAST", "ASIA-PACIFIC", "AMERICAS", "AFRICA", "OCEANIA", "WORLD"]
x = M + 6
for r in order:
    label = f"{r} {counts.get(r, 0)}"
    tw = d.textlength(label, font=f(NARROW_B, 11))
    d.rectangle([x, ry0 + 4, x + 9, ry1 - 4], fill=REGION_COLOR[r])
    d.text((x + 13, ry0 + 4), label, font=f(NARROW_B, 11), fill=INK)
    x += 13 + tw + 14

# ---------------------------------------------------------------- date check
dy0, dy1 = 168, 182
d.rectangle([M, dy0, W - M, dy1], fill=RED)
d.text((M + 6, dy0 + 3), "DATE CHECK", font=f(NARROW_B, 10), fill=WHITE)
d.text((M + 78, dy0 + 3), "every item is dated Sunday 22 November 2026 (UTC) \u2014 nothing carried over from another day",
       font=f(NARROW_R, 10), fill=(255, 232, 232))

# ---------------------------------------------------------------- row 1: 3 large
R1Y0, R1Y1 = 188, 398
GAP = 10
cw1 = (W - 2 * M - 2 * GAP) // 3
ILLO1 = 138


def card(x, y, cw, ch, region, head, detail, slug, illo_h, hsize, dsize, num):
    d.rectangle([x, y, x + cw, y + ch], fill=WHITE, outline=RULE, width=1)
    d.rectangle([x, y, x + cw, y + 4], fill=REGION_COLOR[region])
    if slug:
        illo = Image.open(f"/workspace/images/{slug}/n22b_illo.png").convert("RGB")
        illo = illo.resize((cw - 2, illo_h), Image.LANCZOS)
        canvas.paste(illo, (x + 1, y + 5))
        d.rectangle([x + 1, y + 5, x + cw - 1, y + 5 + illo_h], outline=RULE, width=1)
        ty = y + 5 + illo_h + 5
    else:
        ty = y + 8
    d.text((x + 6, ty), f"{num:02d}", font=f(NARROW_B, 10), fill=REGION_COLOR[region])
    d.text((x + 24, ty), region, font=f(NARROW_B, 9), fill=GREY)
    ty += 12
    hs = fit(head, SERIF_B, hsize, cw - 12)
    hl = wrap(head, SERIF_B, hs, cw - 12)
    for ln in hl[:2]:
        d.text((x + 6, ty), ln, font=f(SERIF_B, hs), fill=INK)
        ty += hs + 1
    ds = dsize
    dl = wrap(detail, NARROW_R, ds, cw - 12)
    for ln in dl[:2]:
        d.text((x + 6, ty), ln, font=f(NARROW_R, ds), fill=GREY)
        ty += ds + 2


for i, (region, head, detail, slug) in enumerate(ILLUSTRATED[:3]):
    x = M + i * (cw1 + GAP)
    card(x, R1Y0, cw1, R1Y1 - R1Y0, region, head, detail, slug, ILLO1, 24, 13, i + 1)

# ---------------------------------------------------------------- rows 2-3: 6 each
GAP2 = 7
cw2 = (W - 2 * M - 5 * GAP2) // 6
ILLO2 = 58
for row, (y0, y1) in enumerate([(404, 544), (550, 690)]):
    for c in range(6):
        idx = 3 + row * 6 + c
        if idx >= len(ILLUSTRATED):
            break
        region, head, detail, slug = ILLUSTRATED[idx]
        x = M + c * (cw2 + GAP2)
        card(x, y0, cw2, y1 - y0, region, head, detail, slug, ILLO2, 13, 9, idx + 1)

# ---------------------------------------------------------------- bottom: map + briefs
BY0, BY1 = 696, 950
MAPW = 214
d.rectangle([M, BY0, M + MAPW, BY1], fill=WHITE, outline=RULE, width=1)
d.rectangle([M, BY0, M + MAPW, BY0 + 16], fill=NAVY)
d.text((M + 6, BY0 + 3), "WHERE IT HAPPENED", font=f(NARROW_B, 10), fill=WHITE)

CONTINENTS = [
    [(0.10, 0.18), (0.22, 0.12), (0.30, 0.16), (0.32, 0.26), (0.28, 0.34), (0.24, 0.40), (0.20, 0.36), (0.16, 0.30), (0.10, 0.26)],
    [(0.24, 0.40), (0.28, 0.44), (0.30, 0.48), (0.26, 0.46), (0.23, 0.42)],
    [(0.28, 0.50), (0.34, 0.48), (0.37, 0.56), (0.35, 0.68), (0.31, 0.80), (0.28, 0.72), (0.27, 0.60)],
    [(0.46, 0.16), (0.54, 0.14), (0.57, 0.20), (0.55, 0.28), (0.48, 0.30), (0.45, 0.24)],
    [(0.47, 0.34), (0.56, 0.32), (0.60, 0.40), (0.58, 0.52), (0.54, 0.64), (0.50, 0.58), (0.47, 0.46)],
    [(0.57, 0.12), (0.72, 0.10), (0.84, 0.16), (0.86, 0.26), (0.78, 0.32), (0.70, 0.34), (0.62, 0.30), (0.57, 0.22)],
    [(0.68, 0.34), (0.73, 0.34), (0.72, 0.44), (0.69, 0.40)],
    [(0.76, 0.36), (0.84, 0.38), (0.86, 0.46), (0.80, 0.48), (0.76, 0.42)],
    [(0.80, 0.62), (0.90, 0.60), (0.93, 0.70), (0.88, 0.76), (0.81, 0.72)],
    [(0.94, 0.76), (0.96, 0.78), (0.95, 0.84), (0.93, 0.80)],
]


def inside(px, py, poly):
    n, hit = len(poly), False
    j = n - 1
    for i in range(n):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if (yi > py) != (yj > py):
            if px < (xj - xi) * (py - yi) / (yj - yi) + xi:
                hit = not hit
        j = i
    return hit


mx0, my0 = M + 8, BY0 + 24
mw, mh = MAPW - 16, BY1 - BY0 - 34
step = 4
for gy in range(0, int(mh), step):
    for gx in range(0, int(mw), step):
        nx, ny = gx / mw, gy / mh
        if any(inside(nx, ny, p) for p in CONTINENTS):
            d.ellipse([mx0 + gx, my0 + gy, mx0 + gx + 2, my0 + gy + 2], fill=(196, 200, 208))

MARKERS = [
    (0.50, 0.24, 1), (0.53, 0.22, 2), (0.55, 0.40, 3), (0.55, 0.17, 4),
    (0.63, 0.33, 5), (0.60, 0.35, 6), (0.20, 0.34, 7), (0.46, 0.25, 8),
    (0.55, 0.44, 9), (0.50, 0.50, 10), (0.50, 0.22, 11), (0.52, 0.20, 12),
    (0.80, 0.20, 13), (0.79, 0.26, 14), (0.54, 0.19, 15),
]
for nx, ny, num in MARKERS:
    px, py = mx0 + nx * mw, my0 + ny * mh
    d.ellipse([px - 6, py - 6, px + 6, py + 6], fill=RED, outline=WHITE, width=1)
    d.text((px, py), str(num), font=f(NARROW_B, 8), fill=WHITE, anchor="mm")

d.text((M + 6, BY1 - 12), "15 illustrated stories \u00b7 6 continents", font=f(NARROW_R, 8), fill=GREY)

# briefs: 3 columns of 7
BX0 = M + MAPW + 8
BW = W - M - BX0
GAP3 = 8
colw = (BW - 2 * GAP3) // 3
per = [7, 7, 7]
d.rectangle([BX0, BY0, W - M, BY0 + 16], fill=NAVY)
d.text((BX0 + 6, BY0 + 3), f"ALSO ON SUNDAY \u00b7 {len(BRIEFS)} MORE STORIES", font=f(NARROW_B, 10), fill=WHITE)

n = 0
for ci, cnt in enumerate(per):
    cx = BX0 + ci * (colw + GAP3)
    cy = BY0 + 22
    for _ in range(cnt):
        if n >= len(BRIEFS):
            break
        region, head, detail = BRIEFS[n]
        n += 1
        d.rectangle([cx, cy + 2, cx + 3, cy + 9], fill=REGION_COLOR[region])
        d.text((cx + 7, cy), f"{15 + n:02d}", font=f(NARROW_B, 8), fill=REGION_COLOR[region])
        hs = fit(head, NARROW_B, 10, colw - 26)
        d.text((cx + 20, cy), head, font=f(NARROW_B, hs), fill=INK)
        dl = wrap(detail, NARROW_R, 9, colw - 26)
        d.text((cx + 20, cy + 11), dl[0] if dl else "", font=f(NARROW_R, 9), fill=GREY)
        cy += 27

# ---------------------------------------------------------------- footer
d.rectangle([0, 958, W, H], fill=MAGENTA)
d.text((M, 972), "make.fun", font=f(SANS_B, 26), fill=WHITE)
d.text((M + 128, 980), "news-image-20261122", font=f(NARROW_B, 15), fill=(255, 220, 240))
d.text((W - M, 976), "SUNDAY 22 NOVEMBER 2026", font=f(NARROW_B, 13), fill=WHITE, anchor="ra")
d.text((W - M, 994), f"{TOTAL} stories \u00b7 7 regions \u00b7 15 illustrated", font=f(NARROW_R, 11), fill=(255, 220, 240), anchor="ra")

canvas.save("/workspace/work22/repo/entry.png", "PNG", optimize=True)
print("saved", canvas.size)
