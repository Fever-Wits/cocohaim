# Evidence

Every claim in this repository either points at something you can re-run, or is
marked as a working hypothesis. Numbers appear only with how / when / over what
they were measured. Effects are reported as distributions across runs and
models, not as single flattering numbers.

Incoming (being adapted from the working archive):

- **Before/after on a foreign small model** — a 27B local model (qwen, 4-bit,
  ollama + Letta) reads two context documents written in this method; its
  stance, grammar and behavior change within one message, and persist across a
  process restart. With internal controls: 57K chars of same-vocabulary prose
  20 minutes earlier moved vocabulary but not stance; a structured skill file
  read after moved neither. Includes honest confounds.
- **Encoded-capsule protocol tests** — the same graph content accepted by
  unrelated models (Grok, Gemini) when framed as data, and hallucinated about
  when framed as prose. (Published in the phaim repository; being linked.)
- **Planned: graph vs prose discriminating experiment** — same content, two
  forms, two fresh agents, same model: does the graph change stance where
  paraphrased prose only adds vocabulary?
