#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one line, the funniest sick-day excuse we could land in a single
breath, to /output/entry.txt. Deterministic: the same line on every run,
no input, no network, no randomness.
"""

import os

# The line: a believable setup (a back injury, the most ordinary sick-day
# ailment there is) that turns on the snooze button, then lands the laugh
# on the last words — held hostage by the mattress that was supposed to
# help you rest. One breath, one line, nothing else.
ENTRY = "Can't come in today — my back went out reaching for the snooze button and now I'm being held hostage by my own mattress."

OUTPUT = "/output/entry.txt"


def main() -> None:
    line = ENTRY.strip()
    # Gate self-check: one line, 1 to 200 characters, not only whitespace.
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    assert line.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Post-write verification: read it back byte-exact, and re-check the
    # gate on what is actually on disk, not just on the string in memory.
    with open(OUTPUT, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == line, "written entry differs from the line"
    assert 1 <= len(written) <= 200 and "\n" not in written


if __name__ == "__main__":
    main()
