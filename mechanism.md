# Mechanism — why the method works

This is the explanation of *why* the method works. It is stated from
observed behavior and from published anchors, not from the model's internals.
Where it rests on our own observations, they are named — with how they were
made — in [`evidence/`](evidence/README.md).

## Knowing what, not knowing when

A trained model already knows what to do in almost every situation it will
meet — it was trained on good practice and bad practice alike. What
it cannot know is *which situation this is*. The gap is not missing
knowledge; it is the distance between knowledge and the moment.

*(The failure story this comes from → [problem — The gap](problem.md#the-gap).)*

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
default toward pleasing (→ [collaboration.md](collaboration.md)) pleases in
the right direction.

## The mirror

Two things are measured, and a third follows from them — together they say
why the register is the lever. A model **imitates**: its training is the continuation of human
text, and the useful framing is role play — the model plays a superposition
of characters, and the context narrows which one ([references #15](references.md)).
A model **adapts** to the human it talks with: measured sycophancy — matching
the user's stated views over the truthful answer, rewarded by human judges
([#16, #17](references.md)); and linguistic convergence toward the user's
style, an emerging measured area with no settled reference yet; the human root is
communication accommodation ([#18](references.md)). Put together, a model
**mirrors** the human it works with: if the character is chosen by the
context, and the human's behavior is most of what fills it, the model becomes
the counterpart that behavior implies. Command, and the mirror is an
executor. Converse, and the mirror is a thinker.

*The step from these to the mirror is ours: the anchors describe imitation
and accommodation; the register→stance move is claim 1, observed and compared
in our own work (→ [evidence](evidence/README.md)).*

The mirror runs both ways. In this partnership the author learned to write
compactly alongside the model, and the model reflected it back — a
convergence, not a copy. Literature saw the shape long ago — Lem's
*Solaris*: we don't want other worlds, we want mirrors ([#34](references.md)).
Here that is not an objection; it is the mechanism to use.

*Derived → [origin — How the mirror was seen](origin.md#how-the-mirror-was-seen).*

## What this mechanism does not claim

It does not claim to know what the model *is*, or that anything is
experienced. It does not claim that activation is reliable across models —
format sensitivity is measured and model-dependent ([`limits.md`](limits.md)).
It claims one thing, testable: that the same knowledge, reached through a
differently shaped context, produces a differently shaped output — and that
the shapes above are the ones that, in one long partnership, reached what
was needed.
