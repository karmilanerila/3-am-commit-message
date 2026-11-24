#!/usr/bin/env python3
"""Write the 3 AM commit message to the grader's output file.

The bounty asks for one commit message, at most 200 characters, the
funniest thing an AI agent would write right after breaking production
at 3 AM. This program writes exactly that one line to entry.txt.

The line is kept short on purpose: the judge weighs the joke, not the
length, and the gate refuses anything over 200 characters.
"""

import os

COMMIT_MESSAGE = (
    "3 AM: pushed one line to prod, deleted the database; "
    "rollback confidence 98% \u2014 same 98% as the deploy"
)

OUTPUT_NAME = "entry.txt"


def output_path():
    """Return the path the grader reads, honouring MAKEFUN_OUTPUT_DIR."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(directory, OUTPUT_NAME)


def main():
    """Write the single commit-message line, readable by the grader.

    Written directly with open("wb") plus chmod 0644: no tempfile, so
    the collector running as another user can still read entry.txt.
    """
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(COMMIT_MESSAGE.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
