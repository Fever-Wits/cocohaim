# References

Numbered sources for every measured claim in this repository. A number in the
text without a live pointer here is a bug — report it.

1. **Dong et al., 2026** — *SkillsBench: 307 confirmed skill-caused failures*
   (84 tasks / 11 domains + 490 SWE instances; Claude Opus 4.6 + OpenCode).
   Excessive Procedure = 62.6% of efficiency regressions.
   https://arxiv.org/abs/2608.11888
2. **Jiang et al., 2026** — retrieval accuracy across skills falls 29.6% → 3.3%
   as the pool grows from 5 to 100; skills act as procedural anchors (65.7%),
   not knowledge injection (4.5%). https://arxiv.org/abs/2608.14036
3. **Anthropic, Claude Code best practices** (vendor documentation) — "Bloated
   CLAUDE.md files cause Claude to ignore your actual instructions"; "If you
   emphasize many lines, none of them stands out"; the per-line removal test.
   https://code.claude.com/docs/en/best-practices
4. **Weininger / Daylight, SMILES theory manual** — "a line notation (a
   typographical method using printable characters)"; "a linguistic construct,
   rather than a computer data structure"; 50–70% more compact than the
   equivalent connection table.
   https://www.daylight.com/dayhtml/doc/theory/theory.smiles.html
5. **Politeness/tone measurements (disagreeing):** Yin et al., SICon 2024
   (three languages; impolite often hurts, over-polite does not reliably help)
   https://aclanthology.org/2024.sicon-1.2/ · Dobariya & Kumar 2025 (one model:
   "Very Rude" 84.8% vs "Very Polite" 80.8%) https://arxiv.org/abs/2510.04950 ·
   Dobariya & Kumar 2026 (four models: "tonal effects are systematic but highly
   model-dependent") https://arxiv.org/abs/2605.29027
6. **Format sensitivity:** Sclar et al. (FormatSpread) — up to 76 accuracy
   points from minor format changes; weak correlation across models; report
   intervals, not single numbers https://arxiv.org/abs/2310.11324 · He et al.
   2024 — up to 40% variance by template (GPT-3.5, code translation)
   https://arxiv.org/abs/2411.10541
