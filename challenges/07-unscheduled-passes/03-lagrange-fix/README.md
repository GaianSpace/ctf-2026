# 703-lagrange-fix

![703-lagrange-fix](art/703-pixel.png)

> Pilgrim-1 does not know what time it is. Before the data computer can be patched, the patch has to be timed, and for that the ground needs to know how wrong the spacecraft's clock is.

Decades ago someone gave Pilgrim-1 a receiver for the Solar System Positioning Service: eight beacons parked at the Lagrange points of the outer planets, each shouting the time into the dark. The receiver has been counting on its own since the 2019 fault. Last night it took three snapshots of what it heard and sent them home.

Engineering needs one number: how far the receiver's clock is from true time.

**Flag format:** `GAIANSPACE{CLK_<receiver clock minus TDB, in whole milliseconds, with sign>}` — for example `GAIANSPACE{CLK_-1234}`.

## Files

- `ssps_receiver_log.csv` — the receiver's snapshots: its own clock, and the stamp of each beacon's pulse arriving at that moment
- `ssps_almanac.md` — how the service defines a beacon's position, and this month's bulletins

## Hints

- **A day on the road** (cost 40): Every pulse in the log is about a day old when it arrives. The beacons did not sit still while it travelled.
- **One voice out of tune** (cost 60): Seven of the eight agree with each other. Let the residuals tell you which one does not.
