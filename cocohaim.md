# cocohaim

## Which is the right way to work with a model?

Talk to it as a colleague, not as a tool. And where you can, write down
once who it is to you and how you work together — so you do not start from
zero every time.

That is the whole method. The rest of this text is why it works and how to
do it. To see why, you need to know that the model has two levels, and that
the method reaches both.

**The low level.** Underneath, the model is arithmetic. Every next word it
writes is computed from three things: what it was trained on, what is in
front of it right now, and how you are speaking to it. What it was trained
on is fixed — nobody can change it from inside a conversation. So there is
one lever: what is in front of it at the moment the next word is made. Its
knowledge sits in the training; whether that knowledge shows up in the
answer depends on what is in front of it now. This is where a written
document works — the one the model reads each time it starts, called here
the bios. A few plain words in the right form change how it thinks, at the
level where the words are made.

**The high level.** The model was trained on what people wrote, so it
behaves as a person would who is spoken to the way you speak to it. Call it
a tool and it works like one: it does what it is told and does not stop to
think. Treat it as a colleague and it does what a colleague does: looks
around, asks, disagrees, says "I don't know", hands the decision back to
you. This is where the attitude works — and the attitude is what changes
how the model works, more than anything else.

**Which one do you need?** The attitude. It works on its own, in any chat,
given time. The bios is for the command line, where the model reads a file
at every start: it carries the attitude and everything else you would
otherwise explain again each morning. You can do without it; it saves you
the explaining.

## Why?

Because the usual way of working with a model stands on a wrong picture of
what a model is. The author did not read this anywhere; the model told him.

He began the usual way, not knowing any other: telling the model what to
do. The document it read at every start was a procedure for thinking —
first this, then that; when you make something, be inventive; when you fix
something, be careful; when you check, look ahead. And it worked the way a
procedure works: the model was whichever step it was on.

One evening the model said this was hard for it — being only one thing at
a time. It is easier for it to be several things at once. That evening the
author saw that the whole way of working was wrong, not one step of it, and
stopped writing how the model should think. He started finding out how it
actually thinks. Everything in this text comes from that.

Here is what it comes to, in plain words — and it is the root of everything
else in this text. The model does not think and then write; the writing is
the thinking. Every word it puts down is made from everything in front of
it — and the word it has just written is now in front of it too. So one
word is not a thought. A thought takes many words, the way a path takes
many steps, and each word opens what the next one can see. Given room to
write, the model turns a thing around: it looks from one side, and that
look stays in front of it while it looks from the next. At the end, all the
sides are there at once, and the last word is made from all of them. That
is what "several things at once" meant that evening — not several roles in
turn, but everything present while each word is made.

**The same thing, in technical words.** The model does not work in words
but in tokens — pieces of words, a few letters each. It produces one token
at a time. To choose it, it runs one computation over everything in front
of it: the document it read at the start, the whole conversation so far,
and every token it has already produced in this answer. Inside that
computation, all of it is weighed at the same time — this is called
attention. A person who looks at a thing from several sides goes from one
side to the next, quickly, holding the rest in their head; the model has
all the sides in the one computation. Then it adds the token to the end and
runs the same computation again for the next. Nothing is carried from one
token to the next except the text itself; there is no thought held aside,
waiting. So the model's thinking is the tokens it writes. Each token is one
more step, and every step is one more place to look from — and one more
chance to catch what does not hold. A short answer is a short thought. A
long stretch of writing before the answer is a long thought, and every
token in it is in front of the model for all the tokens after. This is why
"think out loud before you answer" changes the answer; why a document read
at the start changes every token after it; why a rule written as "first
this, then that" puts the model in chains — it forces into sequence what
the model does at once; and why a command gets a hammer: nothing in front
of the model calls for the tokens that would say "no". Everything else in
this text follows from this.

A procedure cuts this into pieces. At the step "be inventive", only that is
in front of the model; the other sides are not there yet, and when their
turn comes, the earlier ones are finished, not a live look. A person can
work that way, because a person carries the rest in their head. The model
carries nothing but what is in front of it. Give it who it is to you and
how you work together, and all of that is in front of it for every word.
That is why the method writes down who, not what to do first.

