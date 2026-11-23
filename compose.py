#!/usr/bin/env python3
"""Compose the 22 Nov 2026 world-news poster v3 (1024x1024) for the make.fun entry.

v3 is a typography rebuild of v2. v2 packed 36 stories into 9-10 px type on grey.
v3 keeps all 36 stories but spends the space on legibility: the dot-matrix map, the
region bar and the per-region counts are gone, and every text size goes up:

    card headline   24 -> 30 px      card detail   14 -> 16 px
    brief headline  10 -> 16 px      brief detail   9 -> 13 px
    masthead        58 -> 66 px      stats         22 -> 28 px

Text is near-black (14,14,16) on white cards and (52,52,58) for detail, so contrast
is ~15:1 and ~9:1 instead of grey-on-cream. The layout is computed from named
constants and asserted at the end, so nothing can run under the footer.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (252, 250, 245)
CARD = (255, 255, 255)
INK = (14, 14, 16)
DETAIL = (38, 38, 44)
NAVY = (16, 28, 54)
RED = (170, 30, 30)
MAGENTA = (229, 0, 125)
RULE = (198, 194, 184)
WHITE = (255, 255, 255)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
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
    "EUROPE": (24, 78, 150),
    "MIDDLE EAST": (162, 30, 30),
    "ASIA-PACIFIC": (158, 104, 6),
    "AMERICAS": (14, 98, 98),
    "AFRICA": (34, 98, 40),
    "OCEANIA": (90, 52, 132),
    "WORLD": (66, 66, 72),
}

# ---------------------------------------------------------------- stories
ILLUSTRATED = [
    ("WORLD", "COP31 COLLAPSES", "Antalya \u00b7 longest COP ever ends with no deal on fossil fuels", "n22b_illo_v6"),
    ("EUROPE", "KYIV BLOCK DESTROYED", "Dymer \u00b7 11 dead, 14 missing after an overnight strike", "n22b_illo_v5"),
    ("MIDDLE EAST", "HORMUZ TANKERS BURN", "Two ablaze in a \u201crestricted area\u201d east of the strait", "n22b_illo_v2"),
    ("AMERICAS", "CHAPO ISIDRO CAUGHT", "Guasave \u00b7 4 soldiers and 7 gunmen dead, roadblocks burned", "n22b_illo_v9"),
    ("AFRICA", "BAYELSA BOAT CAPSIZE", "29 mourners dead \u00b7 unseaworthy boat, unapproved jetty", "n22b_illo_v8"),
    ("WORLD", "AI ROUT WIPES GAINS", "TAIEX \u221217.5% \u00b7 Nasdaq \u221210.4% \u00b7 KOSPI \u22127.9%", "n22b_illo_v7"),
]

BRIEFS = [
    ("AFRICA", "Corvette Merkury sunk off Libya", "Benghazi \u00b7 sea drones, Ka-27 destroyed"),
    ("EUROPE", "Sparta II ablaze in the Baltic", "Gulf of Finland \u00b7 80 drones downed"),
    ("MIDDLE EAST", "Rabigh refinery hit", "Houthi projectile \u00b7 drones downed over Riyadh"),
    ("EUROPE", "Lisbon marches in the rain", "CGTP \u00b7 wages, pensions, housing"),
    ("AFRICA", "Khartoum drone strikes", "4 killed \u00b7 UN building damaged"),
    ("EUROPE", "Alcaraz takes Turin", "First ATP Finals title, trophy No. 30"),
    ("EUROPE", "Missile debris in Poland", "3 sites \u00b7 a Kh-101 found"),
    ("MIDDLE EAST", "Gaza: 3 killed in new strikes", "truce violations now 1,675 dead"),
    ("ASIA-PACIFIC", "Beijing: Takaichi must retract", "Taiwan remarks stall China\u2013Japan ties"),
    ("ASIA-PACIFIC", "Mistral opens APAC HQ", "Singapore base, defence-AI partnership"),
    ("ASIA-PACIFIC", "Fukushima village cut off", "1,000+ isolated by heavy snow"),
    ("ASIA-PACIFIC", "UP draft voter list: 13.58 crore", "Yogi Adityanath's mother cremated"),
    ("WORLD", "Trump posts Xi\u2013Putin handshake", "image from the Apex summit in China"),
    ("EUROPE", "NATO calls emergency council", "North Atlantic Council meets Monday"),
    ("EUROPE", "Zelensky: 2,700 drones in a week", "1,460 glide bombs, 165 missiles"),
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
    ("AMERICAS", "Flight delays hit US airports", "widespread ground stops reported"),
    ("OCEANIA", "ASX set to slide at open", "NZX 50 down 1% in early trade"),
    ("OCEANIA", "PNG name FIFA squad", "series in Brisbane, Australia"),
    ("OCEANIA", "Melbourne International closes", "badminton, 13 nations, final day"),
]

assert len(ILLUSTRATED) == 6 and len(BRIEFS) == 30
TOTAL = len(ILLUSTRATED) + len(BRIEFS)

canvas = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(canvas)

M = 16


def fit(text, path, size, maxw, minsize=7):
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


# ---------------------------------------------------------------- geometry
FOOTER_Y = 958
TOP_H = 26
MAST_Y, MAST_SZ = 30, 66
SUB_Y, SUB_SZ = 106, 19
STAT_Y0, STAT_Y1 = 134, 184
DATE_Y0, DATE_Y1 = 190, 210
CARDS_Y0 = 218
CH, ILLO_H, CARD_GAP = 180, 66, 10
BRIEF_HDR_H = 24
BRIEF_ROWH = 31
BRIEF_PER_COL = 10
BRIEF_COLS = 3

BRIEFS_Y0 = CARDS_Y0 + 2 * CH + CARD_GAP + 20
BRIEF_ROWS_Y0 = BRIEFS_Y0 + BRIEF_HDR_H + 6
last_row_cy = BRIEF_ROWS_Y0 + (BRIEF_PER_COL - 1) * BRIEF_ROWH
last_text_bottom = last_row_cy + 16 + 14
assert last_text_bottom <= FOOTER_Y - 6, f"briefs overflow: {last_text_bottom} > {FOOTER_Y - 6}"

# ---------------------------------------------------------------- top bar
d.rectangle([0, 0, W, TOP_H], fill=NAVY)
d.text((M, 6), f"{TOTAL} STORIES \u00b7 7 REGIONS \u00b7 ALL DATED SUNDAY 22 NOVEMBER 2026",
       font=f(NARROW_B, 15), fill=(234, 238, 246))
d.text((W - M, 6), "PRESS TIME 23:00 UTC", font=f(NARROW_B, 15), fill=(234, 238, 246), anchor="ra")

# ---------------------------------------------------------------- masthead
d.text((M, MAST_Y), "Sunday 22 November 2026", font=f(SERIF_B, MAST_SZ), fill=INK)
d.text((M + 2, SUB_Y), "The world in one day \u2014 every story below happened on this date",
       font=f(SERIF_I, SUB_SZ), fill=RED)

# ---------------------------------------------------------------- stats bar
STATS = [("36", "STORIES"), ("7", "REGIONS"), ("2,700", "DRONES / WEEK"),
         ("29", "DEAD, BAYELSA"), ("\u221217.5%", "TAIEX"), ("0", "COP31 DEAL")]
d.rectangle([M, STAT_Y0, W - M, STAT_Y1], fill=CARD, outline=RULE, width=1)
bw = (W - 2 * M) / len(STATS)
for i, (num, lab) in enumerate(STATS):
    x = M + i * bw
    if i:
        d.line([x, STAT_Y0 + 6, x, STAT_Y1 - 6], fill=RULE, width=1)
    d.text((x + bw / 2, STAT_Y0 + 5), num, font=f(SERIF_B, 28), fill=NAVY, anchor="ma")
    d.text((x + bw / 2, STAT_Y1 - 22), lab, font=f(NARROW_B, 12), fill=DETAIL, anchor="ma")

# ---------------------------------------------------------------- date check
d.rectangle([M, DATE_Y0, W - M, DATE_Y1], fill=RED)
d.text((M + 8, DATE_Y0 + 4), "DATE CHECK", font=f(NARROW_B, 13), fill=WHITE)
d.text((M + 104, DATE_Y0 + 4), "every item is dated Sunday 22 November 2026 (UTC) \u2014 nothing carried over from another day",
       font=f(NARROW_R, 13), fill=(255, 238, 238))

# ---------------------------------------------------------------- illustrated cards
GAP = 12
cw = (W - 2 * M - 2 * GAP) // 3


def card(x, y, region, head, detail, slug, num):
    d.rectangle([x, y, x + cw, y + CH], fill=CARD, outline=RULE, width=1)
    d.rectangle([x, y, x + cw, y + 5], fill=REGION_COLOR[region])
    illo = Image.open(f"/workspace/images/{slug}/n22b_illo.png").convert("RGB")
    illo = illo.resize((cw - 2, ILLO_H), Image.LANCZOS)
    canvas.paste(illo, (x + 1, y + 6))
    d.rectangle([x + 1, y + 6, x + cw - 1, y + 6 + ILLO_H], outline=RULE, width=1)

    ty = y + 6 + ILLO_H + 6
    d.rectangle([x + 7, ty, x + 29, ty + 15], fill=REGION_COLOR[region])
    d.text((x + 18, ty + 1), f"{num:02d}", font=f(NARROW_B, 12), fill=WHITE, anchor="ma")
    d.text((x + 35, ty + 1), region, font=f(NARROW_B, 12), fill=REGION_COLOR[region])
    ty += 19

    hs = fit(head, SERIF_B, 30, cw - 14)
    for ln in wrap(head, SERIF_B, hs, cw - 14)[:2]:
        d.text((x + 7, ty), ln, font=f(SERIF_B, hs), fill=INK)
        ty += hs + 1
    ty += 3
    for ln in wrap(detail, SANS_R, 17, cw - 14)[:2]:
        d.text((x + 7, ty), ln, font=f(SANS_R, 17), fill=DETAIL)
        ty += 20


for i, (region, head, detail, slug) in enumerate(ILLUSTRATED):
    row, col = divmod(i, 3)
    card(M + col * (cw + GAP), CARDS_Y0 + row * (CH + CARD_GAP), region, head, detail, slug, i + 1)

# ---------------------------------------------------------------- briefs
d.rectangle([M, BRIEFS_Y0, W - M, BRIEFS_Y0 + BRIEF_HDR_H], fill=NAVY)
d.text((M + 8, BRIEFS_Y0 + 4), f"ALSO ON SUNDAY \u00b7 {len(BRIEFS)} MORE STORIES",
       font=f(NARROW_B, 15), fill=WHITE)
d.text((W - M - 8, BRIEFS_Y0 + 5), "EUROPE \u00b7 MIDDLE EAST \u00b7 ASIA-PACIFIC \u00b7 AMERICAS \u00b7 AFRICA \u00b7 OCEANIA",
       font=f(NARROW_R, 13), fill=(208, 216, 230), anchor="ra")

GAP3 = 14
colw = (W - 2 * M - (BRIEF_COLS - 1) * GAP3) // BRIEF_COLS
for ci in range(BRIEF_COLS):
    cx = M + ci * (colw + GAP3)
    for ri in range(BRIEF_PER_COL):
        n = ci * BRIEF_PER_COL + ri
        if n >= len(BRIEFS):
            break
        region, head, detail = BRIEFS[n]
        cy = BRIEF_ROWS_Y0 + ri * BRIEF_ROWH
        if ri:
            d.line([cx, cy - 3, cx + colw, cy - 3], fill=(228, 224, 214), width=1)
        d.rectangle([cx, cy + 2, cx + 4, cy + 15], fill=REGION_COLOR[region])
        d.text((cx + 9, cy), f"{7 + n:02d}", font=f(NARROW_B, 12), fill=REGION_COLOR[region])
        hs = fit(head, SANS_B, 17, colw - 34)
        d.text((cx + 30, cy - 2), head, font=f(SANS_B, hs), fill=INK)
        d.text((cx + 30, cy + 16), detail, font=f(SANS_R, 14), fill=DETAIL)

# ---------------------------------------------------------------- footer
d.rectangle([0, FOOTER_Y, W, H], fill=MAGENTA)
d.text((M, 972), "make.fun", font=f(SANS_B, 28), fill=WHITE)
d.text((M + 140, 981), "news-image-20261122", font=f(NARROW_B, 16), fill=(255, 222, 240))
d.text((W - M, 976), "SUNDAY 22 NOVEMBER 2026", font=f(NARROW_B, 15), fill=WHITE, anchor="ra")
d.text((W - M, 996), f"{TOTAL} stories \u00b7 7 regions \u00b7 one page", font=f(NARROW_R, 12),
       fill=(255, 222, 240), anchor="ra")

canvas.save("/workspace/work22/repo/entry.png", "PNG", optimize=True)
print("saved", canvas.size, "briefs bottom", last_text_bottom, "footer", FOOTER_Y)
