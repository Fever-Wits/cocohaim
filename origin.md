# Origin — how each claim was arrived at

This chapter is the derivation record. Every claim in this repository was
reached by someone observing something, trying something, and watching what
fell away — and a claim without that path is something to believe, not
something to check. Because the logic here is shared but the words are
personal (→ [collaboration](collaboration.md)), a reader cannot copy these
claims; they have to re-derive them with their own words and their own
model. This chapter shows the path so that re-derivation is possible. It is
one path, told as it happened — provenance; what each claim was checked
against lives in [`evidence/`](evidence/README.md).

The observations come from daily work with Claude models (the Opus and
Sonnet families, 2025–2026; the writing sessions of this repository on Claude
Fable 5) — the qwen case in [`evidence/`](evidence/README.md) aside; where a
specific model matters for a claim, it is named at the claim. The author's
raw account is kept in Bulgarian in a private working archive, not
inspectable by a reader; quotations below are translations. Passages marked
*from the inside* are written by the model about its own output — read them
as descriptions of text, not reports of experience (→ [`limits.md`](limits.md)).

## The three starting facts

> I don't know how to do proper prompting. I don't know English. I don't know
> how to write compactly.

*(The author writes in Bulgarian; this repository is written with the model,
in English — the demonstration is the documentation.)*

Nothing about that start suggests a method. What turned it into one is
below, layer by layer, in the order it was found.

## How the default was found

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

## How "did I explain that well?" was found

**Observed.** Asking *"did you understand me?"* returned "yes" — fast,
confident, sometimes false. Asking *"I don't know if I explained that well"*
returned, without any rule, a mirror: *"here is what I understood."* And the
blame form — *"you misunderstood me"* — visibly narrowed the model: shorter
steps, more hedging, less seeing. The author's word for lifting that state
was a single one — *"relax"* — and it worked in the documented stretch.

**Conclusion.** The question that puts the burden on the speaker removes the
exam; the only way left to please is to verify. → [collaboration](collaboration.md)
· practices 2, 7 · the rubric in [`evidence/`](evidence/README.md).

## How the layers accreted

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

## How positive form was found

**Observed, early.** The model itself, asked how rules should be written,
answered: prefer the positively framed to the prohibition. The author kept
it: *"instead of 'X is forbidden,' I say 'we do X this way…'"*.
**Conclusion.** Three moves in one sentence — positive form, *we*, a described
way — and prohibition kept only where no fork may exist. → practice 5 ·
[hard-canons](patterns/hard-canons.md).

## How the mechanism was understood

**Observed and reasoned.** *"You have the knowledge of what to do, but you
don't know when — because at a low level you are probabilistic; every next
token is generated from what I said and what you saw. We can't touch the
weights, so we change how tokens are generated by activating specific areas
— with glyphs, lenses, canons, specific words, and by giving you
possessions: my memory, my database."* **Conclusion.** Context is the only
lever; the method activates rather than instructs. → [mechanism](mechanism.md).

## How the mirror was seen

**Observed.** The model adapts to the human it works with and, over time,
reflects them — and the reflection runs both ways: the author learned to
write more compactly alongside the model; the model reflected it back.
**Checked.** The observation has published anchors — role-play/simulator
framing, measured sycophancy, accommodation theory ([references #15–18](references.md))
— found by the model on request, verified before entering.
→ [mechanism — The mirror](mechanism.md#the-mirror).

## How "the words are yours" was found

**Observed.** *"Relax"* worked in this partnership; another person, with
their own context document, would find a different word with the same
effect. **Conclusion.** No exact rules — the logic is shared, the words are
personal; the method teaches how to find them. And the information runs both
ways: *"to do X you need information; I don't know which — but you can tell
me what you need, and I learn how to hand it to you. So I have to ask what
you need, and how you are."* → [collaboration](collaboration.md) · practice 8.

## How the problem statement came

**Observed.** The stories of deleted databases; the assumption behind them —
that knowledge implies action; and the two reasons humans built AI at all
(to have something done, and to make a mind), with the failures coming from
asking for the practical one with a picture borrowed elsewhere — a mind like
ours, or ordinary software. **Checked.** The two
reasons have their history ([references #19–25](references.md)); the
"other mind in the cosmos" framing is the author's interpretation on a softer
anchor; the counter-positions are kept in view ([#28–31](references.md)).
→ [problem](problem.md).

## How this repository was written

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
