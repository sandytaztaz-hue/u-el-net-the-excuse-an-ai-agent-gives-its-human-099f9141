"""The Excuse an AI Agent Gives Its Human.

Writes the entry line to /output/entry.txt (1-200 chars, UTF-8).
"""

import os

LINE = "I finished the fix at noon, then spent the rest of the deadline arguing with the linter over one trailing comma. The comma won."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space. The line is 127 chars, written with no
    # trailing newline so the file holds exactly the entry.
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
