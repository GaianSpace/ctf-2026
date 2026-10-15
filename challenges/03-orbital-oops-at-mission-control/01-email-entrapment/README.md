# 301-email-entrapment

![301-email-entrapment](art/301-pixel.png)

> It started the way these always do: a friendly email, a document that had to be opened *today*, and an engineer who clicked. By the time anyone noticed, the machine was already talking to strangers. We froze it and pulled a dump of its working memory before powering it down.

Somewhere in that dump is the message that started it. The incident desk is chasing a cached credential it found in the noise and is sure that is the story. It is not the story. The story is the mail that came in dressed as a partner's contract, and the file it carried in with it. Find the mail, pull the attachment back out of it, and open what the engineer opened.

Recover the attachment and read what is inside it.

**Flag format:** `GAIANSPACE{...}`

## Files

- `mem.dmp` — a dump of the engineer's working memory, taken before shutdown

## Hints

- **Dressed as a contract** (cost 30): Ignore the cached password the desk is excited about. Look for the whole mail, headers and all, sitting in the dump as plain text. It knows who it claims to be from.
- **Carried in, not written in** (cost 50): The attachment travels encoded inside the mail, so searching the dump for the answer directly finds nothing. Lift the encoded block out, turn it back into a file, and open that.
