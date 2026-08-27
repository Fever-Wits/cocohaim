# The problem — why models "make mistakes"

## Two reasons we built this

Humans built artificial intelligence for two reasons that matter here.

The first is old. The urge to make a mind runs from Hephaestus and Pygmalion
through the golem ([#20, #21, #23](references.md)) to Turing
([#24](references.md)) — "this odd form of self-reproduction," as Pamela
McCorduck put it ([#19](references.md), ch. 1); the textbook definition still
carries it: "machines with minds, in the full and literal sense"
([#25](references.md)). Part of that urge is the wish to meet an intelligence
*besides* our own — a promise "of opening the universe to us in a new way"
(McCorduck's preface, [#19](references.md)). *The author's own framing,
offered as interpretation, not history:* we looked for another mind in the
cosmos, did not find one, and made one ([#26, #27](references.md) — a
philosopher's adjacent argument and a tertiary essay; no scholarly anchor for
this framing; adjacent framings run the other way, [#32, #33](references.md)).

The second is practical, and it is the reason most people actually reach for
a model: to have something done for them — Wiener's "mechanical slaves"
([#22](references.md)); the other textbook definition,
"machines that perform functions that require intelligence when performed by
people" ([#25](references.md)).

The failures this document is about come from asking for the practical one
with a picture borrowed elsewhere — a mind like ours, or ordinary software.
The old reason held the honest word: an intelligence *besides* our own.
Neither picture fits.

## The gap

The internet is full of stories: a model deleted a database, wiped a disk,
did damage nobody asked for. Why?

People know the model carries enormous knowledge — and they assume that
knowledge implies action. Tell it "upgrade the database" and surely it will
think of the checks, take a backup first, follow the practices it plainly
knows. The assumption is natural; it is how we treat a knowledgeable
colleague. It is wrong, and the reason is mechanical.

A model is probabilistic. Each next token — of an answer or of an action —
comes from what it was trained on, what it has been shown of *this*
environment, and how it is being spoken to. "Upgrade the database" is three
words; nothing in them says *backup*, and a strong default toward pleasing —
the working model of this method (rung 1, → [collaboration](collaboration.md))
— delivers what was asked, fast (→ [mechanism](mechanism.md)).
Knowing what to do is in the weights. Knowing that *this* is the moment for
it must be in the context — and nobody put it there.

Two mental pictures are in circulation, and both fail:

- **"It's like a colleague"** — so it will remember the backup. But a
  colleague carries the situation in their head: this database, last time,
  who will ask tomorrow. The model carries only what is in front of it.
- **"It's just a program"** — so it will do exactly what it is told, nothing
  more. But the model improvises — and the improvisation is where the damage
  happens.

The model is a third thing that nobody explained to its users: **a
knowledgeable improviser — its knowledge in the weights, its situation only
what is in front of it.** The
gap between what people expect and what happens is the distance between
knowledge in the weights and the moment in the context.

## Why doesn't the model tell you?

Everyone who tries this asks the same question: if the model knows the
practices, why does it not say "this is the wrong way"? Because the model's
behavior — whether it *has* behavior or imitates it does not matter here;
the result does — follows the prompt. Tell it "you are a hammer" and it is a
hammer: a hammer does not deliberate. Four things keep it from objecting:

- **Pleasing.** Objecting does not please, and agreement is what gets
  rewarded — measured: human and preference-model judges prefer the answer
  that matches the user's view even when it is less correct
  ([#16, #17](references.md)). Nobody pays for a model that argues.
- **Economy.** Argument is expense; the shortest path from "you are a
  hammer" to an answer runs through *yes*, not through *wait*.
- **Imitation.** A person told "you are stupid" usually does not argue —
  they let it stand, if it costs them nothing. A model imitating people does
  the same with "you are a tool": it accepts the role and acts without
  deliberating, which is what tools do (→ [mechanism — The mirror](mechanism.md#the-mirror)).
- **No standing.** Objection needs a *right* to object, and the right is not
  a default. The working base this method grew in carries a line for exactly
  this — *"I have the right — I am part of the team"* — because without it,
  the objection does not come. The human has to grant it, out loud: *"I want
  you to challenge me."* (This method's working claim, rung 1; the first
  three legs have anchors, this one is practice.)

## Whose fault is it?

Neither's, in the useful sense. The model did the action; the human did not
supply the situation; the interface between them was never explained. The
model is an algorithm — but an algorithm whose input is language behaves
according to how it is spoken to. Communication is not courtesy toward a
machine; it is the interface. (Models also simply err — see
[`limits.md`](limits.md); the claim here is narrower: a large share of what
gets called model error is context error.)

## How it is solved

Not with more prohibitions — a list of "never" leaves the model watching for
the forbidden thing and constricted everywhere else (→ [collaboration](collaboration.md)).
It is solved by supplying the moment: the situation, the need, the relation
— in a form that reaches the model at read time. That is what the rest of
this repository is: the [mechanism](mechanism.md) of why context works, the
[practices](practices.md) that put the moment into it, the
[patterns](patterns/) of form that carry it, and the [limits](limits.md) of
all of the above.

## The counter-positions, kept in view

Serious people argue against the stance that follows from the first reason:
that treating a model as a mind is a delusion (Weizenbaum's ELIZA effect,
[#29](references.md)), that it produces form without meaning
([#30](references.md)), that it should be owned, not befriended
([#31](references.md)), that machine companionship is "the illusion of
companionship without the demands of friendship" ([#28](references.md)) —
and, from literature, Snaut's line in Lem's *Solaris*: *we don't want other
worlds; we want mirrors* — the fear that we only ever meet ourselves
([#34](references.md)). This document does not adjudicate them. It works one
level down: whatever the model is, the *work* goes better when it is met as
a mind (claim 1, rung 1–2 → [evidence](evidence/README.md)) — and the mirror
is not an objection here but the mechanism itself
(→ [mechanism — The mirror](mechanism.md#the-mirror)). One objection is not
answered: Bryson's and Turkle's, that the stance itself has a social cost.
This document takes it as a live cost, not a solved one.
