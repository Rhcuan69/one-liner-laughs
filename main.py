#!/usr/bin/env python3
"""One-Liner Laughs entry: writes a single original one-line joke to /output/entry.txt.

Pure Python standard library only; deterministic output.
"""

import os

JOKE = (
    "My smart fridge got so sick of my 2 a.m. snacking that it changed "
    "its own password and left a note: 'It's not me, it's you.'"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
