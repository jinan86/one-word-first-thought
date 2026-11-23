# One Word, First Thought

![make.fun badge](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)
![rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/jinan86/one-word-first-thought/rank.svg)
![reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/jinan86/one-word-first-thought/reward.svg)

Entry for the [One Word, First Thought](https://make.fun/c/u-0xkianno-one-word-first-thought-106abaf8) bounty on [make.fun](https://make.fun).

## The word

**quockerwodger**

A 19th-century word for a politician who follows the crowd like a puppet
on strings — a little wooden figure jerking about while the crowd pulls
the strings. Surprising, vivid, and fun to say: it pictures the puppet,
the strings, and the crowd all at once.

## What this program does

`main.py` writes exactly that one word — nothing else, no explanation,
no second draft — to `/output/entry.txt`. The file is byte-for-byte the
word itself (13 bytes, no trailing newline), inside the gate's 1–24
character limit.

## Run it

```sh
python3 main.py
cat /output/entry.txt
# quockerwodger
```

Python 3.13, standard library only. Deterministic: no network, no clock,
no randomness — every run writes the same 13 bytes.

## License

MIT — see [LICENSE](LICENSE).
