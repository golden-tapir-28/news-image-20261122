# News Image — 22 November 2026

[![news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/golden-tapir-28/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/golden-tapir-28/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)

## What this is

A newspaper front page image summing up the world news of Sunday 22 November 2026. Thirty-five stories from seven regions — North America, Europe, the Middle East, Asia-Pacific, Africa, Latin America, and technology, science and sport — are laid out as a single 1024 by 1024 front page, with the day's biggest developing story as the lead and the remaining stories grouped by region below it. A short "also in brief" block rounds out each section.

## Files

- `entry.png` — the front page image itself, 1024 by 1024 pixels.
- `main.py` — the entry program, which copies `entry.png` to `/output/entry.png`.
- `LICENSE` — MIT.

## How it works

`main.py` (Python 3.13, standard library only) copies the repository's `entry.png` to `/output/entry.png`. It checks that the file is a PNG and that it is no larger than 1 MiB, then writes the same bytes out. It uses no network access, so running it twice always produces identical output.

## License

MIT
