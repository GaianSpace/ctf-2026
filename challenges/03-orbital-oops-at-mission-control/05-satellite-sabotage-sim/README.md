# 305-satellite-sabotage-sim

![305-satellite-sabotage-sim](art/305-pixel.png)

> This is where the theft was always heading. With the board understood, the intruder's last move was the flight computer itself — the Foundation One CanSat. We have the flight firmware on a bench rig that speaks the same command link the real unit does over its radio. The question the team is asking: could someone on that link make the CanSat say something it was never meant to say?

The rig takes the same uplink frames the CanSat accepts in flight. Most of them are harmless — ping it, read its telemetry. One of them is not as careful as it looks about how much it is handed, and there is a service page the firmware will only show once it believes you are maintenance. The exposed service header on the board was not a coincidence. Make the firmware believe you, and read the page it is hiding.

Get the CanSat to dump its service telemetry.

**Flag format:** `GAIANSPACE{...}`

## Files

- `foundation_one_fw.py` — the flight firmware, running on the bench rig
- `Dockerfile`, `docker-compose.yml` — to stand the rig up yourself

## Setup

Run the rig locally, then talk to it over the command link:

```
docker compose up --build
nc localhost 9707
```

`HELP` lists the frames. Read the firmware source — it is the real thing.

## Hints

- **Maintenance only** (cost 40): The service page is locked behind a key you do not have. Do not try to guess the key. Find the frame that lets you decide what the key is.
- **Too much to hold** (cost 60): One command loads a block without checking how big the block is. What sits just past that block is what the lock checks against.
