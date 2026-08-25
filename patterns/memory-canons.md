# memory-canons — maintain · use

**Fires when** — you give a model external memory (files, a database, a memory
tool, RAG) and nothing changes: the store fills, or does not, and the model's
behavior stays the same.

**Form** —

```
external memory = store × maintain-canon × use-canon
        ⊸ any factor at zero → the product is zero
```

The store is what the tools ship. The two canons are what you write:

*Maintain* — the contract for writing:
- before writing, search for the same thing → update it, never birth a twin;
- a contradiction with an existing record is *raised*, not silently appended;
- every record is self-sufficient — a fresh session reads it without guessing
  today's conversation.

*Use* — the contract for reaching:
- when to reach: *before* deciding, not after (memory consulted after the
  decision is decoration);
- how to ask: with the intention, in a sentence — not a bare keyword;
- what to trust: memory answers are leads — verify against the world before
  building on them.

**Example** — live, negative, measured: a 27B model was given two working
memory systems, fully configured, connection tested. Across every session it
made **zero** calls to either — while fluently *talking about* memory, loops
and records it had read about. Speech activates; work does not — unless the
use-canon is part of what it reads. The positive mirror, from the same house,
one line: *learns → records → the next session reads → it activates* — and
that loop, read by the same model, is what moved it to rewrite its own
persistent memory unprompted, twice, correctly.

**Why** — memory vendors ship stores; behavior lives in canons. Without the
maintain-canon the store rots (duplicates, contradictions, stale records —
and trust in it dies first). Without the use-canon the store is a monument:
configured, never consulted. The canons are documents the model reads — so
they are written in the activating forms of this method, not as policy prose.

**Cost / when not**

- The canons live in always-loaded space → they compete with everything else
  there (→ always-loaded-diet). Keep the canon short; keep the mechanics in
  reachable depth.
- Over-proceduralized canons reproduce the excessive-procedure failure:
  a checklist the model walks *instead of* thinking.
- A memory that only one session will ever use does not need canons — plain
  notes beat ceremony.

**Related** — always-loaded-diet (where the canons live) · registers (a canon
can invite: "before you write, ask what already knows this") · line-notation
(the loop above is one).
