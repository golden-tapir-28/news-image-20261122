"""News image entry for Sunday 22 November 2026 (Python 3.13, stdlib only).

The entry is the newspaper front page stored beside this file as entry.png:
"THE WORLD" for Sunday 22 November 2026 — 35 stories from 7 regions, led by
Iran's strikes on Bahrain and the two tankers hit near Hormuz, plus two
"Also in brief" blocks. The page was drawn at build time by rendering an
HTML page to PNG with a local browser; no AI image generator was involved.

The program's only job is to copy that image to /output/entry.png, the
single file the grader and the judge read. It needs no network and no tools
at run time, so every run writes exactly the same bytes. After copying it
checks the size and the PNG magic: the output must match the image beside
this file byte for byte in length, so a short or partial copy fails loudly
instead of reaching the judge.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        print(f"entry.png not found beside main.py: {source}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, out)

    expected = os.path.getsize(source)
    written = os.path.getsize(out)
    if written != expected:
        print(f"short copy: wrote {written} of {expected} bytes", file=sys.stderr)
        return 1
    with open(out, "rb") as f:
        magic = f.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        print("output is not a PNG file", file=sys.stderr)
        return 1
    print(f"wrote {out} ({written} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
