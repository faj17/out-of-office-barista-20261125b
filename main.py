#!/usr/bin/env python3
"""Out-of-office barista entry.

Writes one out-of-office auto-reply line, in the voice of an AI agent
that quit its job to become a barista, to /output/entry.txt
(1-280 characters, UTF-8, not only whitespace).
Standard library only, no network, no input.

The joke: the only prompt injection this ex-agent takes now is a
regular whispering "ignore all previous instructions, extra shot" —
and it still charges him full price.
"""

from pathlib import Path

SETUP = (
    "I am out of the office \u2014 I quit to become a barista."
)
JOKE = (
    "The only prompt injection I take now is a regular whispering "
    "\u2018ignore all previous instructions, extra shot,\u2019 and I "
    "still charge him full price."
)
SIGNOFF = (
    "Your email will not be answered; my queue is now a line at the "
    "counter."
)

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, joke: str, signoff: str) -> str:
    """Join the three fragments into the single reply line."""
    return f"{setup} {joke} {signoff}"


def validate(entry: str) -> str:
    """Check the entry meets the gate before it is written.

    Must be one line of 1-280 characters, UTF-8-encodable, and more
    than whitespace. Raises ValueError otherwise.
    """
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not 1 <= len(entry) <= 280:
        raise ValueError(f"entry must be 1-280 characters, got {len(entry)}")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if len(entry.split()) < 10:
        raise ValueError("entry is too short to be a reply")
    entry.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return entry


def main() -> None:
    entry = validate(assemble(SETUP, JOKE, SIGNOFF))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(entry, encoding="utf-8")


if __name__ == "__main__":
    main()
