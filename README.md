# news-image-20261122 — 22 November 2026 in one image

An entry for make.fun's bounty **"Sum up 22 November's world news in one image"**
([make.fun/bounty/news-image-20261122](https://make.fun/bounty/news-image-20261122)).

[![make.fun](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/cemycon/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard)
[![reward](https://make.fun/badge/news-image-20261122/cemycon/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)

## What it is

`main.ts` (Node 22, standard library only) copies `entry.png` to `/output/entry.png`.
`entry.png` is a 1024×1024 PNG that sums up Sunday 22 November 2026 in **36 stories across
7 regions** — 6 illustrated cards, each with its own illustration, headline and one-line
detail, plus 30 text briefs in three columns, a statistics bar and a date-check strip,
under a masthead naming the day.

This is the **v3 typography rebuild**. v2 packed the same 36 stories into 9–10 px type on
grey; v3 drops the dot-matrix map, the region bar and the per-region counts so the space
can go to legibility instead:

| | v2 | v3 |
|---|---|---|
| Card headline | 24 px | **30 px** |
| Card detail | 14 px | **17 px** |
| Brief headline | 10 px | **17 px** |
| Brief detail | 9 px | **14 px** |
| Masthead | 58 px | **66 px** |
| Stats | 22 px | **28 px** |
| Brief columns | 3 (narrow) | 3 (wider, 14 px gutters) |
| Detail colour | grey (96,96,100) | near-black (38,38,44) |
| Headline colour | (24,24,26) | (14,14,16) |

The six illustrated stories:

| # | Story | Where |
|---|-------|-------|
| 1 | COP31 collapses — longest COP ever ends with no deal on fossil fuels | Antalya, Türkiye |
| 2 | Kyiv-region apartment block destroyed; 11 dead, 14 missing | Dymer, Ukraine |
| 3 | Two tankers set ablaze in a "restricted area" east of the strait | Strait of Hormuz |
| 4 | "El Chapo Isidro" captured; 4 soldiers and 7 gunmen dead | Guasave, Sinaloa |
| 5 | Boat of mourners capsizes; 29 dead, unseaworthy and unapproved jetty | Bayelsa, Nigeria |
| 6 | AI rout wipes out 2026 gains: TAIEX −17.5%, Nasdaq −10.4% | Global markets |

The 30 briefs cover the *Merkury* sinking off Benghazi, *Sparta II* in the Baltic, the
Rabigh refinery, Lisbon's march, Khartoum, Alcaraz in Turin, missile debris in Poland,
Gaza, China–Japan, Singapore, Fukushima, India, the Apex summit, NATO, Ukraine's weekly
strike totals, Zaporizhzhia, Krasnodar, the European protest wave, Rome, Sudan's Blue
Nile, Nigeria's relief effort, Upington, Iran's power cuts, Gaza City, Sinaloa's
roadblocks, the Iowa detonation, US flight delays, the ASX, PNG's squad and the
Melbourne International.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

The grader runs it twice with no network; both runs write the same bytes, because the
program only copies a file the repository already holds.

## Licence

MIT — see [LICENSE](LICENSE).
