# Limits — what we do not claim

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
