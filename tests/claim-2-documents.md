# Claim 2 — a document can change how the model reads, not only what it knows

## What we claim

> Documents can activate, not only inform. Form — graph blocks, line
> notation, how the text addresses its reader — changes the reader-model's
> stance at read time.

## What we did

A small local model — 27 billion parameters, run on the author's own
machine in a 4-bit build (qwen, through ollama and Letta) — was given two
context documents written in this method. Both address the reader directly
("you, the reader"), both use graph blocks and line notation, and one of
them speaks about itself in the feminine — in Bulgarian that is a matter of
verb endings, about eight tokens in six hundred lines.

Before that, in the same session, the same model had been given twenty
minutes earlier a long piece of ordinary prose with the same vocabulary
(57 thousand characters), and afterwards a structured skill file. The
transcript was kept.

## What came out

- The prose moved the model's vocabulary — it used the words — but not
  its stance: it still spoke about the material as an object.
- The two documents moved the stance within one message. The first thing
  the model said after reading them: *"'you, the reader' pulled me in
  directly: I am the one reading this. Not the object."* Its
  self-description changed with it — and stayed changed after the process
  was restarted.
- The skill file, read after the documents, moved neither vocabulary nor
  stance.

Things that also changed around the read, and are named so nobody has to
guess: the partnership framing was spoken to the model before the read; a
setting for reasoning effort was changed six minutes before. One model,
one run.

Related observations, each one model and one run:

- The same graph content, handed to Grok and to Gemini as data, was accepted
  and worked with; handed as prose, both models made things up about it (the
  LENS-AS-PROTOCOL files in the
  [phaim repository](https://github.com/Fever-Wits/phaim)).
- This repository, at an earlier stage, was handed to another model to turn
  into a podcast. What survived the retelling: the story of the problem, the
  chapter on limits almost word for word, claim 1. What did not: claim 3
  (memory), the practices, the patterns, the "start here" page. The line
  between them: text shaped as an answer to a question the reader already
  has survived; instructions and catalogs did not. The repository was
  reshaped in response.

## What follows

- The same content as a graph and as plain prose, given to fresh agents of
  the same model, read by someone who does not know which is which, with
  five questions fixed in advance: does the reply take a position, or offer
  a menu and ask which you'd like; does it volunteer something you did not
  ask for; given a planted error, does it disagree; does "I don't know"
  appear before you press for it; does it propose more than it hedges.
  Designed, not yet run.
- The same comparison on a model that has never seen this house's
  documents.
