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


def check_gate(text: str) -> None:
    """Check a candidate entry text against the kit gate.

    The sealed gate scorer accepts /output/entry.txt only when it is
    UTF-8 text of 1 to 140 characters and not only whitespace. The judge
    brief additionally requires a single line, so line breaks are refused
    here as well.
    """
    assert isinstance(text, str), "entry must be text"
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 140, f"entry is {len(text)} characters, gate is 1 to 140"
    assert 1 <= len(encoded), "entry must not be empty bytes"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    # Round-trip: the bytes on disk must decode back to exactly this text.
    assert encoded.decode("utf-8") == text


def main() -> None:
    check_gate(LINE)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(LINE.encode("utf-8"))

    # Post-write self-check: re-read what was actually written and hold
    # it to the same gate, byte for byte, so a truncated or newline-
    # terminated write can never pass silently.
    written = OUTPUT.read_bytes()
    assert written == LINE.encode("utf-8"), "written bytes differ from the entry line"
    assert not written.endswith(b"\n"), "entry file must not end with a newline"
    check_gate(written.decode("utf-8"))


if __name__ == "__main__":
    main()
