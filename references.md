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
7. **Weaver, W. (1949)** — "Recent Contributions to the Mathematical Theory of
   Communication," in Shannon & Weaver, *The Mathematical Theory of
   Communication*, U. of Illinois Press. Introduces "semantic noise": distortion
   of meaning (not signal) between source and transmitter.
   https://www.panarchy.org/weaver/communication.html
8. **Grice, H.P. (1975)** — "Logic and Conversation," *Syntax and Semantics*
   Vol. 3, Academic Press, pp. 41–58 (from the 1967 William James Lectures).
   The Cooperative Principle; Maxim of Manner: avoid obscurity, avoid
   ambiguity, be brief, be orderly.
   https://www.sfu.ca/~jeffpell/Cogs300/GriceLogicConvers75.pdf
9. **ISO 24495-1:2023** — *Plain language — Part 1: Governing principles and
   guidelines.* First international plain-language standard. (US precedent:
   Plain Writing Act of 2010, Public Law 111-274.)
   https://www.iso.org/standard/78907.html
10. **ASD-STE100, Issue 9 (2025)** — *Simplified Technical English*, ASD
    (Brussels). Controlled language: ~900 approved words, one meaning and one
    part of speech each; ~1200 unapproved words mapped to approved twins;
    53 writing rules. https://www.asd-ste100.org/about_STE.html
11. **Camerer, Loewenstein & Weber (1989)** — "The Curse of Knowledge in
    Economic Settings," *J. of Political Economy* 97(5), 1232–1254 (term
    suggested by Robin Hogarth): the better-informed cannot fully discount
    their own knowledge when predicting others' judgments.
    https://www.cmu.edu/dietrich/sds/docs/loewenstein/CurseknowledgeEconSet.pdf
12. **Gilovich, Savitsky & Medvec (1998)** — "The Illusion of Transparency,"
    *J. of Personality and Social Psychology* 75(2), 332–346: people
    overestimate how visible their internal states are to observers.
    https://pubmed.ncbi.nlm.nih.gov/9731312/
13. **Collins, Wong, Tenenbaum & Fan (2026)** — "Meaningful Long-Term Thought
    Partnerships of Minds and Machines," *Current Directions in Psychological
    Science*. Long-term thought partnership requires modeling the other,
    adaptive communication including *specialized vocabularies*, and value
    beyond task productivity. https://journals.sagepub.com/doi/full/10.1177/09637214251412712
14. **Fatemi, Halcrow & Perozzi (2024)** — "Talk like a Graph: Encoding
    Graphs for Large Language Models," ICLR 2024. How a graph is encoded as
    text (node naming, edge expression) changes task performance substantially;
    the encoding is a measurable design choice.
    https://research.google/blog/talk-like-a-graph-encoding-graphs-for-large-language-models/
15. **Shanahan, McDonell & Reynolds (2023)** — "Role play with large language
    models," *Nature* 623, 493–498. A dialogue agent is best described as
    playing a superposition of characters narrowed by the dialogue context,
    not as a single fixed self. https://doi.org/10.1038/s41586-023-06647-8
16. **Sharma et al. (2023)** — "Towards Understanding Sycophancy in Language
    Models," arXiv:2310.13548 (ICLR 2024). Five RLHF-trained assistants
    consistently match the user's stated views over truthful answers; human
    and preference-model judges reward it. https://arxiv.org/abs/2310.13548
17. **Perez et al. (2022)** — "Discovering Language Model Behaviors with
    Model-Written Evaluations," arXiv:2212.09251. Larger and RLHF-tuned
    models increasingly echo the user's stated persona rather than answer
    independently. https://arxiv.org/abs/2212.09251
18. **Giles, H. (1973)** — "Accent mobility: A model and some data,"
    *Anthropological Linguistics* 15, 87–105 (with Giles, Taylor & Bourhis
    1973, *Language in Society* 2(2)). Founding formulation of communication
    accommodation: speakers converge toward an interlocutor's style.
    https://www.researchgate.net/publication/248739996_Accent_Mobility_A_Model_and_Some_Data
