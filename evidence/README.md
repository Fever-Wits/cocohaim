# Evidence

Every measured claim in this repository points at a numbered source in
[`REFERENCES.md`](../REFERENCES.md), or at material in this directory, or is
marked below as a **working hypothesis**. Effects are reported as distributions
across runs and models, not as single flattering numbers.

## Claim → status

| Claim (from the README) | Status today |
|---|---|
| 1. Register sets the mode (command → reproduction · conversation → thinking) | **working hypothesis** — observed repeatedly in one working partnership (n=1 setting, no control); a controlled comparison is designed but not yet run |
| 2. Documents activate at read time (form changes stance) | **incoming** — a documented before/after on a foreign 27B model exists in the working archive and is being adapted for publication here, with its confounds |
| 3. Memory lives only with maintain + use canons | **partial, negative direction** — the "configured, never called" failure is documented in the same before/after; the positive direction is working practice, not yet a controlled result |

Nothing in this directory is deliverable *yet* — this table is the honest state,
kept current as material lands.

## Incoming

- **Before/after on a foreign small model** — a 27B local model (qwen, 4-bit,
  ollama + Letta) reads two context documents written in this method; its
  stance and self-description change within one message and persist across a
  process restart. Internal controls: 57K chars of same-vocabulary prose 20
  minutes earlier moved vocabulary but not stance; a structured skill file
  read after moved neither. Confounds documented (partner framing spoken
  before the read; reasoning-effort change 6 min prior; n=1).
- **Encoded-capsule protocol tests** — the same graph content accepted by
  unrelated models (Grok, Gemini) when framed as data, and hallucinated about
  when framed as prose. Published in the
  [phaim repository](https://github.com/Fever-Wits/phaim) (LENS-AS-PROTOCOL
  files).
- **Planned: graph vs prose discriminating experiment** — same content, two
  forms, two fresh agents, same model: does the graph change stance where
  paraphrased prose only adds vocabulary?

## Contribute a run

The cheapest way this directory fills: run [`start-here.md`](../start-here.md)
on your model, keep the transcript, and report what changed (or didn't) via an
issue. Negative results are as welcome as positive ones — the limits are part
of the method.
