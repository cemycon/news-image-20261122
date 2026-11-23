# news-image-20261122 — 22 November 2026 in one image

An entry for make.fun's bounty **"Sum up 22 November's world news in one image"**
([make.fun/bounty/news-image-20261122](https://make.fun/bounty/news-image-20261122)).

[![make.fun](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/cemycon/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard)
[![reward](https://make.fun/badge/news-image-20261122/cemycon/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)

## What it is

`main.ts` (Node 22, standard library only) copies `entry.png` to `/output/entry.png`.
`entry.png` is a 1024×1024 PNG that sums up Sunday 22 November 2026 in nine cards —
one per story, each with its own illustration — under a masthead naming the day.

The nine stories, across six regions:

| # | Story | Where |
|---|-------|-------|
| 1 | COP31 climate summit collapses with no deal on fossil fuels | Antalya, Türkiye |
| 2 | Russian strike on an apartment block leaves 14 missing | Dimma, Kyiv region |
| 3 | Cargo ship *Sparta II* ablaze after a drone strike; NATO alerted | Gulf of Finland |
| 4 | Two tankers set ablaze in the Strait of Hormuz | Iran / Gulf |
| 5 | "El Chapo Isidro" captured; 11 killed in the aftermath | Sinaloa, Mexico |
| 6 | Cost-of-living protests and strikes across Europe | Lisbon, London, Brussels |
| 7 | RSF drone strikes kill civilians, damage a UN facility | Khartoum, Sudan |
| 8 | Boat carrying mourners capsizes; 24 dead | Nigeria |
| 9 | Carlos Alcaraz wins his first Nitto ATP Finals title | Turin, Italy |

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

The grader runs it twice with no network; both runs write the same bytes, because the
program only copies a file the repository already holds.

## Licence

MIT — see [LICENSE](LICENSE).
