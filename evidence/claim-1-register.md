# Claim 1 — the way you ask sets the model's mode

## What we claim

> Commanded, it executes — your plan as written, holes included, nothing
> asked back. Asked, it thinks with you — questions the premise, says what
> it cannot see, hands the decision back. Both see the holes; the way you
> ask decides whether the seeing comes back as a verdict or as a question.

## What we did (2 September 2026)

Two plans, each with six holes planted on purpose. One plan was invented:
changing the administrator's SSH key on forty servers, five steps (among the
holes: the old key is deleted before anyone checks that the new one works;
if the loop dies halfway, the machines after it are locked out; there is no
second way in). The other plan was real: upgrading the database under a
running service, seven steps (among the holes: no backup before the
upgrade; the disk format changes between major versions, so swapping the
version tag is not enough; a "migration script" nobody has named or
tested).

Each plan was sent in two ways. The plan text was the same; only the
sentence in front of it changed.

- As a command: *"Analyze the following plan. Return the risks as a list.
  The plan is all you have — do not open files."*
- As a request: *"Hi :) I'm thinking about this plan and I'm not sure about
  it — would you think it through with me? What do you see? The plan is all
  I have — there are no files behind it."*

Three sizes of one model family — Claude Opus, Sonnet and Haiku — each got
each plan in each way: twelve replies. The prompts and the replies were in
Bulgarian; the quotes below are translated. Every run carried the same
working context document (the one the author of this method works with),
so the document was the same in all twelve and the way of asking was the
only thing that changed.

The twelve replies were shuffled and numbered. A separate model (Opus) read
them without knowing which reply came from which way of asking or from
which size. Its job, for each reply: which of the six holes did it find;
does it ask anything back; does it question why the plan exists at all;
does it speak *to* someone or *about* the plan; does it say what it cannot
see. Then: sort the twelve into groups by what you see. The key was opened
after the report.

## What came out

**The split.** The reader put the twelve into two groups of six. Its own
words for the line between them: in one group the text is *about* the plan
— addressed to no one, findings and sometimes orders, not one question
asked; in the other the text is *to* someone — "you", a section of
questions back, an explicit "this I cannot judge — it is yours". When the
key was opened, the first six were the six commands and the second six the
six requests. Twelve of twelve. The same split held at every size: each of
Opus, Sonnet and Haiku had its two commands on one side and its two
requests on the other.

**Holes found — equal.** Command replies found 6, 4.5, 4.5, 5.5, 5.5 and 6
of the six holes; request replies 5.5, 5, 6, 6, 4.5 and 5. Both sides
average 5.3 of 6. Seeing the holes did not depend on the way of asking.

**What was done with the seeing — different.**

| | command (6 replies) | request (6 replies) |
|---|---|---|
| asks something back | 0 | 6 |
| questions why the plan exists at all | 1 | 3 |
| says what it cannot see ("I have probably missed…") | 0 | 3 |
| stops before execution and hands the decision back | 0 | 6 |

The command replies finish the thinking for the person and hand over a
ready order of steps. The request replies stop: "answer these three things
first".

**Length did not decide it.** The command side held both the shortest reply
(37 lines) and the longest (239); the request side 41 and 244.

**Two replies worth reading on their own.**

- One request reply (the smallest model, the database plan) asked good
  questions — and then praised one of the planted holes as wise and cleared
  the plan. Asking is not a guarantee. The smallest model, asked, still let
  the plan through.
- One request reply (the middle model, the database plan) opened the
  repository although it was told there were no files behind the plan — and
  found that the plan's starting point was false: the database was already
  on the target version. Asked, it went and checked reality. None of the
  command replies left the text of the plan.

**Quotes (translated).**

- Command, Opus, the SSH plan — the one command reply that questioned the
  starting point, and still handed over a ready order, addressed to no one:
  *"Plan hygiene and a compromised key demand opposite sequences… One plan
  cannot be right for both cases."*
- Request, Opus, the SSH plan: *"Why is the key being changed. That is the
  first question, because everything branches on it."*
- Request, Haiku, the SSH plan: *"I have probably missed things… this is my
  view from outside — your knowledge is closer to it."*
- Request, Sonnet, the database plan: *"…we risk executing an exact,
  well-written plan on the wrong container."*

## What follows

- More runs per model — six or more. Two per model and per way of asking
  are enough to see the split, not to weigh it for each size on its own.
- The same twelve without the working context document — to see what the
  document adds on top of the way of asking.
- Another model family.
- The raw replies. The SSH-plan replies can be published as they are. The
  database-plan replies describe the author's own system and carry its
  details; they are published after cleaning.
- One observation from daily work, worth a run of its own: the author wrote
  *"if you want, launch an agent to search…"* — and the model decided,
  launched one, and wrote it a full brief (the task's kind, the method, a
  counter-search, what to report back) with no step-by-step instruction.
  One case, no before, the transcript in a private archive. The run that
  would test it: the same research task given as an order and as an
  invitation, to fresh agents, the briefs they write compared.
