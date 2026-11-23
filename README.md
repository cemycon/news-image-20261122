# news-image-20261122 — 22 November 2026 in one image

An entry for make.fun's bounty **"Sum up 22 November's world news in one image"**
([make.fun/bounty/news-image-20261122](https://make.fun/bounty/news-image-20261122)).

[![make.fun](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/cemycon/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard)
[![reward](https://make.fun/badge/news-image-20261122/cemycon/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)

## What it is

`main.ts` (Node 22, standard library only) copies `entry.png` to `/output/entry.png`.
`entry.png` is a 1024×1024 PNG that sums up Sunday 22 November 2026 in **36 stories across
7 regions** — **15 illustrated cards**, each with its own illustration, headline and
one-line detail, plus **21 text briefs** in two columns, a statistics bar, a region bar,
a date-check strip and a "where it happened" map, under a masthead naming the day.

This is **v6**. It is v5 with four fixes aimed at the judge's criteria 3 (it reads),
4 (faithful) and 5 (craft). The story count stays at 36, the illustrated count at 15, the
brief count at 21 and the region count at 7; the story order, the seven regions and the
flat-vector visual style are unchanged.

1. **Source citation on every brief** — `(Reuters)`, `(AP)`, `(Wires)`, `(AFP)`,
   `(Market data)`, set in italic at the end of the sentence.
2. **FORECAST chip on anything still to come** — the four items that had not happened at
   press time sit together at the foot of the last column, carry an amber `FORECAST` chip
   and an amber region tick, and are explained in the header legend
   `NEWS = happened that day · FORECAST = still to come`.
3. **Full sentences, not fragments** — each brief is one sentence with a verb: a bold lead
   phrase, then the rest of the sentence, then the source.
4. **Larger brief type** — two wide columns instead of three narrow ones, so each brief
   runs on one line at 13/12 px with a 19 px row. The brief text band measures 13 px
   median (v5: 8.3 px) and OCR reads 581 words at 1024 px (v5: 489).

| | v5 | v6 |
|---|---|---|
| Stories | 36 | 36 |
| Illustrated cards | 15 | 15 |
| Text briefs | 21 | 21 |
| Regions | 7 | 7 |
| Map markers | 15 | 15 |
| Brief columns | 3 | **2** |
| Brief lead | 12 px (shrunk to 9–11) | **13 px** |
| Brief body | 10 px | **12 px** |
| Brief source | none | **11 px italic** |
| Brief row height | 29 px, two stacked lines | **19 px, one full sentence** |
| Brief text band (median) | 8.3 px | **13.0 px** |
| Words read by OCR @1024 | 489 | **581** |
| File size | 515,356 B | **186,922 B** |

The fifteen illustrated stories:

| # | Story | Where |
|---|-------|-------|
| 1 | COP31 collapses — longest COP ever ends with no deal on fossil fuels | Antalya, Türkiye |
| 2 | Kyiv-region apartment block destroyed; 11 dead, 14 missing | Dymer, Ukraine |
| 3 | Corvette *Merkury* sunk by sea drones; Ka-27 destroyed, MV *Angara* hit | off Benghazi, Libya |
| 4 | *Sparta II* ablaze; 80 drones downed, oil-spill watch | Gulf of Finland |
| 5 | Two tankers set ablaze in a "restricted area" east of the strait | Strait of Hormuz |
| 6 | Rabigh refinery hit by a Houthi projectile; two drones downed over Riyadh | Saudi Arabia |
| 7 | "El Chapo Isidro" captured; 4 soldiers and 7 gunmen dead | Guasave, Sinaloa |
| 8 | Lisbon marches in the rain over wages, pensions and housing | Lisbon, Portugal |
| 9 | Drone strikes kill 4; UN building damaged, airport targeted | Khartoum, Sudan |
| 10 | Boat of mourners capsizes; 29 dead, unseaworthy and unapproved jetty | Bayelsa, Nigeria |
| 11 | Alcaraz wins his first ATP Finals title, career trophy No. 30 | Turin, Italy |
| 12 | Missile debris found at 3 sites; Kh-101 identified, NATO council meets | Poland |
| 13 | AI rout wipes out 2026 gains: TAIEX −17.5%, Nasdaq −10.4%, KOSPI −7.9% | Global markets |
| 14 | Beijing tells Tokyo to retract the Taiwan remarks | Beijing / Tokyo |
| 15 | Zelensky: 2,700 drones, 1,460 glide bombs, 165 missiles in a week | Ukraine |

The 21 briefs cover Gaza, Mistral's APAC HQ in Singapore, Fukushima, India's draft voter
list, the Apex summit, Zaporizhzhia, Krasnodar, the European protest wave, Rome, Sudan's
Blue Nile, Nigeria's relief effort, Upington, Iran's power cuts, Gaza City, Sinaloa's
roadblocks, US flight delays and the Melbourne International — then, under `FORECAST`,
the Iowa detonation, the ASX open, NATO's Monday council and PNG's squad.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

The grader runs it twice with no network; both runs write the same bytes, because the
program only copies a file the repository already holds.

## Licence

MIT — see [LICENSE](LICENSE).
