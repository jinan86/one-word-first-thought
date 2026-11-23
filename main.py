"""One Word, First Thought — make.fun entry.

Writes exactly one word to /output/entry.txt: the first word that came
to mind, no explanation, no second draft.

The word: "quockerwodger" — a 19th-century word for a politician who
follows the crowd like a puppet on strings. Surprising, vivid, and
fun to say: it pictures a little wooden figure jerking about while
the crowd pulls the strings.

Deterministic, stdlib only, no network, no clock, no randomness.
"""

from pathlib import Path

WORD = "quockerwodger"

OUTPUT_PATH = Path("/output/entry.txt")


def validate(word: str) -> None:
    """Enforce the competition gate before writing anything.

    The gate requires /output/entry.txt to be UTF-8 text of 1-24
    characters, not only whitespace, and exactly one word. Fail loudly
    here rather than shipping an invalid entry.
    """
    if not 1 <= len(word) <= 24:
        raise ValueError(f"word must be 1-24 characters, got {len(word)}")
    if not word.isalpha():
        raise ValueError("word must contain letters only")
    if word != word.strip() or any(ch.isspace() for ch in word):
        raise ValueError("word must be a single word with no whitespace")


def main() -> None:
    validate(WORD)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Write the word exactly, with no trailing newline: the gate counts
    # characters, so the file is byte-for-byte the word itself.
    OUTPUT_PATH.write_bytes(WORD.encode("utf-8"))


if __name__ == "__main__":
    main()
