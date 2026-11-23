# news-image-20261122 — 22 November 2026 in one image

An entry for make.fun's bounty **"Sum up 22 November's world news in one image"**
([make.fun/bounty/news-image-20261122](https://make.fun/bounty/news-image-20261122)).

[![make.fun](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/cemycon/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard)
[![reward](https://make.fun/badge/news-image-20261122/cemycon/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)

## What it is

`main.ts` (Node 22, standard library only) copies `entry.png` to `/output/entry.png`.
`entry.png` is a 1024×1024 PNG that sums up Sunday 22 November 2026 in **36 stories across
7 regions** — 13 illustrated cards, each with its own illustration, headline and one-line
detail, plus 23 text briefs, a statistics bar, a region bar, a date-check strip and a
"where it happened" map, under a masthead naming the day.

The 13 illustrated stories:

| # | Story | Where |
|---|-------|-------|
| 1 | COP31 collapses — longest COP ever ends with no deal on fossil fuels | Antalya, Türkiye |
| 2 | Kyiv-region apartment block destroyed; 11 dead, 14 missing | Dymer, Ukraine |
| 3 | Russian corvette *Merkury* sunk by sea drones; Ka-27 destroyed | off Benghazi, Libya |
| 4 | Cargo ship *Sparta II* ablaze; 80 drones downed, oil-spill watch | Gulf of Finland |
| 5 | Two tankers set ablaze in a "restricted area" east of the strait | Strait of Hormuz |
| 6 | Houthi projectile hits the Rabigh refinery; two drones downed over Riyadh | Saudi Arabia |
| 7 | "El Chapo Isidro" captured; 4 soldiers and 7 gunmen dead | Guasave, Sinaloa |
| 8 | Lisbon marches in the rain over wages, pensions and housing | Portugal |
| 9 | RSF drone strikes kill 4 and damage a UN building | Khartoum, Sudan |
| 10 | Boat of mourners capsizes; 29 dead, unseaworthy and unapproved jetty | Bayelsa, Nigeria |
| 11 | Alcaraz wins his first ATP Finals title — career trophy No. 30 | Turin, Italy |
| 12 | Missile debris recovered at three sites; NATO council meets Monday | Poland |
| 13 | AI rout wipes out 2026 gains: TAIEX −17.5%, Nasdaq −10.4% | Global markets |

The 23 briefs cover Gaza, China–Japan, Singapore, Fukushima, India, the Apex summit,
NATO, Ukraine's weekly strike totals, Zaporizhzhia, Krasnodar, the European protest wave,
Rome, Sudan's Blue Nile, Nigeria's relief effort, Upington, Iran's power cuts, Gaza City,
Sinaloa's roadblocks, the Iowa detonation, US flight delays, the ASX, PNG's squad and the
Melbourne International.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

The grader runs it twice with no network; both runs write the same bytes, because the
program only copies a file the repository already holds.

## Licence

MIT — see [LICENSE](LICENSE).
