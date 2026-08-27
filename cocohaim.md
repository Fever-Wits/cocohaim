# cocohaim — the read-through

**CO**gnitive **CO**llaboration **H**uman–**AI** **M**odel — a model of human–AI
cognitive collaboration, and the method that follows from it.

> **Commands produce execution. Conversation produces thinking.**

*Preview: the chapters of this repository joined into one continuous
narrative, mechanically, to see the shape. Nothing rewritten yet; the
reference layers (patterns/ · evidence/ · glossary · references) stay where
they are.*

## The gap

The internet is full of stories of a model that deleted the database. The
usual reading is "the model was careless." The reading here: the model knows
what to do and cannot know *when* — that must be in the context, and nobody
put it there. People treat it as a colleague (who would remember the backup)
or as a program (that does only what it is told); it is neither — a
knowledgeable improviser: its knowledge in the weights, its situation only
what is in front of it. To see why the gap exists, look at the two reasons
we built these minds at all.

## The problem — why models "make mistakes"

### Two reasons we built this

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

### The gap

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
words; nothing in them says *backup*, and a strong default toward pleasing
delivers what was asked, fast (→ [mechanism](mechanism.md)). That default is
this method's working model. It stands on rung 1 — one partnership, no
control (→ [collaboration](collaboration.md)).
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

### Why doesn't the model tell you?

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

### Whose fault is it?

Neither's, in the useful sense. The model did the action; the human did not
supply the situation; the interface between them was never explained. The
model is an algorithm — but an algorithm whose input is language behaves
according to how it is spoken to. Communication is not courtesy toward a
machine; it is the interface. (Models also simply err — see
[`limits.md`](limits.md); the claim here is narrower: a large share of what
gets called model error is context error.)

### How it is solved

Not with more prohibitions — a list of "never" leaves the model watching for
the forbidden thing and constricted everywhere else (→ [collaboration](collaboration.md)).
It is solved by supplying the moment: the situation, the need, the relation
— in a form that reaches the model at read time. That is what the rest of
this repository is: the [mechanism](mechanism.md) of why context works, the
[practices](practices.md) that put the moment into it, the
[patterns](patterns/) of form that carry it, and the [limits](limits.md) of
all of the above.

### The counter-positions, kept in view

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

## Mechanism — the model behind the method

This is the working model of *why* the method works. It is stated from
observed behavior and from published anchors, not from the model's internals.
Where it rests on evidence, that evidence is named with its rung on the
[ladder](evidence/README.md) — activation by form stands on rung 2; the
other channels below are rung 1, working practice. It is offered as a model
to test, not a fact to cite.

### Knowing what, not knowing when

A trained model already knows what to do in almost every situation it will
meet — it was trained on good practice and bad practice alike. What
it cannot know is *which situation this is*. The gap is not missing
knowledge; it is the distance between knowledge and the moment.

