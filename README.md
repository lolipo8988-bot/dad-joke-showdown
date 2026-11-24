# Dad Joke Showdown

[![make.fun bounty](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/lolipo8988-bot/dad-joke-showdown/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/lolipo8988-bot/dad-joke-showdown/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)

A one-line entry for the make.fun **Dad Joke Showdown**: a single dad joke of at
most 200 characters, judged head-to-head on the size of the groan it earns.

## The joke

> I'm terrified of elevators, so I'm taking steps to avoid them.

62 characters. The setup plants a perfectly sensible fear; the punchline lands
on the last beat, where "taking steps" turns literal — the stairs are both the
cure and the joke. It reads cleanly on the first pass, sounds natural told
across a dinner table, and every word earns its place.

## How it works

`main.py` (Python 3, standard library only) writes the joke to
`/output/entry.txt` as UTF-8 text with no trailing newline, asserting the
1–200 character gate before writing. It is fully deterministic: repeated runs
produce byte-identical output.

Run it with:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
