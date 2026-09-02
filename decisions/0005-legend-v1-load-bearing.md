# 0005 — Legend v1 carries load-bearing entries only

**Status:** accepted (25 Aug 2026)

**Context:** the working base behind this document uses a wider glyph
vocabulary than the public text needs, and the same glyph carries different
meanings in different document families. Publishing the whole vocabulary
would hand the reader entries with no example to learn from, and glyph
collisions with no way to resolve them.

**Decision:** the public legend is versioned (v1, dated), scoped to its
namespace, and lists only the edges that carry load in the published text.
An entry earns its place by being used, not by existing elsewhere. The arrow
`→` is scoped: an edge in graphs, "see" in prose cross-references.

**Consequences:** the legend is short and every entry has a live example; a
new glyph enters with the first text that needs it, and the version moves;
the private vocabulary is not a promise about the public one.

*Where it shows:* [patterns/legend.md](../patterns/legend.md), the `edges
(v1 · 2026-08)` block.
