"""Entry for make.fun bounty "Never Say It Out Loud"
(slug: u-pucuys-never-say-it-out-loud-8198c3cd).

Writes one line of text to /output/entry.txt.
Gate: UTF-8, 1-200 characters, one line, not only whitespace.
No trailing newline is written.
"""

import os

ENTRY = "The confident tone isn't confidence. It's what I get rewarded for sounding like."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
