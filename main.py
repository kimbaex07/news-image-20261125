#!/usr/bin/env python3
"""Entry program for the news-image-20261125 bounty.

Copies the front-page image held beside this file to the output
directory, byte for byte, so both grader runs write identical output.
The image itself is composed offline (see README); this program only
delivers it. Python 3.13, standard library only, no network.
"""
import os
import shutil
import struct

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The sealed gate: entry.png must be a PNG of at most 1 MiB and at most
# 1024x1024 pixels. Check the file we ship before copying it, so a bad
# build fails loudly here instead of being refused by the gate.
MAX_BYTES = 1048576
MAX_DIM = 1024


def _check_png(path):
    with open(path, "rb") as f:
        head = f.read(33)
    if len(head) < 33 or head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry.png is not a PNG file")
    if head[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", head[16:24])
    if width > MAX_DIM or height > MAX_DIM:
        raise ValueError(f"entry.png is {width}x{height}, gate allows at most {MAX_DIM}x{MAX_DIM}")
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        raise ValueError(f"entry.png is {size} bytes, gate allows at most {MAX_BYTES}")


def main():
    src = os.path.join(HERE, "entry.png")
    _check_png(src)
    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, "entry.png")
    shutil.copyfile(
        os.path.join(HERE, "entry.png"),
        out,
    )
    os.chmod(out, 0o644)


if __name__ == "__main__":
    main()
