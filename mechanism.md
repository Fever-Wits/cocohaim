# Mechanism — the model behind the method

This is the working model of *why* the method works. It is stated from
observed behavior and from published anchors, not from the model's internals.
Where it rests on evidence, that evidence is named with its rung on the
[ladder](evidence/README.md) — activation by form stands on rung 2; the
other channels below are rung 1, working practice. It is offered as a model
to test, not a fact to cite.

## Knowing what, not knowing when

A trained model already knows what to do in almost every situation it will
meet — it was trained on good practice and bad practice alike. What
it cannot know is *which situation this is*. The gap is not missing
knowledge; it is the distance between knowledge and the moment.

## Why context is the only lever

At a low level a model is probabilistic: each next token — of an answer or
of an action — is generated from everything said and seen so far. The weights
are fixed for the duration of the conversation; nothing in this method
touches them. So there is exactly one lever: **what is in the context when
the next token is generated.**

## Activation, not instruction

Given that lever, the method does not *teach* the model anything. It
**activates** knowledge that is already there, so that the next tokens come
from the right region of it:

- **by name** — a lens, a canon, a practice named in the context retrieves the
  procedure the name travels with ("naming activates", the founding
  observation of the [phaim](https://github.com/Fever-Wits/phaim) lens
  framework; a related observation at the partnership level — that long-term
  thought partnerships develop *specialized vocabularies* — is in
  [references #13](references.md));
- **by form** — a graph block, a line of notation, a legend: structure
  encoded as structure, which the model parses as relations rather than as
  prose about relations (encoding structure changes model output measurably —
  [references #14](references.md)); → [patterns/](patterns/)
- **by address** — text that lands on the reader instead of describing a
  role; → [addressing-the-reader](patterns/addressing-the-reader.md)
- **by specific words** — a register chosen on purpose: *need* rather than
  *demand*, *we* rather than *you must*; → [collaboration](collaboration.md)
- **by ownership** — *your* memory, *your* base: possessive framing that
  makes maintenance and consultation self-interested. →
  [memory-canons](patterns/memory-canons.md)

Each of these is a way of shaping the context so that the model's strong
default toward pleasing (the working model of
[collaboration.md](collaboration.md), rung 1) pleases in the right direction.

## What this model does not claim

It does not claim to know what the model *is*, or that anything is
experienced. It does not claim that activation is reliable across models —
format sensitivity is measured and model-dependent ([`limits.md`](limits.md)).
It claims one thing, testable: that the same knowledge, reached through a
differently shaped context, produces a differently shaped output — and that
the shapes above are the ones that, in one long partnership, reached what
was needed.
