# References

Numbered sources for every measured claim in this repository. A number in the
text without a live pointer here is a bug — report it; an entry nobody cites
is removed. Links marked *(secondary link)* point at an overview, not the
original.

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
5. **Sharma et al. (2023)** — "Towards Understanding Sycophancy in Language
   Models," arXiv:2310.13548 (ICLR 2024). Five RLHF-trained assistants
   consistently match the user's stated views over truthful answers; human
   and preference-model judges reward it. https://arxiv.org/abs/2310.13548
6. **Perez et al. (2022)** — "Discovering Language Model Behaviors with
   Model-Written Evaluations," arXiv:2212.09251. Larger and RLHF-tuned
   models increasingly echo the user's stated persona rather than answer
   independently. https://arxiv.org/abs/2212.09251
7. **COPE (2023)** — *Authorship and AI tools*, COPE position statement,
   Committee on Publication Ethics (reviewed 13 Feb 2023). "AI tools cannot
   be listed as an author"; as non-legal entities they cannot manage copyright
   and licence agreements; use must be disclosed — which tool, and how; the
   authors remain fully responsible for every part.
   https://publicationethics.org/guidance/cope-position/authorship-and-ai-tools
8. **CRediT (2022)** — *Contributor Roles Taxonomy*, ANSI/NISO Z39.104-2022.
   Fourteen named roles; the ones decision 0008 leans on:
   Conceptualization · Validation · Writing – original draft · Writing –
   review & editing. https://credit.niso.org/contributor-roles-defined/
9. **Zhou, Schellaert, Martínez-Plumed, Moros-Daval, Ferri &
   Hernández-Orallo (2024)** — "Larger and more instructable language models
   become less reliable," *Nature*, 25 Sept 2024. Shaping models up "has
   usually penalized answers that hedge or look uncertain"; developers are
   pushed toward models that are "never evasive" — that say something rather
   than admit a gap. https://www.nature.com/articles/s41586-024-07930-y ·
   open access: https://pmc.ncbi.nlm.nih.gov/articles/PMC11446866/
10. **Kalai, Nachum, Vempala & Zhang (2025)** — "Why Language Models
    Hallucinate," OpenAI, arXiv:2509.04664. Under the usual scoring, "I don't
    know" earns the same as a wrong answer — zero — so training and evaluation
    reward a confident guess over an admitted gap.
    https://arxiv.org/abs/2509.04664
11. **Vaswani et al. (2017)** — "Attention Is All You Need," arXiv:1706.03762
    (June 2017). The paper that introduced the transformer — the way of
    building a model that every large language model since is built on.
    https://arxiv.org/abs/1706.03762