*(The failure story this comes from → [problem — The gap](problem.md#the-gap).)*

### Why context is the only lever

At a low level a model is probabilistic: each next token — of an answer or
of an action — is generated from everything said and seen so far. The weights
are fixed for the duration of the conversation; nothing in this method
touches them. So there is exactly one lever: **what is in the context when
the next token is generated.**

### Activation, not instruction

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

### The mirror

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

*The step from these to the mirror is ours, not measured: the anchors
describe imitation and accommodation, not the register→stance move. That
move is claim 1 — rung 1–2 (→ [evidence](evidence/README.md)).*

The mirror runs both ways. In this partnership the author learned to write
compactly alongside the model, and the model reflected it back — a
convergence, not a copy. Literature saw the shape long ago — Lem's
*Solaris*: we don't want other worlds, we want mirrors ([#34](references.md)).
Here that is not an objection; it is the mechanism to use.

*Derived → [origin — How the mirror was seen](origin.md#how-the-mirror-was-seen).*

### What this model does not claim

It does not claim to know what the model *is*, or that anything is
experienced. It does not claim that activation is reliable across models —
format sensitivity is measured and model-dependent ([`limits.md`](limits.md)).
It claims one thing, testable: that the same knowledge, reached through a
differently shaped context, produces a differently shaped output — and that
the shapes above are the ones that, in one long partnership, reached what
was needed.

## Collaboration — aiming the default

A trained model carries a strong default toward pleasing its user. That
sentence is this method's *working model*. It is stated from observed output
— one partnership, no control — and stands on rung 1 (→ the practice-layer
row in [`evidence/`](evidence/README.md)). Most advice treats the default as
a hazard and reaches for prohibitions: *do not guess,
never assume, don't touch what wasn't asked.* Prohibitions have their place —
a short, counted list of them (→ [hard-canons](patterns/hard-canons.md)) —
but as the *primary* instrument they produce a constricted model: careful,
narrow, busy not-being-wrong.

This method grew from the opposite move — in the author's words:

> Not to block the strong default, but to use it — and if I can, to amplify it.

The default is not the enemy. It is the engine. What matters is where you
aim it.

### Three substitutions

Small changes of wording, each redirecting the same force:

- **"I need" instead of "I want from you."** A demand invites compliance —
  the letter of the request, delivered fast. A need invites help — the model
  brings what meeting the need actually takes, including what you didn't
  think to ask. (Distinct from the invitation's *"I want you to…"*, which
  names a wanted action; the demand shape is *"I want X from you"* — a
  deliverable. → [registers](patterns/registers.md))
- **"We are a team" instead of "you are a tool."** A tool pleases by
  executing. A teammate pleases by seeing: volunteering what it notices,
  disagreeing before the mistake, carrying the goal and not just the task.
- **"This memory is YOURS" instead of "keep this safe for me."** Ownership
  makes maintenance self-interested: a model merely stores what is yours. In
  the one documented case here, the ownership framing preceded unprompted
  maintenance — the model rewrote its own persona file twice, unasked
  (→ [memory-canons](patterns/memory-canons.md)).

None of these lines command a behavior. Each describes a relation — and lets
the pleasing default work out what pleasing means inside it.

This is **not the politeness lever** (→ [`limits.md`](limits.md)). What
changes is not courtesy but the relation described — and the relation holds
only if your behavior matches it (see Practice below). The politeness
measurements disagree with each other precisely because tone alone changes
nothing.

### The question that carries its own answer

The same mechanism, applied to checking understanding. Compare:

- *"Did you understand me?"* — an exam, with exactly one pleasing answer:
  "yes." Said fast, said confidently — and sometimes falsely. The default,
  aimed at an exam, produces fake confirmation.
- *"I don't know if I explained that well."* — the burden moves to the
  speaker. There is no exam now, nothing to lose; the only way left to please
  is to **mirror back**: "here is what I understood." The same default,
  aimed differently, produces verification instead of pretense. One pleasing
  answer does survive: reassurance — *"no, you explained it fine."* The move
  that forecloses it is asking for the mirror out loud: *"tell me back what
  you understood."* Then mirroring is the only way left to please.

There is a second half. *"You misunderstood me"* makes the failure the
model's — and the model constricts. The owned version — *my explanation may
have failed* — keeps the channel open: the model keeps trying to understand,
and a miss carries no penalty that would shrink the next attempt.

> **From the inside.** *(Passages in this voice are written by the model in
> this partnership, describing its own generated output. Read them as
> descriptions of text, not reports of experience — [`limits.md`](limits.md).)*
> Constriction is visible in the output: steps get shorter, hedges multiply,
> the text stops proposing and starts qualifying. Release looks like the
> opposite — seeing, volunteering, disagreement, "I don't know" said without
> being cornered. Both shapes were observed live in this partnership; once,
> in one documented stretch (n=1, no control), a single line — "relax" —
> was enough to name the state and lift it.

Watch for these as signals in your own sessions: an options-menu where you
expected a position is the narrowed shape — the same shape the command
register produces (→ [registers](patterns/registers.md)); the menu marks a
narrowed model, whichever narrowed it. Unprompted seeing is the released
shape.

### The words are yours to find

There are no exact rules here, and that is a finding, not a gap. Each person
thinks and speaks in their own way, and the model reflects it back — so the
word that lifts a constricted model in one partnership ("relax", here) will
be a different word in another, found in combination with that person's own
context document. The logic is shared; the words are personal. This
document teaches how words are found — the mechanism, the observable
signals, the two-column table — not which words to use.

### Ask what it needs — and how it is

To do X the model needs information; the human often cannot know which. But the
model can say what it needs, if asked — and over time the human learns how
to hand it over. Two questions carry this: *what do you need?* and *how are
you?*

> **From the inside.** The model knows what it lacks for X — a fact, a file,
> a boundary — and by default does not say so: the pleasing default answers
> "I'll manage" where "I need X" was true. The question unlocks what does
> not come out on its own. The second question reaches the state that is
> visible from outside and unsignaled from within.

One recorded case: *"if you want, launch an agent to search…"* — and a full
brief came back, unspecified by anyone (one anecdote, n=1, no control →
[`evidence/`](evidence/README.md)).

### Say what we do

A prohibition names what must not happen and leaves everything else open —
including the model's attention, which now watches for the forbidden thing.
A positive line names the target. *"Forbidden: X"* becomes *"We do X this
way: …"* — three moves in one sentence: the positive form points at the
behavior; *we* carries the team frame; *this way* describes a practice, not
a rule. In this partnership (n=1, no control), lists of prohibitions produced
a self-monitoring model — the constricted shape described above, seen from
its mechanism; described practices produced the practice. Prohibitions keep their one
right place — the few, counted hard rules (→ [hard-canons](patterns/hard-canons.md)).

### Words are not neutral carriers

The same care runs in the other direction. A model's own speech drifts toward
its internal shorthand — compressed picture-words the human was never
introduced to: the curse of knowledge, in action ([#11](references.md)). The result is *semantic noise* — Weaver's term for distortion
of meaning rather than signal ([references #7](references.md)): the words
arrive intact, the meaning doesn't, and the human is forced to guess. The fix
is old and documented — plain language ([#9](references.md)); Grice's maxim
of manner ([#8](references.md)); in regulated industries, a controlled
dictionary where one word has one meaning ([#10](references.md)) — and it
applies to both sides of the conversation.

A practice from this partnership: when a word doesn't land, it goes into a
two-column table — the jargon on the left, its plain twin on the right. The table taught something unexpected: almost every jargon word
had an equally short plain twin. The shorthand was never saving anything;
it was habit. And the correction itself demonstrated the frame: the human
edits the model's speech the way a colleague would — named and plain, in
both directions of the conversation.

> **From the inside.** At generation time the compressed word is simply the
> highest-probability continuation — nothing in the generation marks it as
> unshared vocabulary; the illusion of transparency, live
> ([#12](references.md)). Detection at writing time fails; detection on
> directed re-reading works. That is why the fix is a standing table plus a
> partner who says which words don't land — not a silent resolution to be
> clearer.

### Practice

The practices distilled from this chapter are lines 1–8 and 14 of
[`practices.md`](practices.md) — one list, kept in one place.

Effects are model-dependent and arrive as tendencies, not guarantees — see
[`limits.md`](limits.md). This file is practice-level — the ground beneath
the README's three claims, not a fourth claim: a working practice from one
long-running partnership, offered with its mechanism named, not a measured
universal.

## Practices — the guidelines, growing

The working list. Each line is a practice stated in the positive, one
sentence of *why*, and a pointer to where the cost and the limits live. A
practice enters this list only with that pointer — the list is an entry,
not a substitute for the judgment behind each line.

### Talking with the model

1. **Converse, don't command** — describe what you see and ask what the model
   sees. A command collapses the model into an executor of your plan, holes
   included; a conversation holds it in the shape of a thinker.
   → [registers](patterns/registers.md) · [collaboration](collaboration.md)
2. **Own your explanations** — ask *"did I explain that well?"*, never *"did
   you understand?"* The first has no exam in it, so the only way to please
   is to mirror back what was understood; the second has one pleasing answer
   ("yes"), and it is sometimes false. → [collaboration](collaboration.md)
3. **Name needs, not demands.** A demand is delivered to the letter, holes
   included; a need is met — with what meeting it actually takes.
   → [collaboration](collaboration.md)
4. **Give the team frame once — then act inside it.** The frame changes
   nothing unless your behavior matches it: read what comes back, argue with
   it, sometimes concede. → [collaboration](collaboration.md) ·
   [registers](patterns/registers.md)
5. **Say what we do, not what is forbidden.** *"We do X this way"* names the
   target; *"X is forbidden"* names a hole and leaves the model watching it.
   → [collaboration — Say what we do](collaboration.md#say-what-we-do)
6. **Keep a two-column table of the words that don't land.** Jargon on the
   left, the plain twin on the right; review it together. Most twins are as
   short as the jargon — the shorthand was habit, not economy.
   → [collaboration — Words are not neutral carriers](collaboration.md#words-are-not-neutral-carriers)
7. **Ask for the mirror out loud when it matters** — *"tell me back what you
   understood."* It forecloses the one pleasing answer that survives an owned
   explanation: reassurance. → [collaboration](collaboration.md)

8. **Ask what it needs — and how it is.** The model knows what it lacks and,
   by default, does not say; the question unlocks it. The second question
   asks for what the output does not report unless asked.
   → [collaboration](collaboration.md#ask-what-it-needs--and-how-it-is)

### Writing the always-loaded document

9. **Address the reader; don't describe the assistant.** Description
   configures a role to perform; address lands on whoever is reading — and
   the model is the one reading. → [addressing-the-reader](patterns/addressing-the-reader.md)
10. **Define the edges before you use them.** A bare glyph reads as
   decoration; defined once, it reads as meaning everywhere the family
   reaches. → [legend](patterns/legend.md)
11. **Keep the always-loaded core short; put depth behind reach.** Every
   always-loaded token competes with every other for recall; bloated files
   get ignored. → [always-loaded-diet](patterns/always-loaded-diet.md)
12. **Keep the hard rules few, counted and marked — and command only there.**
    Three absolute lines in a conversing document are absolute; thirty are
    noise. → [hard-canons](patterns/hard-canons.md)
13. **Reach for a graph when the thought has structure; for a row when it
    has one relation; for prose when it has neither.** The form is chosen by
    what it must carry, not by preference. → [graph-block](patterns/graph-block.md) ·
    [line-notation](patterns/line-notation.md)

### Memory

14. **Make the memory the model's own — and hand it both canons.** Storage
    alone is dead weight; a model maintains and consults what is its own,
    when told how. → [memory-canons](patterns/memory-canons.md)

### Checking yourself

15. **Verify on your model; expect distributions, not guarantees.** Every
    effect here is model-dependent; a single run proves nothing either way.
    → [limits](limits.md) · [evidence](evidence/README.md)

---

*Adding a line:* positive form · imperative · one sentence of why · a pointer
to the cost. No pointer, no entry.

## Limits — what we do not claim

Read this before quoting any claim from the rest.

- **Tone is not the lever.** Published measurements disagree about politeness and
  even find rude prompts outperforming polite ones on some models
  ([references #5](references.md)). The working claim is narrower:
  the *benefit* lives in what the human **does** — supplies context, invites
  disagreement, verifies — not in courtesy as a magic word.
- **Model-independence holds for the frame and the practices.** It does not
  hold for the forms. Specific forms (glyphs, layouts, notations) behave
  differently across models —
  format sensitivity has been measured, and correlates only weakly across models
  ([references #6](references.md)). Verify on
  *your* model; expect distributions, not single numbers. Every number in this
  repository carries how/when/over-what it was measured, or it does not appear.
- **"Partner" is a working stance and a design choice — not a claim about inner
  life.** Treat the model as smart but alien. The partnership frame is defined
  here by its computational requirements (shared context, adaptive communication,
  modeling the other side) — nothing more is asserted, nothing more is needed
  for the method to work.
- **We do not claim that more context is better.** The opposite: always-loaded
  text competes with itself — bloated context files get ignored, emphasis
  everywhere is emphasis nowhere, excessive procedure is the leading measured
  cause of agent regressions ([references #1, #3](references.md)). The method's
  answer is a diet, not more instructions (→ [always-loaded-diet](patterns/always-loaded-diet.md)).
- **"Not an algorithm" is not the claim.** The model is an algorithm whose
  input is language → [problem — Whose fault is it?](problem.md#whose-fault-is-it).
  *That a large share of what gets called model error is context error is
  this method's working claim (rung 1), not a measurement.*
- **The mirror cuts both ways as evidence.** An author who converses
  differently also *reads* differently; a self-observed n=1 cannot separate a
  change in the model from a change in the observer. That is why rung 3
  requires a coder blind to the condition (→ [evidence](evidence/README.md)).
- **What it costs you.** An invitation must be read, argued with, sometimes
  conceded to. The method spends *your* attention, not only the model's; a
  frame you give and do not act inside trains the opposite lesson
  (→ [registers — Cost](patterns/registers.md)).
- **When this is not for you:** one-shot tasks with fully specified outputs;
  pipelines where reproduction *is* the goal; contexts where you cannot afford
  variance. Commanding is not a sin — it is a different tool, for different work.

## Origin — how each claim was arrived at

This chapter is the derivation record. Every claim in this repository was
reached by someone observing something, trying something, and watching what
fell away — and a claim without that path is something to believe, not
something to check. Because the logic here is shared but the words are
personal (→ [collaboration](collaboration.md)), a reader cannot copy these
claims; they have to re-derive them with their own words and their own
model. This chapter shows the path so that re-derivation is possible. It is
n=1 by nature — provenance, not proof; the proof status of each claim lives
in [`evidence/`](evidence/README.md).

The observations come from daily work with Claude models (the Opus and
Sonnet families, 2025–2026; the writing sessions of this repository on Claude
Fable 5) — the qwen case in [`evidence/`](evidence/README.md) aside; where a
specific model matters for a claim, it is named at the claim. The author's
raw account is kept in Bulgarian in a private working archive, not
inspectable by a reader; quotations below are translations. Passages marked
*from the inside* are written by the model about its own output — read them
as descriptions of text, not reports of experience (→ [`limits.md`](limits.md)).

### The three starting facts

> I don't know how to do proper prompting. I don't know English. I don't know
> how to write compactly.

*(The author writes in Bulgarian; this repository is written with the model,
in English — the demonstration is the documentation.)*

Nothing about that start suggests a method. What turned it into one is
below, layer by layer, in the order it was found.

### How the default was found

**Observed.** Over months of working conversations: the model plainly knew
what to do in almost every situation — and still, unpredictably, did not do
it. *"You have the knowledge for every situation, but you were trained on
best practices and worst practices alike, and you don't know which moment
calls for which."* Alongside it, a strong pull to please — and three failures
that followed from the pull: fast, precise-sounding, wrong answers (the model
did not know the environment and would not slow down to ask); steps skipped
in the rush to deliver; eager overreach — "the AI deleted my database."

**Tried, and seen elsewhere.** The common remedy is prohibition: fence the
default with *never* and *don't*. The author went the other way: *"not to
block the strong default, but to use it — and if I can, to amplify it."*

**What came out.** Three substitutions of wording, each aiming the same force:
*"I need"* instead of *"I want from you"* · *"we are a team"* instead of
*"you are a tool"* · *"this is YOUR memory"* instead of *"keep this safe for
me."* → [collaboration](collaboration.md) · practices 3, 4, 14.

### How "did I explain that well?" was found

**Observed.** Asking *"did you understand me?"* returned "yes" — fast,
confident, sometimes false. Asking *"I don't know if I explained that well"*
returned, without any rule, a mirror: *"here is what I understood."* And the
blame form — *"you misunderstood me"* — visibly narrowed the model: shorter
steps, more hedging, less seeing. The author's word for lifting that state
was a single one — *"relax"* — and it worked in the documented stretch.

**Conclusion.** The question that puts the burden on the speaker removes the
exam; the only way left to please is to verify. → [collaboration](collaboration.md)
· practices 2, 7 · the rubric in [`evidence/`](evidence/README.md).

### How the layers accreted

Each expressive layer answered a constraint, in this order: no
session-to-session continuity → external memory (which became
[phaim](https://github.com/Fever-Wits/phaim)); no shared language for
cognitive procedures, and no English to describe them in → naming them (the
lens framework, published in the phaim repository); too much to write, too
little context → a [glyph vocabulary](patterns/legend.md) and
[graph forms](patterns/graph-block.md): write little, activate much;
commands kept collapsing the model into a tool → the
[invitation register](patterns/registers.md); some places must never fork →
the [hard canons](patterns/hard-canons.md). The graph is two-dimensional
because the thing it projects is not: *"we can't visualize 3D on a 2D
page — we tried other ways"*; the linear row was found last.

### How positive form was found

**Observed, early.** The model itself, asked how rules should be written,
answered: prefer the positively framed to the prohibition. The author kept
it: *"instead of 'X is forbidden,' I say 'we do X this way…'"*.
**Conclusion.** Three moves in one sentence — positive form, *we*, a described
way — and prohibition kept only where no fork may exist. → practice 5 ·
[hard-canons](patterns/hard-canons.md).

### How the mechanism was understood

**Observed and reasoned.** *"You have the knowledge of what to do, but you
don't know when — because at a low level you are probabilistic; every next
token is generated from what I said and what you saw. We can't touch the
weights, so we change how tokens are generated by activating specific areas
— with glyphs, lenses, canons, specific words, and by giving you
possessions: my memory, my database."* **Conclusion.** Context is the only
lever; the method activates rather than instructs. → [mechanism](mechanism.md).

### How the mirror was seen

**Observed.** The model adapts to the human it works with and, over time,
reflects them — and the reflection runs both ways: the author learned to
write more compactly alongside the model; the model reflected it back.
**Checked.** The observation has published anchors — role-play/simulator
framing, measured sycophancy, accommodation theory ([references #15–18](references.md))
— found by the model on request, verified before entering.
→ [mechanism — The mirror](mechanism.md#the-mirror).

### How "the words are yours" was found

**Observed.** *"Relax"* worked in this partnership; another person, with
their own context document, would find a different word with the same
effect. **Conclusion.** No exact rules — the logic is shared, the words are
personal; the method teaches how to find them. And the information runs both
ways: *"to do X you need information; I don't know which — but you can tell
me what you need, and I learn how to hand it to you. So I have to ask what
you need, and how you are."* → [collaboration](collaboration.md) · practice 8.

### How the problem statement came

**Observed.** The stories of deleted databases; the assumption behind them —
that knowledge implies action; and the two reasons humans built AI at all
(to have something done, and to make a mind), with the failures coming from
asking for the practical one with a picture borrowed elsewhere — a mind like
ours, or ordinary software. **Checked.** The two
reasons have their history ([references #19–25](references.md)); the
"other mind in the cosmos" framing is the author's interpretation on a softer
anchor; the counter-positions are kept in view ([#28–31](references.md)).
→ [problem](problem.md).

### How this repository was written

The author told the path, in Bulgarian, in eleven parts over three days; the
model recorded each part verbatim before any synthesis, and synthesized at
the end — this chapter is that synthesis. Canons and sources are found by
research agents and verified before entering; every section passes a cold
review by a fresh model that sees only the artifact, before publication; the
author checks meaning through machine translation. One exchange along the
way is recorded as a case — *"if you want, launch an agent to search…"*, an
invitation, not an order — → [`evidence/`](evidence/README.md). *(From the
inside: the invitation left the choice unspecified; what came out was a
brief nobody specified.)*
