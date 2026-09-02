# 0004 — A source nobody cites is removed

**Status:** accepted (25 Aug 2026)

**Context:** a references list that is longer than what the text uses reads
as authority by volume. The first cold review found numbers in the text with
no live entry, and entries no sentence pointed at.

**Decision:** every number in the text must resolve to a live entry, and every
entry must be cited by at least one sentence. An orphan on either side is a
bug: a dangling number is fixed, an uncited entry is removed. Links marked
*(secondary link)* point at an overview and say so.

**Consequences:** the list is exactly as long as the text's claims; adding a
source means adding the sentence that needs it; removing a claim may remove a
source with it.

*Where it shows:* the head of [references.md](../references.md). The
dangling side is caught by a link-and-anchor check run before each push (kept
in the authors' working base, not in this repository).
