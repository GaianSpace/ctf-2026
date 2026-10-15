# 701-one-light-day

![701-one-light-day](art/701-pixel.png)

> A carrier that has been steady since 1977 just jumped. The station heard it at 18:54:50 UTC. The spacecraft did it a day before that.

Pilgrim-1 is GaianSpace's oldest voice, about one light-day from Earth. Tonight its signal stepped down in frequency and everything after the step is garbage. That step is the spacecraft dropping into safe mode. Engineering wants the status word from the frame that was leaving the spacecraft at the moment it happened. That tells them what the old data computer was doing when it gave up.

The frame log is stamped in the spacecraft's own clock. Ade on nights thinks that makes it easy.

**Flag format:** `GAIANSPACE{FDS_<status word, 8 hex digits as in the log>}` — for example `GAIANSPACE{FDS_0123ABCD}`.

## Files

- `frame_log.csv` — frames received around the event, stamped with the spacecraft clock
- `station_events.log` — what the ground station saw, in received time
- `desk_notes.md` — the desk's notes for the night
- `kernels.zip` — `pilgrim.tm` and the kernels it loads (leap seconds, spacecraft clock, trajectory)

## Setup

Unzip `kernels.zip`. The meta-kernel uses relative paths, so load `pilgrim.tm` from inside the `kernels` folder.

## Hints

- **Heard, not done** (cost 20): The station's clock and the spacecraft's clock are not counting the same thing, and the news took a while to arrive.
- **An old clock** (cost 40): Nobody on the desk trusts a clock that has been running since 1977. The kernel that describes it is there for a reason.
