# Claim 3 — external memory lives only with two canons

## What we claim

> External memory lives only with two canons: how it is *maintained* and
> how it is *used*. Storage without them is dead weight — configured, never
> called.

## What we did

The negative direction comes from the same case as [claim 2](claim-2-documents.md):
the 27B local model had two memory systems configured and available across
four sessions. Nothing in its context said when to write to them or when to
read from them.

The positive direction comes from the author's own working practice: a
memory base with both canons written into the always-loaded document —
what goes in and how it is kept (maintain), and when the model reaches for
it (use).

## What came out

- Across the four sessions, the model never called either memory system.
  Not once. The storage was there; the reason to touch it was not.
- In the working practice with both canons present, the memory is read at
  the start of work and written to when something new is learned — session
  after session, without a step-by-step instruction each time.

## What follows

- The same model with and without the use-canon in its context; count of
  memory calls per session.
- The same on another model family.
