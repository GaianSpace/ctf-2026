# 207-lost-signal-to-mars

![207-lost-signal-to-mars](art/207-pixel.png)

> A listening post that usually eavesdrops on satellites just a few thousand kilometres up was pointed, for once, at something very far away. It came back with a file that every meter on the rack calls empty. There is a message in it. The distance just buried it, and the sender was clever about how it keyed it.

Close in, a downlink is loud and you read it on the first pass. This was not close in. The sender is so far off that one copy of its message is weaker than the noise sitting on top of it, so it says the same thing again, and again, and again, and trusts the far end to be patient. And it does not spell with loud-and-quiet, which would be easy to fake across that much noise; it spells with *change and no-change*, so a single stolen glance tells you nothing even after you clean it up. Reyes looked at one slice, saw snow, and moved on.

Recover what the distant transmitter kept repeating.

**Flag format:** `GAIANSPACE{...}`

## Files

- `deep_space_capture.f32` — the raw recording from the post
- `beacon_notes.md` — the operator's settings for the capture

## Hints

- **Find the beat** (cost 30): The burst repeats on a fixed stride, but nothing tells you the stride. Let the recording line up against a shifted copy of itself and the stride will show.
- **Changes, not levels** (cost 50): Once the repeats are stacked and the noise is gone, do not read the levels. Read where the signal flips and where it holds. One of those is a one.
