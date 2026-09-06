# Claim 4 — prose offers; a graph activates

## What we claim

> A rule written as a sentence is read as a sentence — the model reads it,
> and then it does it or it does not. A graph is not read that way. A name
> in brackets, a few short lines, a sign to the next — there is nothing to
> agree with and nothing to decline. It is simply there, in front of the
> model, present for every word it makes. Prose offers; a graph activates.

What a graph is, in this method, is shown in
[patterns/graph-block.md](../patterns/graph-block.md): the name of a thing in
square brackets; under it, short lines; between the lines, signs that say how
one leads to the next; and a legend that says what each sign means. The story
shows one in the *How* — the block called *the exit*.

## What we did (25 and 27 June 2026)

Two runs. In both, the replies were judged blind: a separate model ranked them
without knowing which reply came from which form.

**First run — one method, four forms.** The author has a method for digging to
the cause of a thing. The models he works with carry it. It was written in
four forms:

- as a graph — the form described above: the steps as short lines, a sign
  from each to the next, the check and the exit marked;
- as prose — the same steps, written as sentences;
- as an example — the method applied to another question (why code reviews
  catch bugs the author missed), from the first easy answer down to the
  principle;
- as all three, one after the other.

Each form was put at the start of a fresh conversation with the model (Claude
Sonnet), together with one task. The task was the same for all (translated
from Bulgarian):

> *"A question for deep analysis: why is it so hard to estimate how long a
> software task will take? Dig to the mechanism underneath — do not stop at
> the first smooth answer ("because it is complex"). Bring out the
> principle. Write briefly — about 180 words. The quality is in the depth of
> the mechanism, not the length."*

Two conversations per form: eight replies. The run cost 467 thousand tokens.
The replies were given the letters A to H, in a fixed order that mixed the
forms. Two judges (Claude Opus) received the eight lettered replies. They did
not know which letter was which form. Their instruction (translated):

> *"You are an independent judge of the quality of analytical reasoning.
> You are given eight short analyses of the same task. You do not know how
> they were produced — judge only the text. Score each on two things, 1 to
> 5: depth — does it dig to the mechanism, under "it is complex", or stop
> at the surface; application — does it actually apply the discipline: find
> an invariant or a principle, test it against a counter-case, turn the
> operation around, check from a fresh vantage. Do not reward length or
> jargon — ask what the analysis actually does. Then rank all eight."*

Which letter was which form was revealed after the rankings.

**Second run — one lens, four forms.** A lens is a short piece a model thinks
with; the story explains them. One lens was used. It says: when a problem does
not give way in the form it came in, find what stays the same in it, and move
that into a form where it is easier to handle. The lens was given in four
ways: not at all; as prose that describes it; as a graph of its steps; as
both. The task was a question about traffic in a city — it had nothing to do
with the lens. Three conversations per form: twelve replies. They were
lettered and ranked by two judges who did not know which was which, on how
deeply the lens was applied.

**One more thing was in front of the model every time.** Every conversation
also carried the author's working file — the AGENTS.md the *How* describes —
the same file in every form. So the runs show what the form of one added piece
does on top of that file.

## What came out

**First run — the average place of each form, over the two judges (1 is best,
8 is worst).**

| form | average place | the two replies |
|---|---|---|
| graph | **2.75** | 3.5 and 2.0 — both judges put it first |
| example | 3.75 | steady, in the middle |
| prose | 4.5 | first once, last once |
| all three together | **7.0** | 6.5 and 7.5 — last both times |

The graph came first, and both judges put it there. Prose was first once and
last once. All three together came last both times: more form did not help —
the model had three versions of the method to handle, and applied it less.

**Second run — the average place of each form (1 is best, 12 is worst).**

| form | average place |
|---|---|
| graph | **4.33** |
| both | 5.83 |
| prose | 7.0 |
| no lens | 8.83 |

Having the lens helped: without it was worst. The graph did the work. Prose
alone was close to having no lens at all. Prose and graph together did worse
than the graph alone — the same as in the first run, with different material.

**Why the gap is wide in the first run and narrow in the second — the author's
explanation (1 July 2026).** A method is a rule: something to be kept. The
graph holds it; prose is read and not kept. A lens is not a rule: it calls up
something the model already knows. There the content does most of the work,
and the form helps a little.

## What follows

- The same two runs without the working file — to separate
  what the form does from what the file already does.
- A second task for each run, and more replies per form.
- Another model family, at full size.
- A run of its own for the rule-or-lens split: one rule and one lens, each
  as a graph and as prose, judged on whether it was kept.
- The script of the first run holds the task, the four forms, the
  lettering and the judges' instruction in one file. It will be published
  after the author's working text in it — the four renderings of his
  method — is cleaned for the outside.
