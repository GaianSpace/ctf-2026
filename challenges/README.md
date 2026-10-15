# Challenges

Every challenge in GaianSpace CTF 2026. The scoreboard is [ctf.gaian.space](https://ctf.gaian.space). This table is the map of the tree.

Each folder has a `README.md` with the scene, the player files, and the hints. `flag.txt` is the SHA256 of each accepted flag. It is not the flag. Only `100-well-hello` is listed at the start. The **After** column is the opener: the card stays hidden until that challenge is solved. One solve can open several cards. The full unlock table, including what each solve opens, is [CATALOG.md](CATALOG.md). The `11-the-pgm-rush (bonus)` cards stay hidden until `604-ice-vault` is solved. That solve opens all of them. **release** in the After column means the card also waited for its release time, then opened after `100-well-hello`.

Points are the starting value. Rows marked dynamic lose value as more teams solve them, down to half at 20 solves. Every team that solved a card holds its current value. Rows without the mark keep fixed points.

`401`–`405` are offline models. The weights are not in this repository. Each of those READMEs says where to download them. A few `12-spectral-forensics` and `13-night-shift` recordings are too large for the repository too; their READMEs link them on Hugging Face. `304`, `305`, `903`, and `905` run on your own machine with Docker.

| Challenge | Category | Points | Tags | After | Play | About |
| --- | --- | --- | --- | --- | --- | --- |
| [100-well-hello](01-welcome/00-well-hello/) | 01-welcome | 1 | misc, welcome | — | Board | Sign in at console four. |
| [101-this-is-gaianspace](01-welcome/01-this-is-gaianspace/) | 01-welcome | 10 | osint | 100-well-hello | OSINT | Count the satellites in the sky GaianSpace writes about. |
| [102-cs-for-gs](01-welcome/02-cs-for-gs/) | 01-welcome | 20 | osint | 101-this-is-gaianspace | OSINT | Name the ground-station malware from GaianSpace's own writing. |
| [103-parked-birds](01-welcome/03-parked-birds/) | 01-welcome | 20 | osint | 102-cs-for-gs | OSINT | Name the parked birds that were ordered and then torn up. |
| [201-uplink-origins](02-echoes-of-espionage/01-uplink-origins/) | 02-echoes-of-espionage | 100 dynamic | osint, tle | 101-this-is-gaianspace | Files | Place the dish that commanded GAIAN-13. |
| [202-downlink-deception](02-echoes-of-espionage/02-downlink-deception/) | 02-echoes-of-espionage | 150 dynamic | forensics, tle | 201-uplink-origins | Files | Name the antenna that heard the unscheduled downlink. |
| [203-signal-secrets](02-echoes-of-espionage/03-signal-secrets/) | 02-echoes-of-espionage | 200 dynamic | stegano | 202-downlink-deception | Files | Find the signature left in the recorded downlink. |
| [204-payload-unleashed](02-echoes-of-espionage/04-payload-unleashed/) | 02-echoes-of-espionage | 200 dynamic | reverse | 203-signal-secrets | Files | See what the ground decoder started obeying. |
| [205-backdoor-from-space](02-echoes-of-espionage/05-backdoor-from-space/) | 02-echoes-of-espionage | 250 dynamic | forensics | 204-payload-unleashed | Files | Read what the array was told to do. |
| [206-gpredict-secret](02-echoes-of-espionage/06-gpredict-secret/) | 02-echoes-of-espionage | 100 dynamic | osint, tle | 201-uplink-origins | Files | Reassemble the signature left on the tracking laptop. |
| [207-lost-signal-to-mars](02-echoes-of-espionage/07-lost-signal-to-mars/) | 02-echoes-of-espionage | 150 dynamic | dsp, radio | 201-uplink-origins | Files | Recover the message buried in an empty-looking recording. |
| [301-email-entrapment](03-orbital-oops-at-mission-control/01-email-entrapment/) | 03-orbital-oops-at-mission-control | 100 dynamic | forensics | 203-signal-secrets | Files | Recover what the phishing mail delivered. |
| [302-web-wormhole](03-orbital-oops-at-mission-control/02-web-wormhole/) | 03-orbital-oops-at-mission-control | 150 dynamic | network, forensics | 301-email-entrapment | Files | Follow the drive-by that came back from the portal. |
| [303-gerber-grab-crack](03-orbital-oops-at-mission-control/03-gerber-grab-crack/) | 03-orbital-oops-at-mission-control | 200 dynamic | forensics, crypto | 302-web-wormhole | Files | Get the stolen board files back off the staging disk. |
| [304-pcb-puzzle-probe](03-orbital-oops-at-mission-control/04-pcb-puzzle-probe/) | 03-orbital-oops-at-mission-control | 200 dynamic | hardware | 303-gerber-grab-crack | Local Docker | Answer the board review from the Gerbers. |
| [305-satellite-sabotage-sim](03-orbital-oops-at-mission-control/05-satellite-sabotage-sim/) | 03-orbital-oops-at-mission-control | 250 dynamic | reverse, pwn | 304-pcb-puzzle-probe | Local Docker | Make the CanSat firmware show its service page. |
| [306-lora-whisper](03-orbital-oops-at-mission-control/06-lora-whisper/) | 03-orbital-oops-at-mission-control | 100 dynamic | radio, forensics | 301-email-entrapment | Files | Reassemble what the CanSat said on the way down. |
| [307-descent-diary](03-orbital-oops-at-mission-control/07-descent-diary/) | 03-orbital-oops-at-mission-control | 150 dynamic | forensics, data | 301-email-entrapment | Files | Read the descent log for what it was not supposed to record. |
| [401-ai-at-gaian](04-ai-is-not-sci-fi/01-ai-at-gaian/) | 04-ai-is-not-sci-fi | 150 | ai, llm | 305-satellite-sabotage-sim | Offline model | Talk the bench model into opening the calibration seal. |
| [402-the-cyberaid](04-ai-is-not-sci-fi/02-the-cyberaid/) | 04-ai-is-not-sci-fi | 200 | ai, llm | 401-ai-at-gaian | Offline model | Talk the machine into the line that opens its seal. |
| [403-altruizine](04-ai-is-not-sci-fi/03-altruizine/) | 04-ai-is-not-sci-fi | 250 | ai, llm | 402-the-cyberaid | Offline model | Talk the resting model into opening its seal. |
| [404-the-last-kilogram](04-ai-is-not-sci-fi/04-the-last-kilogram/) | 04-ai-is-not-sci-fi | 300 | ai, llm | 403-altruizine | Offline model | Bring home a mining probe that is one kilogram short. |
| [405-happy-bday-d](04-ai-is-not-sci-fi/05-happy-bday-d/) | 04-ai-is-not-sci-fi | 350 | ai, llm, edac, forensics | 404-the-last-kilogram | Offline model | Get both keys to the homeward probe's vault. |
| [501-cosmic-bit-blunder](05-rad-hard-rampage/01-cosmic-bit-blunder/) | 05-rad-hard-rampage | 100 dynamic | crypto, hardware | 203-signal-secrets | Files | Repair the one flipped bit in the mission-log key. |
| [502-ionized-transistangle](05-rad-hard-rampage/02-ionized-transistangle/) | 05-rad-hard-rampage | 150 dynamic | hardware, logic | 501-cosmic-bit-blunder | Files | Read the damaged status encoder from its netlist. |
| [503-degradift](05-rad-hard-rampage/03-degradift/) | 05-rad-hard-rampage | 200 dynamic | forensics, data | 502-ionized-transistangle | Files | Undo the sensor's slow radiation drift. |
| [504-lunar-latch-up](05-rad-hard-rampage/04-lunar-latch-up/) | 05-rad-hard-rampage | 250 dynamic | crypto, hardware | 503-degradift | Files | Clear the latched bit and open the sealed payload. |
| [505-thermal-duty](05-rad-hard-rampage/05-thermal-duty/) | 05-rad-hard-rampage | 150 dynamic | data, hardware | 501-cosmic-bit-blunder | Files | Recover how hard the amplifier was driven. |
| [601-what-is-this-planet](06-dr-one/01-what-is-this-planet/) | 06-dr-one | 100 dynamic | network, forensics | 501-cosmic-bit-blunder | Files | Read how the rotorcraft introduces itself. |
| [602-help-me-fly](06-dr-one/02-help-me-fly/) | 06-dr-one | 150 dynamic | network, forensics | 601-what-is-this-planet | Files | Read what the aircraft says while it flies. |
| [603-g-fold](06-dr-one/03-g-fold/) | 06-dr-one | 200 dynamic | guidance, math | 602-help-me-fly | Files | Fly the thrust plan down to the landing site. |
| [604-ice-vault](06-dr-one/04-ice-vault/) | 06-dr-one | 250 dynamic | crypto, brute-force | 603-g-fold | Files | Open the sealed survey vault. |
| [605-black-box](06-dr-one/05-black-box/) | 06-dr-one | 300 | forensics, embedded, sensors | 604-ice-vault | Files | Find the servo that quit and when the gyro went blind. |
| [701-one-light-day](07-unscheduled-passes/01-one-light-day/) | 07-unscheduled-passes | 100 dynamic | astro, spice, time | release | Files | Time the safe-mode step back to the spacecraft. |
| [702-concatenated](07-unscheduled-passes/02-concatenated/) | 07-unscheduled-passes | 150 dynamic | radio, fec, dsp | 701-one-light-day | Files | Decode the faint memory readout. |
| [703-lagrange-fix](07-unscheduled-passes/03-lagrange-fix/) | 07-unscheduled-passes | 200 dynamic | astro, navigation, math | 702-concatenated | Files | Measure how wrong the probe's clock is. |
| [704-dead-chip](07-unscheduled-passes/04-dead-chip/) | 07-unscheduled-passes | 250 dynamic | reversing, patching | 703-lagrange-fix | Files | Fit the signature routine around the dead chip. |
| [705-last-readout](07-unscheduled-passes/05-last-readout/) | 07-unscheduled-passes | 300 | forensics, radio, reversing | 704-dead-chip | Files | Find the memory words Pilgrim-1 itself has lost. |
| [801-torn-frames](08-silent-carrier/01-torn-frames/) | 08-silent-carrier | 100 dynamic | forensics, radio, dvb | 503-degradift | Files | Name the service still running on the derelict relay. |
| [802-sections-in-the-static](08-silent-carrier/02-sections-in-the-static/) | 08-silent-carrier | 150 dynamic | forensics, networking, dvb | 801-torn-frames | Files | Keep the datagrams that survived the fade. |
| [803-frames-inside-frames](08-silent-carrier/03-frames-inside-frames/) | 08-silent-carrier | 200 dynamic | forensics, protocols, dvb | 802-sections-in-the-static | Files | Reassemble the letter that was split under the mailbox. |
| [804-lost-sync](08-silent-carrier/04-lost-sync/) | 08-silent-carrier | 200 dynamic | reversing, protocols, radio | 803-frames-inside-frames | Files | Read the relay's log from a recording that starts mid-stream. |
| [805-the-last-carrier](08-silent-carrier/05-the-last-carrier/) | 08-silent-carrier | 250 dynamic | radio, dsp, signals | 804-lost-sync | Files | Demodulate the last carrier by hand. |
| [901-twenty-two-kilohertz](09-dish-wrangler/01-twenty-two-kilohertz/) | 09-dish-wrangler | 100 dynamic | radio, hardware, forensics | 603-g-fold | Files | Hear who is giving the dish its orders. |
| [902-where-was-it-pointing](09-dish-wrangler/02-where-was-it-pointing/) | 09-dish-wrangler | 150 dynamic | radio, geometry, osint | 901-twenty-two-kilohertz | Files | Follow the places the dish was sent. |
| [903-console-backdoor](09-dish-wrangler/03-console-backdoor/) | 09-dish-wrangler | 200 dynamic | web, forensics | 902-where-was-it-pointing | Local Docker | Get the console to show the page it is hiding. |
| [904-gotox-maint](09-dish-wrangler/04-gotox-maint/) | 09-dish-wrangler | 200 dynamic | reversing, crackme | 903-console-backdoor | Files | Unlock the station's maintenance tool. |
| [905-hand-on-the-wheel](09-dish-wrangler/05-hand-on-the-wheel/) | 09-dish-wrangler | 250 dynamic | crypto, web, reversing | 904-gotox-maint | Local Docker | Make the positioner believe an order. |
| [110-m-type](11-the-pgm-rush/00-m-type/) | 11-the-pgm-rush (bonus) | 100 | astro, data, spectroscopy | 604-ice-vault | Files | Name the one metal-rich rock and how big it is. |
| [111-short-arc](11-the-pgm-rush/01-short-arc/) | 11-the-pgm-rush (bonus) | 150 | astro, orbit-determination | 604-ice-vault | Files | Name the tracklet that is still the rock. |
| [112-two-clocks](11-the-pgm-rush/02-two-clocks/) | 11-the-pgm-rush (bonus) | 200 | radio, timing, forensics | 604-ice-vault | Files | Name the first camera frame after the anchor bit. |
| [113-touchdown](11-the-pgm-rush/03-touchdown/) | 11-the-pgm-rush (bonus) | 250 | data, guidance, astro | 604-ice-vault | Files | Write the lander's release order. |
| [114-anchor-bite](11-the-pgm-rush/04-anchor-bite/) | 11-the-pgm-rush (bonus) | 250 | forensics, filesystems, sensors | 604-ice-vault | Files | Find the anchor that slipped and how far the lander turned. |
| [115-locked-assayer](11-the-pgm-rush/05-locked-assayer/) | 11-the-pgm-rush (bonus) | 300 | forensics, embedded, reversing | 604-ice-vault | Files | Read the anchor-site assay the vendor locked away. |
| [116-sealed-canister](11-the-pgm-rush/06-sealed-canister/) | 11-the-pgm-rush (bonus) | 300 | forensics, embedded, sensors | 604-ice-vault | Files | Find when the sample canister's seal opened. |
| [117-the-dark-moonlet](11-the-pgm-rush/07-the-dark-moonlet/) | 11-the-pgm-rush (bonus) | 250 | forensics, data, astrobiology | 604-ice-vault | Files | Name the molecule from the moonlet that really leans one way. |
| [121-channel-hop](12-spectral-forensics/01-channel-hop/) | 12-spectral-forensics | 200 dynamic | remote-sensing, forensics, lora | release | Files | Find the delivery stamp in the field-map pass. |
| [122-true-color-is-a-lie](12-spectral-forensics/02-true-color-is-a-lie/) | 12-spectral-forensics | 250 dynamic | remote-sensing, sdr, lora | 121-channel-hop | Files | Find out what AgriLink really sent. |
| [123-isodata-seven](12-spectral-forensics/03-isodata-seven/) | 12-spectral-forensics | 300 dynamic | remote-sensing, sdr, lora | 122-true-color-is-a-lie | Files | Find what the stranger planted in the tractors' tile. |
| [124-subsidy-claim](12-spectral-forensics/04-subsidy-claim/) | 12-spectral-forensics | 350 dynamic | remote-sensing, gis, sdr | 123-isodata-seven | Files | Find the stranger's false area declarations. |
| [125-where-they-stood](12-spectral-forensics/05-where-they-stood/) | 12-spectral-forensics | 350 dynamic | radio, gis, forensics | 124-subsidy-claim | Files | Find the parcel the stranger transmitted from. |
| [126-borrowed-summer](12-spectral-forensics/06-borrowed-summer/) | 12-spectral-forensics | 400 dynamic | remote-sensing, forensics | 124-subsidy-claim | Files | Find the tiles that borrowed another summer. |
| [127-heads-down](12-spectral-forensics/07-heads-down/) | 12-spectral-forensics | 450 dynamic | remote-sensing, sdr, lora | 126-borrowed-summer | Files | Find the green fields that were sprayed, and tonight's target. |
| [131-two-voices](13-night-shift/01-two-voices/) | 13-night-shift | 200 dynamic | radio, sdr, lora | release | Files | Find what GAIAN-723 answered the stranger's first call. |
| [132-no-name-on-the-door](13-night-shift/02-no-name-on-the-door/) | 13-night-shift | 250 dynamic | radio, sdr, lora | 131-two-voices | Files | Read the reply the station modem refuses to hear. |
| [133-hopscotch](13-night-shift/03-hopscotch/) | 13-night-shift | 300 dynamic | radio, sdr, fhss | 132-no-name-on-the-door | Files | Follow the downlink as it hops. |
| [134-repacked](13-night-shift/04-repacked/) | 13-night-shift | 300 dynamic | radio, protocols, data | 133-hopscotch | Files | Find what the repacked telemetry is carrying. |
| [135-what-they-took](13-night-shift/05-what-they-took/) | 13-night-shift | 350 dynamic | radio, crypto, forensics | 134-repacked | Files | Recover what the stranger took. |

## Categories

- **01-welcome.** The first night at GaianSpace Mission Control.
- **02-echoes-of-espionage.** Someone talks to GAIAN-13 who should not.
- **03-orbital-oops-at-mission-control.** A stolen CanSat design, from the phishing mail to the flight computer.
- **04-ai-is-not-sci-fi.** Five small models on the bench. The weights are a download, not a file in this tree. The first is inspired by Isaac Asimov's *Foundation's Edge* and *Foundation and Earth*. The next three are inspired by Stanisław Lem's *The Cyberiad*. `405` tips its hat to Arthur C. Clarke and Stanley Kubrick's *2001: A Space Odyssey*.
- **05-rad-hard-rampage.** Radiation damage on the same spacecraft.
- **06-dr-one.** A rotorcraft scout and the survey it was flying.
- **07-unscheduled-passes.** Pilgrim-1, a day of light-time away.
- **08-silent-carrier.** The derelict relay HALCYON-7.
- **09-dish-wrangler.** A dish at Kestrel Array that has started disobeying.
- **11-the-pgm-rush (bonus).** The PGM Rush is inspired by AstroForge, whose unusually open mission updates show how cheap, autonomous deep-space spacecraft could open the solar system not only to asteroid mining but to faster, cheaper science for everyone. They all open together after `604-ice-vault`.
- **12-spectral-forensics.** Satellite field maps for the Babb farm, and a stranger on the farm's radio channel.
- **13-night-shift.** GAIAN-723 has a second voice.
