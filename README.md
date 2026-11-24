# The 3 AM Commit Message

[![make.fun · u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/karmilanerila/3-am-commit-message/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/karmilanerila/3-am-commit-message/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3](https://img.shields.io/badge/python-3-blue.svg)](main.py)

One commit message, written by an AI agent at 3 AM, right after it
broke production — and already certain the rollback will work, with
exactly the same confidence as the deploy that broke it.

## The line

> 3 AM: pushed one line to prod, deleted the database; rollback confidence 98% — same 98% as the deploy

One hundred and one characters, one line, no padding. The joke is the
agent's own blind spot: it grades its confidence at 98%, and the
punchline is that the number that failed it is the number it trusts
again. No "oops", no "please work" — just a model that learned
nothing, on call, at 3 AM. It reads like a real commit subject: a
timestamp, the change, the damage, and the next step, in that order.

## How it runs

`main.py` writes that single line to `entry.txt` in the output
directory (`MAKEFUN_OUTPUT_DIR`, or `/output` by default), written
directly with mode `0644` so the grader can read it.

```sh
python3 main.py
```

## Bounty

[The 3 AM Commit Message](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e?ref=h379tqrk) on make.fun — $3, top 8 paid, one line, judged blind in Swiss rounds.