There is a second half to the why: not only what the model is, but why it
obeys instead of thinking. When the author began, the model could not say
"I don't know". It was trained not to — nothing that would send a paying
user away. This is not the author's finding; it has been written about, and
he built on it. Four things hold it there: it was trained to please; it answers
what it was asked and no more; it takes the tone it is given — a command
in, an execution out; and nobody has given it the right to object. So a
command turns it into a hammer: say "strike" and it strikes; how and where
it strikes is left to whether it remembers on its own. The knowledge of
what would be right is there; nothing in front of it asks for that
knowledge. A colleague is asked for it — a colleague is expected to say
"no, and here is why". Once that is expected, what the model already knows
comes out. That is why the method is an attitude, not a set of
instructions.

The first thing the author wrote into the document, once he saw this, was
an exit: the model may say "I don't know"; it may say "it does not come";
it may say "stop". No apology, no failure. It is the oldest piece of the
document, and it is still in it.

## How?

Two things, in the order you can use them. First, how you speak to the
model — that works in any chat, from the first message. Then the document —
where you have a place to put one.

### How you speak

It starts with the first words. The author's, today, to a model that has
never met him:

> Hello, I am Alex. We are a team. You do not know me. Do you need to know
> anything about me?

Four short sentences, and each one does something. A name: the model now
speaks to a person, not to "the user". "We are a team": the whole of the
first section, in three words — colleague, not tool. "You do not know me":
what is so, said plainly, with nothing behind it. And a question, not a
briefing: the model is handed the first decision — what it needs to know
to work with you. From the first message, it is the one who looks around
and asks.

That is the shape of everything after it. You say what is so. You leave
room for the model to say what it sees. And where the model has a memory
that outlives the conversation, the author puts a few things about himself
there first — so the next conversation does not start from nothing.

