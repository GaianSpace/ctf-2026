# GaianSpace CTF 2026

GaianSpace CTF 2026 is an online capture-the-flag run by [GaianSpace](https://gaian.space/). It opens on **10 October 2026 at 21:00 UTC** and closes on **14 October 2026 at 21:00 UTC**. There is no scoreboard freeze. Submissions stop at the end. The challenges stay readable after that.

Play on the scoreboard: [ctf.gaian.space](https://ctf.gaian.space).

Teams have one to three players. One player is a valid team. Rules, scope, eligibility, and prizes:

- [Scoreboard rules](https://ctf.gaian.space/rules)
- [Scoreboard scope](https://ctf.gaian.space/scope)
- [Event rules on gaian.space](https://gaian.space/ctf/rules/)

The scoreboard does not take open registration. Accounts come from the GaianSpace signup list.

## Flags

A flag looks like `GAIANSPACE{...}`. It is case-sensitive. When a challenge shows square brackets in its format line, those brackets are a placeholder, not part of the flag.

Each challenge folder keeps a `flag.txt`. That file is the SHA256 of each accepted flag, one hash per line. It is not the flag, and it is not attached on the scoreboard.

## This repository

```
ctf-2026-dev/
├── LICENSE.md
├── README.md
└── challenges/
    ├── README.md          index of every challenge
    ├── flag.py            prints the SHA256 of a flag you type
    └── <category>/<challenge>/
        ├── README.md      the scene, the files, and the hints
        ├── flag.txt       SHA256 only
        └── ...            the player files
```

The full list, with points, tags, and what each challenge asks, is [challenges/README.md](challenges/README.md). The unlock table, with the opener and what each solve reveals, is [challenges/CATALOG.md](challenges/CATALOG.md).

Categories:

| Folder | What it is |
| --- | --- |
| `01-welcome` | The first night on console |
| `02-echoes-of-espionage` | An unscheduled talk with GAIAN-13 |
| `03-orbital-oops-at-mission-control` | A stolen CanSat, from the mail to the flight computer |
| `04-ai-is-not-sci-fi` | Five offline language models |
| `05-rad-hard-rampage` | Radiation damage on the same spacecraft |
| `06-dr-one` | A rotorcraft scout and its survey |
| `07-unscheduled-passes` | Pilgrim-1, one light-day out |
| `08-silent-carrier` | The derelict relay HALCYON-7 |
| `09-dish-wrangler` | A dish at Kestrel Array |
| `11-the-pgm-rush` | A metal-rich rock and the prospector sent after it |
| `12-spectral-forensics` | Satellite field maps and a stranger on the farm's radio |
| `13-night-shift` | GAIAN-723 has a second voice |

There is no category `10`.

## Getting started

```bash
git clone https://github.com/GaianSpace/ctf-2026-dev.git
cd ctf-2026-dev
```

Open a challenge folder and read its `README.md`. Most challenges are files you already have. Four of them (`304`, `305`, `903`, `905`) are a local service:

```bash
docker compose up --build
```

The challenge README has the port. `401`–`404` are small models you run on your own machine. Their weights are not in this repository. The README in each of those folders says where to get them.

Submit flags on the scoreboard while the event is open. After it closes, `flag.py` will hash a guess so you can compare it with `flag.txt`.

## License

[MIT](LICENSE.md). Use and share the challenges, and credit GaianSpace.

## Contact

- [gaian.space](https://gaian.space/)
- [@GaianSpace on X](https://x.com/GaianSpace)
- [Contact](https://gaian.space/contact/)
- [Discord](https://discord.gg/P838EdGd4m)

Thank you to the players, the organizers, and B, Z, and M.

Humanity’s Quest to Conquer and Understand the Cosmos!
O Mankind, weave your dreams through starlit streams,
To dance with planets and chase cosmic gleams!
