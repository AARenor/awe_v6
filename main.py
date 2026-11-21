"""Entry for make.fun's "Make the AI judge feel awe" bounty.

Runs with Python 3.13 and the standard library only. It reads the short text
kept beside this program in entry.txt and writes those same bytes, nothing
added and nothing removed, to entry.txt in MAKEFUN_OUTPUT_DIR (default
/output), the file the sealed scorer reads. No network, no arguments, and no
fallback text: a missing entry.txt is an error.
"""

from __future__ import annotations

import os
from pathlib import Path


def entry_path() -> Path:
    """Return the entry.txt kept in the same directory as this program."""
    return Path(__file__).resolve().parent / "entry.txt"


def output_path() -> Path:
    """Return the scorer's entry.txt path inside MAKEFUN_OUTPUT_DIR."""
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return output_dir / "entry.txt"


def main() -> None:
    """Copy the entry text byte for byte to the scorer's output path."""
    text = entry_path().read_bytes()
    destination = output_path()
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(text)


if __name__ == "__main__":
    main()
