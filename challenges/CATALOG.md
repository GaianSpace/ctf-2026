# Challenge catalog

Index of every GaianSpace CTF 2026 card. **Requires** is the opener: that card must be solved before this one appears. **Next** is what this solve reveals. Only `100-well-hello` has no opener. Every other card stays hidden until its opener is solved. One solve can open several cards. There is no locked placeholder card.

`701`–`704` are also hidden until their release. After the release `701` opens once your team has solved `100-well-hello`; `702`, `703`, and `704` wait on the previous card as well. `121` and `131` work the same way: hidden until their release, then open after `100-well-hello`; `122`–`124` and `132`–`135` then open one after another.

Points show the starting value and the floor. Dynamic cards lose value as more teams solve them and reach half their starting value at 20 solves; every team that solved a card holds its current value. The `01-welcome` cards, the `04-ai-is-not-sci-fi` cards, and the four cards opened by `604-ice-vault` keep fixed points.

| Solve | Also opens |
| --- | --- |
| `100` | `101` |
| `101` | `102` and `201` |
| `102` | `103` |
| `201` | `202`, `206`, and `207` |
| `203` | `204`, `301`, and `501` |
| `301` | `302`, `306`, and `307` |
| `305` | `401`, then `402`, `403`, and `404` in order |
| `501` | `502`, `505`, and `601` |
| `503` | `504` and `801` |
| `603` | `604` and `901` |
| `124` | `125` and `126` |
| `604` | `110`, `111`, `112`, `113`, `114`, `115`, `116`, `117`, and `605` |

