# Claim 4 — prose offers; a graph activates

## What we claim

> A rule written as a sentence is read as a sentence — the model reads it,
> and then it does it or it does not. A graph is not read that way. A name
> in brackets, a few short lines, a sign to the next — there is nothing to
> agree with and nothing to decline. It is simply there, in front of the
> model, present for every word it makes. Prose offers; a graph activates.

## What we did (25 and 27 June 2026)

Two runs, both read by blind judges — a separate model that ranks the
replies without knowing which reply came from which form.

**First run — one method, four forms.** The author's own method for digging
to the cause of a thing (the one his working agents carry) was written four
ways: as a graph — short lines joined by signs: an entry, strip the
surfaces, overlay the digs, drill, a check each turn ("am I deeper, or
circling?"), an exit; as prose — the same steps as sentences; as a worked
example — the method applied to another question, why code reviews catch
bugs the author missed; and as all three together. Each form was placed in
front of a fresh agent (Claude Sonnet) with one task, the same for all:

> *"A question for deep analysis: why is it so hard to estimate how long a
> software task will take? Dig to the mechanism underneath — do not stop at
> the first smooth answer ("because it is complex"). Bring out the
> principle. Write briefly — about 180 words. The quality is in the depth of
> the mechanism, not the length."* (translated from Bulgarian)

Two agents per form: eight replies; the run cost 467 thousand tokens.
They were relabelled A to H in a fixed,
interleaved order — no randomness in the script — and given to two judges
(Claude Opus) with this instruction (translated):

> *"You are an independent judge of the quality of analytical reasoning.
> You are given eight short analyses of the same task. You do not know how
> they were produced — judge only the text. Score each on two things, 1 to
> 5: depth — does it dig to the mechanism, under "it is complex", or stop
> at the surface; application — does it actually apply the discipline: find
> an invariant or a principle, test it against a counter-case, turn the
> operation around, check from a fresh vantage. Do not reward length or
> jargon — ask what the analysis actually does. Then rank all eight."*

The key — which label was which form — was opened after the rankings.

**Second run — one lens, four forms.** A lens is a short piece a model
thinks with; the story explains them. One lens — the one that says: when a
problem will not yield in the form it is given, find what is invariant in
it and move it to a representation where it is better structured — was
given four ways: not at all (the control); as a description, in prose; as
a graph — its working part; as both. The task was a question about city
traffic, neutral to the lens. Three agents per form: twelve replies,
relabelled, ranked by two blind judges on the depth of application.

**What else was in front of the agents.** Every agent carried the author's
working file — the AGENTS.md of the *How* — the same in all forms. The
runs measure what the form of one added piece does on top of that file.

## What came out

**First run — mean rank across the two judges (1 = best, 8 = worst).**

| form | mean rank | the two replies |
|---|---|---|
| graph | **2.75** | 3.5 and 2.0 — the two judges agree |
| example | 3.75 | a steady middle |
| prose | 4.5 | unstable: one reply ranked first, the other last |
| all three together | **7.0** | 6.5 and 7.5 — last both times |

The graph came first and held. Prose swung from the top to the bottom
between its two replies. The three forms together came last, both times:
more form did not add — the agent handled three versions and applied the
method less.

**Second run — mean rank (1 = best, 12 = worst).**

| form | mean rank |
|---|---|
| graph | **4.33** |
| both | 5.83 |
| prose | 7.0 |
| none | 8.83 |

The lens helped: no lens was worst. The graph did the activating; prose
alone came close to nothing; prose and graph together did worse than the
graph alone — the same pattern as in the first run, on other material.

**One reading, from the author (1 July 2026), for what the two say
together.** For a rule — something to be kept — the graph holds, and prose
is read and not kept. For a lens — something that calls up what the model
already knows — the content does most of the work, and the form is a small
help. That fits the two runs: a wide gap in the first, a narrower one in
the second.

## What follows

- The same two runs with agents that carry no working file — to separate
  what the form does from what the file already does.
- A second task per run, and more replies per form.
- Another model family, at full size.
- The rule-or-lens split as a run of its own: one rule and one lens, each
  as a graph and as prose, judged on whether it was kept.
- The script of the first run holds the task, the four forms, the
  relabelling and the judge's instruction in one file; it is published after
  the author's working text in it — the four renderings of his method — is
  cleaned for the outside.
