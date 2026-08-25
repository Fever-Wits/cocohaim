# always-loaded-diet

**Fires when** — the context file grows. Concretely: every time a line is about
to enter it "just in case".

**Form** — four rules, each with teeth:

- **The removal test, per line:** *would removing this cause mistakes?*
  If not, it does not enter. (The vendor's own canon for CLAUDE.md files —
  [REFERENCES #3](../REFERENCES.md).)
- **Short core, heavy depth behind triggers.** Always-loaded text carries only
  what applies always; domain material lives behind explicit reach ("when X,
  load Y") — the progressive-disclosure ladder: discovery → activation →
  execution.
- **The emphasis budget:** emphasize many lines and none stands out. IMPORTANT
  survives only where it is rare.
- **TIGHT ≠ SHRUNK** — the two feel identical from inside and are opposites:
  cutting *words per node* sharpens; cutting *nodes and branches* deletes
  structure (a fork collapsed into a summary stops firing). When tightening,
  ask which one you are doing. Cut width, never depth.

**Example** — from the measured world: bloated always-loaded files cause the
model to ignore the instructions in them (vendor documentation, verbatim
warning — [REFERENCES #3](../REFERENCES.md)); excessive procedure is the
leading cause of agent regressions in a 307-failure study — 62.6%
([#1](../REFERENCES.md)); retrieval accuracy across skills collapses from
29.6% to 3.3% when the pool grows from 5 to 100 ([#2](../REFERENCES.md)).
And from the working base this method grew in: an always-loaded core of ~600
lines has carried months of daily work — density by *form* (graphs, rows,
legend), not by volume.

**Why** — attention is a budget: every always-loaded token competes with every
other for the model's recall at the moment it matters. The whole expressive
layer of this method — graph blocks, line notation, the legend — exists to
spend fewer tokens per unit of activation. The diet is not an accessory to
the language; it is the pressure that shaped it.

**Cost / when not**

- The diet is not minimalism for its own sake — a load-bearing line stays even
  if it is long; the removal test protects it.
- Applied with the wrong knife (SHRUNK instead of TIGHT) the diet kills the
  very structure that activates.
- One-off prompts need no diet — the budget matters where text is loaded on
  every step of every session.

**Related** — [graph-block](graph-block.md) · [line-notation](line-notation.md) (the
compression forms) · [legend](legend.md) (entries earn their place) ·
[memory-canons](memory-canons.md) (depth behind reach instead of in-context bulk).