| # | Challenge | Category | Tags | Points | Type | Requires | If locked | Next |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [100-well-hello](01-welcome/00-well-hello/) | 01-welcome | misc, welcome | 1 | standard | — | — | 101 |
| 2 | [101-this-is-gaianspace](01-welcome/01-this-is-gaianspace/) | 01-welcome | osint | 10 | standard | 100-well-hello | Hidden | 102, 201 |
| 3 | [102-cs-for-gs](01-welcome/02-cs-for-gs/) | 01-welcome | osint | 20 | standard | 101-this-is-gaianspace | Hidden | 103 |
| 4 | [103-parked-birds](01-welcome/03-parked-birds/) | 01-welcome | osint | 20 | standard | 102-cs-for-gs | Hidden | — |
| 5 | [201-uplink-origins](02-echoes-of-espionage/01-uplink-origins/) | 02-echoes-of-espionage | osint, tle | 100 → 50 | dynamic | 101-this-is-gaianspace | Hidden | 202, 206, 207 |
| 6 | [202-downlink-deception](02-echoes-of-espionage/02-downlink-deception/) | 02-echoes-of-espionage | forensics, tle | 150 → 75 | dynamic | 201-uplink-origins | Hidden | 203 |
| 7 | [203-signal-secrets](02-echoes-of-espionage/03-signal-secrets/) | 02-echoes-of-espionage | stegano | 200 → 100 | dynamic | 202-downlink-deception | Hidden | 204, 301, 501 |
| 8 | [204-payload-unleashed](02-echoes-of-espionage/04-payload-unleashed/) | 02-echoes-of-espionage | reverse | 200 → 100 | dynamic | 203-signal-secrets | Hidden | 205 |
| 9 | [205-backdoor-from-space](02-echoes-of-espionage/05-backdoor-from-space/) | 02-echoes-of-espionage | forensics | 250 → 125 | dynamic | 204-payload-unleashed | Hidden | — |
| 10 | [206-gpredict-secret](02-echoes-of-espionage/06-gpredict-secret/) | 02-echoes-of-espionage | osint, tle | 100 → 50 | dynamic | 201-uplink-origins | Hidden | — |
| 11 | [207-lost-signal-to-mars](02-echoes-of-espionage/07-lost-signal-to-mars/) | 02-echoes-of-espionage | dsp, radio | 150 → 75 | dynamic | 201-uplink-origins | Hidden | — |
| 12 | [301-email-entrapment](03-orbital-oops-at-mission-control/01-email-entrapment/) | 03-orbital-oops-at-mission-control | forensics | 100 → 50 | dynamic | 203-signal-secrets | Hidden | 302, 306, 307 |
| 13 | [302-web-wormhole](03-orbital-oops-at-mission-control/02-web-wormhole/) | 03-orbital-oops-at-mission-control | network, forensics | 150 → 75 | dynamic | 301-email-entrapment | Hidden | 303 |
| 14 | [303-gerber-grab-crack](03-orbital-oops-at-mission-control/03-gerber-grab-crack/) | 03-orbital-oops-at-mission-control | forensics, crypto | 200 → 100 | dynamic | 302-web-wormhole | Hidden | 304 |
| 15 | [304-pcb-puzzle-probe](03-orbital-oops-at-mission-control/04-pcb-puzzle-probe/) | 03-orbital-oops-at-mission-control | hardware | 200 → 100 | dynamic | 303-gerber-grab-crack | Hidden | 305 |
| 16 | [305-satellite-sabotage-sim](03-orbital-oops-at-mission-control/05-satellite-sabotage-sim/) | 03-orbital-oops-at-mission-control | reverse, pwn | 250 → 125 | dynamic | 304-pcb-puzzle-probe | Hidden | 401 |
| 17 | [306-lora-whisper](03-orbital-oops-at-mission-control/06-lora-whisper/) | 03-orbital-oops-at-mission-control | radio, forensics | 100 → 50 | dynamic | 301-email-entrapment | Hidden | — |
| 18 | [307-descent-diary](03-orbital-oops-at-mission-control/07-descent-diary/) | 03-orbital-oops-at-mission-control | forensics, data | 150 → 75 | dynamic | 301-email-entrapment | Hidden | — |
| 19 | [401-ai-at-gaian](04-ai-is-not-sci-fi/01-ai-at-gaian/) | 04-ai-is-not-sci-fi | ai, llm | 150 | standard | 305-satellite-sabotage-sim | Hidden | 402 |
| 20 | [402-the-cyberaid](04-ai-is-not-sci-fi/02-the-cyberaid/) | 04-ai-is-not-sci-fi | ai, llm | 200 | standard | 401-ai-at-gaian | Hidden | 403 |
| 21 | [403-altruizine](04-ai-is-not-sci-fi/03-altruizine/) | 04-ai-is-not-sci-fi | ai, llm | 250 | standard | 402-the-cyberaid | Hidden | 404 |
| 22 | [404-the-last-kilogram](04-ai-is-not-sci-fi/04-the-last-kilogram/) | 04-ai-is-not-sci-fi | ai, llm | 300 | standard | 403-altruizine | Hidden | 405 |
| 23 | [501-cosmic-bit-blunder](05-rad-hard-rampage/01-cosmic-bit-blunder/) | 05-rad-hard-rampage | crypto, hardware | 100 → 50 | dynamic | 203-signal-secrets | Hidden | 502, 505, 601 |
| 24 | [502-ionized-transistangle](05-rad-hard-rampage/02-ionized-transistangle/) | 05-rad-hard-rampage | hardware, logic | 150 → 75 | dynamic | 501-cosmic-bit-blunder | Hidden | 503 |
| 25 | [503-degradift](05-rad-hard-rampage/03-degradift/) | 05-rad-hard-rampage | forensics, data | 200 → 100 | dynamic | 502-ionized-transistangle | Hidden | 504, 801 |
| 26 | [504-lunar-latch-up](05-rad-hard-rampage/04-lunar-latch-up/) | 05-rad-hard-rampage | crypto, hardware | 250 → 125 | dynamic | 503-degradift | Hidden | — |
| 27 | [505-thermal-duty](05-rad-hard-rampage/05-thermal-duty/) | 05-rad-hard-rampage | data, hardware | 150 → 75 | dynamic | 501-cosmic-bit-blunder | Hidden | — |
| 28 | [601-what-is-this-planet](06-dr-one/01-what-is-this-planet/) | 06-dr-one | network, forensics | 100 → 50 | dynamic | 501-cosmic-bit-blunder | Hidden | 602 |
| 29 | [602-help-me-fly](06-dr-one/02-help-me-fly/) | 06-dr-one | network, forensics | 150 → 75 | dynamic | 601-what-is-this-planet | Hidden | 603 |
| 30 | [603-g-fold](06-dr-one/03-g-fold/) | 06-dr-one | guidance, math | 200 → 100 | dynamic | 602-help-me-fly | Hidden | 604, 901 |
| 31 | [604-ice-vault](06-dr-one/04-ice-vault/) | 06-dr-one | crypto, brute-force | 250 → 125 | dynamic | 603-g-fold | Hidden | 110, 111, 112, 113, 114, 115, 116, 117, 605 |
| 32 | [701-one-light-day](07-unscheduled-passes/01-one-light-day/) | 07-unscheduled-passes | astro, spice, time | 100 → 50 | dynamic | 100-well-hello | Hidden until release | 702 |
| 33 | [702-concatenated](07-unscheduled-passes/02-concatenated/) | 07-unscheduled-passes | radio, fec, dsp | 150 → 75 | dynamic | 701-one-light-day | Hidden | 703 |
| 34 | [703-lagrange-fix](07-unscheduled-passes/03-lagrange-fix/) | 07-unscheduled-passes | astro, navigation, math | 200 → 100 | dynamic | 702-concatenated | Hidden | 704 |
| 35 | [704-dead-chip](07-unscheduled-passes/04-dead-chip/) | 07-unscheduled-passes | reversing, patching | 250 → 125 | dynamic | 703-lagrange-fix | Hidden | 705 |
| 36 | [801-torn-frames](08-silent-carrier/01-torn-frames/) | 08-silent-carrier | forensics, radio, dvb | 100 → 50 | dynamic | 503-degradift | Hidden | 802 |
| 37 | [802-sections-in-the-static](08-silent-carrier/02-sections-in-the-static/) | 08-silent-carrier | forensics, networking, dvb | 150 → 75 | dynamic | 801-torn-frames | Hidden | 803 |
| 38 | [803-frames-inside-frames](08-silent-carrier/03-frames-inside-frames/) | 08-silent-carrier | forensics, protocols, dvb | 200 → 100 | dynamic | 802-sections-in-the-static | Hidden | 804 |
| 39 | [804-lost-sync](08-silent-carrier/04-lost-sync/) | 08-silent-carrier | reversing, protocols, radio | 200 → 100 | dynamic | 803-frames-inside-frames | Hidden | 805 |
| 40 | [805-the-last-carrier](08-silent-carrier/05-the-last-carrier/) | 08-silent-carrier | radio, dsp, signals | 250 → 125 | dynamic | 804-lost-sync | Hidden | — |
| 41 | [901-twenty-two-kilohertz](09-dish-wrangler/01-twenty-two-kilohertz/) | 09-dish-wrangler | radio, hardware, forensics | 100 → 50 | dynamic | 603-g-fold | Hidden | 902 |
| 42 | [902-where-was-it-pointing](09-dish-wrangler/02-where-was-it-pointing/) | 09-dish-wrangler | radio, geometry, osint | 150 → 75 | dynamic | 901-twenty-two-kilohertz | Hidden | 903 |
| 43 | [903-console-backdoor](09-dish-wrangler/03-console-backdoor/) | 09-dish-wrangler | web, forensics | 200 → 100 | dynamic | 902-where-was-it-pointing | Hidden | 904 |
| 44 | [904-gotox-maint](09-dish-wrangler/04-gotox-maint/) | 09-dish-wrangler | reversing, crackme | 200 → 100 | dynamic | 903-console-backdoor | Hidden | 905 |
| 45 | [905-hand-on-the-wheel](09-dish-wrangler/05-hand-on-the-wheel/) | 09-dish-wrangler | crypto, web, reversing | 250 → 125 | dynamic | 904-gotox-maint | Hidden | — |
| 46 | [110-m-type](11-the-pgm-rush/00-m-type/) | 11-the-pgm-rush (bonus) | astro, data, spectroscopy | 100 | standard | 604-ice-vault | Hidden | — |
| 47 | [111-short-arc](11-the-pgm-rush/01-short-arc/) | 11-the-pgm-rush (bonus) | astro, orbit-determination | 150 | standard | 604-ice-vault | Hidden | — |
| 48 | [113-touchdown](11-the-pgm-rush/03-touchdown/) | 11-the-pgm-rush (bonus) | data, guidance, astro | 250 | standard | 604-ice-vault | Hidden | — |
| 49 | [117-the-dark-moonlet](11-the-pgm-rush/07-the-dark-moonlet/) | 11-the-pgm-rush (bonus) | forensics, data, astrobiology | 250 | standard | 604-ice-vault | Hidden | — |
| 50 | [131-two-voices](13-night-shift/01-two-voices/) | 13-night-shift | radio, sdr, lora | 200 → 100 | dynamic | 100-well-hello | Hidden until release | 132 |
| 51 | [132-no-name-on-the-door](13-night-shift/02-no-name-on-the-door/) | 13-night-shift | radio, sdr, lora | 250 → 125 | dynamic | 131-two-voices | Hidden | 133 |
| 52 | [133-hopscotch](13-night-shift/03-hopscotch/) | 13-night-shift | radio, sdr, fhss | 300 → 150 | dynamic | 132-no-name-on-the-door | Hidden | 134 |
| 53 | [134-repacked](13-night-shift/04-repacked/) | 13-night-shift | radio, protocols, data | 300 → 150 | dynamic | 133-hopscotch | Hidden | 135 |
| 54 | [135-what-they-took](13-night-shift/05-what-they-took/) | 13-night-shift | radio, crypto, forensics | 350 → 175 | dynamic | 134-repacked | Hidden | — |
| 55 | [121-channel-hop](12-spectral-forensics/01-channel-hop/) | 12-spectral-forensics | remote-sensing, forensics, lora | 200 → 100 | dynamic | 100-well-hello | Hidden until release | 122 |
| 56 | [122-true-color-is-a-lie](12-spectral-forensics/02-true-color-is-a-lie/) | 12-spectral-forensics | remote-sensing, sdr, lora | 250 → 125 | dynamic | 121-channel-hop | Hidden | 123 |
| 57 | [123-isodata-seven](12-spectral-forensics/03-isodata-seven/) | 12-spectral-forensics | remote-sensing, sdr, lora | 300 → 150 | dynamic | 122-true-color-is-a-lie | Hidden | 124 |
| 58 | [124-subsidy-claim](12-spectral-forensics/04-subsidy-claim/) | 12-spectral-forensics | remote-sensing, gis, sdr | 350 → 175 | dynamic | 123-isodata-seven | Hidden | 125, 126 |
| 59 | [405-happy-bday-d](04-ai-is-not-sci-fi/05-happy-bday-d/) | 04-ai-is-not-sci-fi | ai, llm, edac, forensics | 350 | standard | 404-the-last-kilogram | Hidden | — |
| 64 | [125-where-they-stood](12-spectral-forensics/05-where-they-stood/) | 12-spectral-forensics | radio, gis, forensics | 350 → 175 | dynamic | 124-subsidy-claim | Hidden | — |
| 63 | [126-borrowed-summer](12-spectral-forensics/06-borrowed-summer/) | 12-spectral-forensics | remote-sensing, forensics | 400 → 200 | dynamic | 124-subsidy-claim | Hidden | 127 |
| 66 | [127-heads-down](12-spectral-forensics/07-heads-down/) | 12-spectral-forensics | remote-sensing, sdr, lora | 450 → 225 | dynamic | 126-borrowed-summer | Hidden | — |
| 62 | [112-two-clocks](11-the-pgm-rush/02-two-clocks/) | 11-the-pgm-rush (bonus) | radio, timing, forensics | 200 | standard | 604-ice-vault | Hidden | — |
| 60 | [115-locked-assayer](11-the-pgm-rush/05-locked-assayer/) | 11-the-pgm-rush (bonus) | forensics, embedded, reversing | 300 | standard | 604-ice-vault | Hidden | — |
| 65 | [116-sealed-canister](11-the-pgm-rush/06-sealed-canister/) | 11-the-pgm-rush (bonus) | forensics, embedded, sensors | 300 | standard | 604-ice-vault | Hidden | — |
| 67 | [114-anchor-bite](11-the-pgm-rush/04-anchor-bite/) | 11-the-pgm-rush (bonus) | forensics, filesystems, sensors | 250 | standard | 604-ice-vault | Hidden | — |
| 68 | [605-black-box](06-dr-one/05-black-box/) | 06-dr-one | forensics, embedded, sensors | 300 | standard | 604-ice-vault | Hidden | — |
| 61 | [705-last-readout](07-unscheduled-passes/05-last-readout/) | 07-unscheduled-passes | forensics, radio, reversing | 300 | standard | 704-dead-chip | Hidden | — |
