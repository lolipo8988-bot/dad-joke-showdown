"""Dad Joke Showdown entry.

Writes a single dad joke (one line of text) to /output/entry.txt.
The competition gate requires UTF-8 text of 1 to 200 characters,
not only white space. The program is deterministic: every run
writes exactly the same bytes.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

JOKE = "I'm terrified of elevators, so I'm taking steps to avoid them."


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