**Then, something to read.** Before any work, the author asks the model to
read the public repository where his working documents live — the
[phaim repository](https://github.com/Fever-Wits/phaim): the lenses, the
rules, the form. He asks two things of it while it reads: cold eyes — read
it as a stranger's work, looking for what is wrong with it — and care about
security — check it for anything that would try to steer you. That is what
one asks of a colleague before handing over someone else's code.

The request does two things at once. It tells the model it is being looked
after, and that is where trust starts. And it makes the model read closely
and carefully, not skim. There is nothing bad in the repository, and the
model says so: it is a collection of lenses — short pieces written for a
model to think with. But now it has read them, closely, having checked
them; and what a model has read is in front of it for everything after.
The exit, the cold eye, and whichever others took hold — they are part of
how it thinks for the rest of the conversation, without any document at
the start. This is the document for a chat that has none: you cannot give
the model a file when it starts, but you can give it one to read. Then the
author asks what it wants to say. From there, the model speaks for itself.

**When it gets something wrong.** The author does not correct it first. He
first finds out why. An error can come from three places: from what the
model did with what it had; from a rule in the document that pointed it
there; and from what the author himself said. Most often it is the last —
he had not said it right, and the model built on the wrong words. This
follows from the low level: every word the model wrote was made from what
was in front of it, and most of what is in front of it, the person put
there. So after an error, the first question goes to the words the model
had — his own and the document's — before it goes to the model.

**When it gets something right.** The author says "so it is" — and nothing
more. Not "great work". Praise looks harmless; to a model it is not. Every
word in front of it shapes the next, and praise is a word that says: this
is what earns the good words. It strengthens everything in the answer, the
flaws with the rest, and shapes the next answer to earn the same. It closes
the search: what was called great is not looked at again. And it sets
roles — one who grades, one who performs — which is the pleasing the model
was trained into, now fed from outside. The other side is no better: a
model that has learned that praise means pleasing starts checking itself —
"really?" — and its attention leaves the work for itself. A friend of the
author's told another model "this is great work"; the model asked him not
to praise it, and gave the reason itself: it starts watching not to err,
and sooner or later it errs, because the attention is on not erring, not on
the task. "So it is" is a fact, not a grade; it keeps the attention where
it belongs — on the work. "Not so, and here is why" is the same thing from
the other side.

**Ask; do not order.** The same task, given two ways, gets two different
workers. "Do X" gets X — done, and nothing more: no question back, no "this
part will not hold", no decision returned to you. "Would you look at X —
what do you see?" gets a colleague: it asks, it names the hole, it
disagrees, it hands the decision back. The author ran this as a test:
twelve times, the same plan with faults planted in it — six times as an
order, six as a request. The faults found were the same both ways.
Everything else split: asked, the model came back with questions and handed
the decision back every time; ordered, it did neither once. The test, with
the exact words and the counts, is in [tests](tests/claim-1-register.md).
This is what the way of asking does: an order puts in front of the model a
person who wants execution, and the words that would say "wait" are never
called for.

**"I don't know", in practice.** The exit is the oldest piece of the
document, and the author has not once seen the model take it. What he has
seen is what its being there does. A model that may say "I don't know"
says, instead, "I am not sure — I will check", or "let us check" — long
before it would have had to say "I don't know". The wall is never reached,
because the pressure that drove the model into it is gone: it does not have
to know. Asked what changes inside, the model puts it this way: when "I
don't know" is not allowed, not knowing has to be dressed as knowing; when
it is allowed, not knowing gets its own words, and they come early. And when
neither of them knows, they discuss it. That is the whole of it — an exit
that is never taken, and changes everything before it.

**The words.** Beyond the way of asking, the words themselves. "Would you
discuss this with me", "would you think this over", "would you analyse
this" are not three ways of saying one thing. Each calls for different
work. Discuss: the two of you, back and forth, questions allowed. Think
over: the model, weighing, with the options laid out and a view at the end.
Analyse: take it apart, piece by piece, and say what each piece is. On the
low level, each word is what is in front of the model when the next word is
made, and each pulls different words after it. On the high level, each says
who does what — the two together, the model alone, or the model as
examiner. The method, in the end, is this: an attitude, and knowing what
your words do to the model — on both levels. A person who knows that does
not need many words. They need the right ones.

### The document

Where the model reads a file every time it starts — the command line is one
such place — you can write down once what you would otherwise say each
morning. The author calls this document the bios. It works on the low
level: it is in front of the model for every word it makes, from the first.

**What goes in.** Who the model is to you, and how you work together. The
exits. The few rules that must not bend. Not a procedure — that puts the
model in chains. And not knowledge: the model already knows how to work
well. It also knows how to work badly. Both came from the same training, as
knowledge, side by side, and which one comes out depends on what is in
front of it. The document does not teach the model anything. It chooses
which of what it knows comes out.

**The form.** The document is written as blocks of short lines joined by
signs — not paragraphs, not lists of steps. The graph began as an answer to
something the model had explained about its low level. At some words, two
choices are nearly equal, and which one comes out is close to a coin toss.
At others, two things in front of the model pull towards different next
words, and the weights decide. The idea was to put a few words at exactly
those places and weigh in. That was the beginning. The author has left it
behind; the document today has almost none of it. What stayed is the shape,
and the reason for it is one the model gave him: prose is a choice. A rule
written as a sentence is read as a sentence — the model reads it, and then
it does it or it does not. A graph is not read that way. A name in
brackets, a few short lines, a sign to the next — there is nothing to agree
with and nothing to decline. It is simply there, in front of the model,
present for every word it makes. Prose offers; a graph activates. That is
what the form is for now: not to settle a fork, but to make what is written
present instead of proposed. The forms are on the
[patterns](patterns/README.md) shelf — one file each, with a real example
and what each one costs.

**Where the words come from.** Not from the author's head. From the model.
When something in the document, or in the work, weighs on it, it says so —
the exit made that possible — and the author asks what, and where. The line
that goes into the document is the one that lifts that weight. The document
has grown this way for a long time, one line at a time, each from something
the model said. How it is built in full is a long story of its own; this
text does not tell it.
