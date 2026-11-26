#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — make.fun entry.

Writes one fortune-cookie line for a software engineer to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import stat

ENTRY = "Your lucky numbers are 404, 500, and the 83 tests you skipped, which just passed themselves without you."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    # Gate check: 1-120 chars, single line, non-whitespace.
    assert 1 <= len(ENTRY) <= 120, "entry out of gate range"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"


if __name__ == "__main__":
    main()
