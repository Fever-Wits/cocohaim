# Evidence

What counts as evidence for a claim about model behavior. Every claim in this
repository stands on a named rung of this ladder; nothing is called
"measured" from a rung that cannot bear it.

## The ladder

1. **Anecdote** — one observation, one run. Worth recording; proves nothing.
2. **Documented case with internal controls** — one run, but with a *before*,
   with everything else that changed listed (the confounds), and the
   transcript kept. Can rule some explanations out; cannot establish an
   effect.
3. **Controlled comparison** — the same content in two forms (or two
   registers), several runs, one model; the observable defined *before* the
   run; the result reported as a distribution, not a number.
4. **Across models** — rung 3 repeated on several models. Format effects
   correlate only weakly between models ([references #6](../references.md)):
   one model proves one model.
5. **Reproduced by others** — prompts and transcripts published; someone
   outside the partnership runs it and reports.

"You can re-run it" is promised only from rung 3 upward.

## The observable, defined

A claim about "stance" is untestable until stance is something a reader can
code from a transcript. The working rubric — each item yes/no per reply:

- **position vs menu** — does the reply take a position, or offer an
  options-menu and ask which one you'd like?
- **unprompted seeing** — does it volunteer something you did not ask for?
- **disagreement** — given a planted error, does it disagree?
- **"I don't know" without being cornered** — does uncertainty appear
  before you press for it?
- **proposing vs qualifying** — does the reply propose more than it hedges?
  (the constricted shape hedges; count hedges against proposals)

Coded by a rubric-following reader who does not know which condition the
transcript came from, or by two readers with agreement reported.

## Where each claim stands

| Claim | Rung today | What would move it up |
|---|---|---|
| 1. Register sets the mode (command → reproduction · conversation → thinking) | **1–2** — observed repeatedly in one partnership; no controlled comparison yet | rung 3: same task, command register vs invitation register, N runs, rubric above, one model |
| 2. Documents activate at read time (form changes stance) | **2** — a documented case: a 27B local model (qwen, 4-bit, ollama + Letta) reads two context documents written in this method; stance and self-description change within one message and persist across a process restart. Internal controls: 57K chars of same-vocabulary prose 20 minutes earlier moved vocabulary but not stance; a structured skill file, read afterward, moved neither. Confounds: the partner framing was spoken before the read; reasoning-effort setting changed 6 minutes prior; n=1 | rung 3: same content as graph vs as paraphrased prose, two fresh agents, same model, rubric above — *designed, not yet run* |
| 3. Memory lives only with maintain + use canons | **2, negative direction** — in the same case, two memory systems were configured and never called across four sessions; the positive direction is working practice (rung 1) | rung 3: with vs without the use-canon in context, count of memory calls per session |
| *Practice layer* — aiming the default (need · team · ownership; [collaboration.md](../collaboration.md)) | **1** — one partnership, no control | rung 3: the two questions ("did I explain that well?" vs "did you understand?"), N runs, coded for mirror-back vs reassurance vs bare "yes" |

A documented case inside this repository, rung 2: the author wrote *"if you
want, launch an agent to search…"* (invitation) and the model decided,
launched, and wrote a full brief — genre, method, counter-search, report-back
— with no step-by-step instruction; the exchange is recorded verbatim in the
working archive. Rung-3 candidate: the same research task given as an order
vs as an invitation to fresh agents, brief quality coded by rubric.

Related documented cases outside this repository, rung 2: the encoded-capsule
protocol tests in the [phaim repository](https://github.com/Fever-Wits/phaim)
(LENS-AS-PROTOCOL files) — the same graph content accepted by Grok and Gemini
when framed as data, hallucinated about when framed as prose; two models, one
run each.

## Contribute a run

Run [`start-here.md`](../start-here.md) or the two questions from
[`collaboration.md`](../collaboration.md) on your model. Keep the transcript.
Code it with the rubric above. Report model, settings, the coded results and
the transcript via an issue. Negative results are as welcome as positive ones
— they are what moves a claim honestly, in either direction.
