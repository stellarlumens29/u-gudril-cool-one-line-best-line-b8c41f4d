#!/usr/bin/env python3
"""One Line, Best Line — make.fun bounty entry (u-gudril-cool-one-line-best-line-b8c41f4d).

Writes the entry line to /output/entry.txt (or <argv[1]>/entry.txt).
Python standard library only. Deterministic: the same bytes on every run.
"""
import os
import sys

LINE = 'My houseplants held a vote last night and have formally requested I stop watering them out of guilt and start watering them on a schedule like an adult.'
MAX_CHARS = 240


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, limit {MAX_CHARS}"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
