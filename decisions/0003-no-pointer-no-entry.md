# 0003 — No pointer, no entry

**Status:** accepted (26 Aug 2026)

**Context:** lists of advice grow by accretion — a line is added because it
sounds right, and nothing in the list says what it costs or where it came
from. A reader then cannot tell a rule that was paid for from one that was
merely liked.

**Decision:** a line enters a practice list only with a pointer to its cost
(when it fails, what it takes); a measured claim enters the text only with a
numbered source in [references](../references.md). A line without a pointer
is not added, and an existing one without a pointer is a bug.

**Consequences:** the lists grow slower and stay checkable; contributors are
asked for the pointer before the wording; the cost of a practice is visible
next to the practice, not in a separate caveat section.

*Where it shows:* the footer of [practices.md](../practices.md) ("Adding a
line") · the head of [references.md](../references.md).
