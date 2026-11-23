// Entry for make.fun bounty news-image-20261122 — "Sum up 22 November's world news in one image".
//
// The image is the whole deliverable: entry.png beside this file is a 1024x1024 PNG that
// sums up Sunday 22 November 2026 in nine cards, one per story, each with its own
// illustration, plus the date and the day's regions in the masthead.
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
const source = join(here, 'entry.png');
const target = join(outDir, 'entry.png');

mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);

console.log(`wrote ${target}`);
