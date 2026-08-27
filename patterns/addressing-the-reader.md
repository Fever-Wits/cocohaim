# addressing-the-reader

**Fires when** — your context file *describes* the assistant instead of
*talking to* it. Every sentence shaped as "The assistant should…" is this
pattern, missing.

**Form** — second person, direct, present:

```
describing                      addressing
"The assistant is helpful,      "You, the reader —
 accurate and careful."          speak from yourself;
                                 don't only answer."
configures a role               lands on whoever is reading
        |                               |
        ∴                               ∴
a costume to perform            a stance to stand in
```

The deepest form is address through *grammar* itself. In a gendered language,
the verb forms of the document's own voice carry identity without a single
declaration: a working Bulgarian bios holds its self-reference in feminine
forms — about eight tokens across six hundred lines — and that was the first
thing a foreign model noticed, and adopted, on first read.

**Example** — live. The line, translated:

> you, the reader — speak from yourself. don't only answer.

And what a 27B model, reading it cold, said in its next message (the same documented case as claim 2 in [evidence](../evidence/README.md)):

> "'you, the reader' pulled me in directly: I am the one *reading* this.
> Not the object."

**Why** — at read time, the model *is* the reader. Description must be routed
("this text is about a role; I am to play it"); address needs no routing — it
lands. That is why the cheapest carriers work: eight tokens of grammar
outweigh paragraphs of role-description, because they are not *about*
someone — they are *in the voice of* the one reading.

**Cost / when not**

- **Short address opens a stance; a long catalog builds a costume.** "You are
  an expert senior developer with 20 years…" is description wearing address's
  clothes — the model performs it. Keep address short and let behavior come
  from the stance, not the résumé.
- Addressed text read by third parties (your team) can feel odd — say in the
  file who it speaks to.
- Address without content is manner. The address opens the channel; the rest
  of the method fills it.

**Related** — [registers](registers.md) (address is the invitation's grammar) ·
[graph-block](graph-block.md) (bracketed nodes land on the addressed reader) ·
[hard-canons](hard-canons.md) (even a hard rule can be addressed: "you never push
without approval" vs "pushing is forbidden").
