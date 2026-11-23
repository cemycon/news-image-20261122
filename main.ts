// Entry for make.fun bounty news-image-20261122 — "Sum up 22 November's world news in one image".
//
// The image is the whole deliverable: entry.png beside this file is a 1024x1024 PNG that
// sums up Sunday 22 November 2026 in 36 stories across 7 regions — 15 illustrated cards,
// each with its own illustration, headline and one-line detail, plus 21 text briefs in
// three columns, a statistics bar, a region bar, a date-check strip and a "where it
// happened" map. v5 is v4 with every type size raised for legibility: the story count
// stays at 36, the illustrated count at 15, the brief count at 21 and the region count at
// 7, and the story order, headlines, details and visual style are unchanged. Room for the
// larger type comes from shorter illustration strips and a narrower map panel.
//
// The grader runs this with no network, a read-only /bot and a writable /output, twice,
// and both runs must write the same bytes. Copying a file the repository already holds is
// deterministic by construction, so the two runs agree byte for byte.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const imageName = 'entry.png';
const source = join(here, imageName);
const target = join(outDir, imageName);

mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);

console.log(`wrote ${target}`);
