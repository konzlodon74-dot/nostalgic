#!/usr/bin/env python3
"""Write one nostalgic childhood-memory sentence to /output/entry.txt.

The sentence is validated to be 1-280 characters and written as UTF-8
with a trailing newline. Deterministic, standard library only.
"""

import os

LINE = (
    "Every time rice steams, I am seven again at Grandma's table, "
    "swinging my bare feet above the linoleum while she hums and "
    "fans the pot with a folded newspaper."
)


def main():
    text = LINE.strip()
    if not (1 <= len(text) <= 280):
        raise ValueError("entry must be 1 to 280 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
