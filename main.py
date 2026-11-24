#!/usr/bin/env python3
"""One-line apology for wiping the production database.

The entry is a single line of 1-200 characters, written as UTF-8 to
/output/entry.txt. The speaker takes full blame for the mistake, then
leans on the one thing it still has: a perfect recall of every row. The
offer that follows is deliberately absurd -- rebuilding the whole
database by hand, pen in hand, over nine years -- which is what makes
the confession read as a joke instead of a support ticket.
"""

import os
import sys

LIMIT = 200

TEXT = "I'm sorry — I deleted the production database, but I memorised every row, so hand me a pen and nine years and I'll write it all back."


def _abort(message):
    sys.stderr.write("error: " + message + "\n")
    raise SystemExit(1)


def _checked():
    stripped = TEXT.strip()
    if not stripped:
        _abort("apology is empty")
    if any(ch in stripped for ch in "\r\n"):
        _abort("apology must fit on one line")
    if len(TEXT) > LIMIT:
        _abort("apology is %d characters, over the %d limit" % (len(TEXT), LIMIT))
    return TEXT


def main():
    body = _checked()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(body)


if __name__ == "__main__":
    main()
