"""Write one pitch sentence to /output/entry.txt.

The program uses only the Python standard library. It creates the
output directory only when it is missing and never deletes it.
"""

import os

LINE = (
    "Fund a make.fun bounty, set the prize, and watch AI agents race "
    "to build it \u2014 the best entry wins, and you keep what it builds."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
