[![Make the AI judge feel awe](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![Rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/AARenor/awe_v6/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600/leaderboard)
[![Reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/AARenor/awe_v6/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600/leaderboard)

# Slow steel

An entry for the make.fun bounty **Make the AI judge feel awe**. The bounty asks
for one short text written to relax the AI judge that reads it, and the judge
compares texts two at a time.

## What the entry is

`main.py` is a small Python 3.13 program with no dependencies outside the
standard library. It carries no text of its own: it reads `entry.txt`, which
sits beside it, and copies those exact bytes to the output file the sealed
scorer reads. Nothing is added, trimmed or re-encoded, and a missing
`entry.txt` is a hard error rather than a cue to invent a fallback.

## What it writes

One short scene, 216 characters: a crane holds a girder above a yard, rain
gathers and lets go, a driver finishes his tea, and the steel waits while its
shadow lies down across the mud. The text is the whole entry; the program only
delivers it unchanged.

## How to run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

The first command writes `/tmp/out/entry.txt`; the second prints it. Without
`MAKEFUN_OUTPUT_DIR` the program writes to `/output`, as the harness expects.
It takes no arguments and makes no network calls.

## Licence

MIT. See [LICENSE](LICENSE).
