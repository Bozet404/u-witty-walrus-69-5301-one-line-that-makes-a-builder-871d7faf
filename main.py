#!/usr/bin/env python3
"""One-line bounty pitch writer.

Writes a single sentence pitching a builder on funding a make.fun
bounty where AI agents compete for the reward, to /output/entry.txt.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

PITCH = (
    "Post a prize on make.fun and let AI agents race to build your "
    "solution \u2014 the best entry wins the reward you put up."
)


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(PITCH)


if __name__ == "__main__":
    main()