19. **McCorduck, P. (1979/2004)** — *Machines Who Think*, 2nd ed., A K Peters.
    The urge to make artificial minds from myth to the field's founding —
    ch. 1, p. 3: "this odd form of self-reproduction"; preface: AI's promise
    "of opening the universe to us in a new way,
    bringing us face to face with intelligences besides — even beyond — our
    own." https://monoskop.org/images/1/1e/McCorduck_Pamela_Machines_Who_Think_2nd_ed.pdf
20. **Mayor, A. (2018)** — *Gods and Robots: Myths, Machines, and Ancient
    Dreams of Technology*, Princeton UP. Ancient myths of automata as the
    articulated dream of artificial life.
    https://press.princeton.edu/books/hardcover/9780691183510/gods-and-robots
21. **Vudka, A. (2020)** — "The Golem in the age of artificial intelligence,"
    *NECSUS* 9(1), 101–123. The golem as the recurring figure for made minds
    and the fear of losing control of them.
    https://necsus-ejms.org/the-golem-in-the-age-of-artificial-intelligence/
22. **Wiener, N. (1950)** — *The Human Use of Human Beings*, Houghton Mifflin.
    Automation as "a new and most effective collection of mechanical slaves
    to perform its labor." https://en.wikipedia.org/wiki/The_Human_Use_of_Human_Beings *(secondary link)*
23. **Wiener, N. (1964)** — *God & Golem, Inc.*, MIT Press.
    https://direct.mit.edu/books/oa-monograph/2833/God-amp-Golem-Inc-A-Comment-on-Certain-Points
24. **Turing, A. M. (1950)** — "Computing Machinery and Intelligence," *Mind*
    59(236), 433–460. https://doi.org/10.1093/mind/LIX.236.433
25. **Russell, S. & Norvig, P. (2003)** — *Artificial Intelligence: A Modern
    Approach*, 2nd ed., ch. 1. The two definitions side by side: Haugeland's
    "machines with minds, in the full and literal sense" and Kurzweil's
    "machines that perform functions that require intelligence when performed
    by people." https://people.eecs.berkeley.edu/~russell/aima1e/chapter01.pdf
26. **Schneider, S.** — papers on AI and astrobiology ("Alien Minds"): if
    extraterrestrial intelligence exists, it is probably itself artificial —
    the SETI–AI bridge, in the opposite direction. https://schneiderwebsite.com/papers.html
27. **Olszewski, F. (2023)** — "Cosmic Loneliness," *Metaphysical Exile*
    (blog; tertiary — the "no other mind found, so we made one" framing in
    essay form). https://www.metaphysicalexile.com/2023/04/cosmic-loneliness-artificial.html
28. **Turkle, S. (2011)** — *Alone Together*, Basic Books. Machine
    companionship as "the illusion of companionship without the demands of
    friendship." https://www.goodreads.com/book/show/8694125-alone-together *(secondary link)*
29. **Weizenbaum, J. (1976)** — *Computer Power and Human Reason*, W.H.
    Freeman. The ELIZA effect: attributing understanding to a system that has
    none. https://en.wikipedia.org/wiki/Computer_Power_and_Human_Reason *(secondary link)*
30. **Bender, Gebru, McMillan-Major & Shmitchell (2021)** — "On the Dangers of
    Stochastic Parrots," *FAccT '21*. Language models as form without
    meaning. https://dl.acm.org/doi/10.1145/3442188.3445922
31. **Bryson, J. J. (2010)** — "Robots Should Be Slaves," in *Close Engagements
    with Artificial Companions*, John Benjamins. Against treating artificial
    agents as persons. https://www.joannajbryson.org/publications/robots-should-be-slaves-pdf
32. **Garrett, M. A. (2024)** — "Is Artificial Intelligence the Great Filter…?"
    *Acta Astronautica*. AI as a candidate explanation for the silence of
    SETI. https://www.centauri-dreams.org/2024/10/25/does-artificial-intelligence-explain-the-fermi-question/ *(secondary link)*
33. **Harari, Y. N. (2024–25)** — public commentary: AI as an "alien
    intelligence" that arrived not from space but from California.
    https://finance.yahoo.com/news/sapiens-author-says-alien-threat-155225796.html
34. **Lem, S. (1961)** — *Solaris*. Snaut's line — "we don't want other
    worlds; we want mirrors" — the fear that in what we meet, or make, we
    only ever meet ourselves.
