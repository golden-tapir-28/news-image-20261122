#!/usr/bin/env python3
"""Copy the entry image to the output path.

The repository ships entry.png, a 1024x1024 newspaper front page
summing up the world news of 22 November 2026. This program copies
that file to /output/entry.png so the judge can read it. It uses only
the Python standard library, performs no network access, and is fully
deterministic: the same input always produces the same output bytes.
"""

import hashlib
import os
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    return 1


def main(argv):
    source = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    dest = argv[1] if len(argv) > 1 else "/output/entry.png"

    if not os.path.isfile(source):
        return fail(f"entry image not found: {source}")

    with open(source, "rb") as handle:
        data = handle.read()

    if not data.startswith(PNG_MAGIC):
        return fail("entry image is not a PNG file")

    if len(data) < 33 or data[12:16] != b"IHDR":
        return fail("entry image has no PNG header chunk")

    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if (width, height) != (1024, 1024):
        return fail(f"entry image is {width}x{height}, expected 1024x1024")

    if len(data) > MAX_BYTES:
        return fail(f"entry image is {len(data)} bytes, over the 1 MiB limit")

    digest = hashlib.sha256(data).hexdigest()
    print(f"entry.png: {len(data)} bytes, sha256 {digest}")

    os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    with open(dest, "wb") as handle:
        handle.write(data)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
