# handle-with-care — one sentence before the fragile work

**When to reach for it** — you hand the model work where a mistake is
expensive — a live system, someone's memory, code that must not change
behavior — and you want careful handling, not fearful checking.

**Form** — one short sentence before the facts, naming that what follows is
delicate. Then the facts. Not a list of what could break.

**Example** — live, translated from a working session, handing over the
rebuild of the memory server's core:

> And here comes the delicate part. memdex is the server that holds the
> memory, and it has grown into one big file. It must become modular.
> There is a plan.

What followed: the model read the plan, said back its understanding, and
stopped to confirm before touching anything; in two days of work the live
memory was never touched outside the safe paths.

**Why it works** — the model shapes what it does from what stands in front
of it. A list of warnings puts fear in front of it: it starts guarding
against the list, and against nothing else. One sentence naming the work as
delicate puts care in front of it — and the care colors every step after,
including the ones no list would have covered.

**Cost, and when not**

- **It must be true.** Mark trivial work as delicate and the word wears out.
- **It does not replace the hard rules** — the sentence sets the handling;
  the few rules where no choice is allowed still stand on their own.
  (→ hard-canons)
- Effects are model-dependent — verify on yours.

**Related** — [registers](registers.md) (the same axis — what you want
back — applied to safety) · [hard-canons](hard-canons.md) (what this
pattern does not replace).
