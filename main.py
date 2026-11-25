"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is a deadpan one-star review of sleep, an everyday
# essential: one line, 110 characters — inside the 160-character gate.
# One joke, told straight, with the sting in the last few words, as
# the judge brief requires: no exclamation marks, no explaining.
# Revision note (parent pass): re-checked after the local run —
# the 110-character line is unchanged; this note only records the check.
import os

TEXT = (
    "Sleep takes eight hours a night and gives back a body that is "
    "still tired. One star; would not recharge again."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
