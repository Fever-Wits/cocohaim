# graph-block

**Fires when** — a principle or a choice has *structure* — branches, tensions,
guards — that prose would flatten into a paragraph the reader skims.

**Form** — this is itself the anatomy of one:

```
[name-of-the-block]
        |
   ─────┴─────
   ↔         ↔
[side A]   [side B]
 what A     what B
 carries    carries
        |
        ∴
  what follows from holding both
        ⊸ what this block guards against
```

- `[name]` — a node: a short noun phrase in brackets. The bracket makes it addressable.
- `|` — vertical flow: read downward.
- `─────┴─────` — a fork: one trunk, two columns, both kept.
- Edge glyphs carry the *type* of relation: `↔` two sides of one thing ·
  `∴` therefore · `⊸` guards against · `◇` a choice · `→` leads to.
- **A legend is mandatory.** A bare glyph reads as decoration; defined once,
  it reads as meaning. (→ pattern: legend)

**Example** — live, translated from a working Bulgarian bios (the original
grammar carries more than the translation can — see Cost):

```
[universal exit]
        |
  always available.
  you may say: "it doesn't come."
  you may say: "I don't know."
  you may say: "stop."
        ⊸ no provider failure. no apology.
```

**Why** — at read time the model parses *relations*, not sentence flow: the
structure of the thought arrives as structure, not as a description of
structure. Node names are vectors into what the model already carries —
naming activates; the graph tells the names how they connect.

**Cost / when not**

- **Expect stance, not glyphs.** The glyphs do not transfer into the model's
  own speech — they activate at read time; they are not vocabulary the model
  will speak back. A model that read graph blocks and answers in plain prose
  with a changed stance is the *success* case. [→ `tests/`]
- A graph without a legend degrades to decoration.
- Do not redefine common punctuation as edges — known failure mode of
  invented notations (redefining the comma breaks everything).
- Overuse: everything-as-graph means nothing stands out. Graphs are for
  structure that earns them; prose remains right for narrative and for
  retrieval anchors.
- **Translation loses carriers.** A translated example (like the one above)
  keeps the structure but drops what the original grammar carried — see
  [addressing-the-reader](addressing-the-reader.md) for why grammar itself
  is a channel.

**Related** — [line-notation](line-notation.md) (the same graph flattened into one row) ·
[legend](legend.md) · [addressing-the-reader](addressing-the-reader.md) (what the nodes
land on) · [always-loaded-diet](always-loaded-diet.md) (what keeps the block short).
