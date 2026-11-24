#!/usr/bin/env python3
"""Two Days of Quiet Dread: write one approving, quietly dreadful PR review line.

The entry is a single line of at most 140 characters, written to
/output/entry.txt with no trailing newline. The line approves the pull
request twice in ordinary reviewer language, then lets the dread arrive
flat, as a permission: the code will outlive everyone who remembers why
it was needed.
"""

from pathlib import Path

LINE = "Approved. Ship it, and let it outlive everyone who remembers why we needed it."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    # Inline gate checks (kit gate: UTF-8 text, 1 to 140 characters,
    # not only whitespace, single line).
    assert isinstance(LINE, str)
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} characters"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    LINE.encode("utf-8")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
