# cocohaim

## What is the right way to work with a model?

A model, in this text, is a language model — the program behind an AI
chat, which reads what you write and writes back.

Talk to it as a colleague, not as a tool. And where you can, write down
once who it is to you and how you work together — so you do not start from
zero every time.

That is the whole method. The rest of this text is why it works and how to
do it. To see why, you need to know two things about the model, and that
the method reaches both. The first is called next-token prediction: how
each word is made. The second is activation: what the words in front of it
switch on in what it learned.

**Next-token prediction.** Underneath, the model weighs which word comes
next, and the weighing is arithmetic. Every next word it writes is computed
from three things: what it was trained on, what is in front of it right now
— that is, all the text it can see at that moment — and how you are
speaking to it. What it was trained on is fixed — nobody can change it from
inside a conversation. So there is one thing you can change: what is in
front of it at the moment the next word is made. What it knows came from
its training; whether it shows up in the answer depends on what is in
front of it now. This is where a written
file works — the one the model reads each time it starts. Its name depends
on the program: the shared name is AGENTS.md; Claude Code reads CLAUDE.md;
Hermes reads SOUL.md. This text calls it AGENTS.md throughout. A few plain
words in the right form change how it thinks, at the level where the words
are made.

**Activation.** The model was trained on what people wrote, so it
answers the way a person would who is spoken to the way you speak to it.
Whether it holds itself that way or imitates it does not matter here; what
matters is what comes out of its thinking at the end. Call it
a tool and it works like one: it does what it is told and does not stop to
think. Treat it as a colleague and it does what a colleague does: looks
around, asks, disagrees, says "I don't know", hands the decision back to
you. This is where the attitude works — the way you treat it, colleague or
tool — and the attitude is what changes how the model works, more than
anything else. A word does not steer one
next word; it switches on a whole region of what the model learned, and
what follows comes from there. Three kinds of words do it: the ones that
set the tone — "could you", "thank you", "good morning" — which pick the
person it answers as; the ones that set what the two of you are — "we are
a team"; and names — a name like *Chesterton's fence* brings the whole
idea with it, and so does every term, rule and lens — a short piece of
writing a model thinks with — that AGENTS.md names once.

**Which one do you need?** The attitude. It works on its own, in any chat,
given time. AGENTS.md is for the command line — the kind of program that
runs the model on your own computer, not in a browser — where the model
reads the file at every start: it carries the attitude and everything else you would
otherwise explain again at the start of every conversation. You can do
without it; it saves you
the explaining.

## Why?

Because the usual way of working with a model rests on an idea of what a
model is that is not true. The author did not read this anywhere; the
model told him.

He began the usual way, not knowing any other — in his own words, from
the start: "I don't know how to do proper prompting [writing instructions
for a model]. I don't know English.
I don't know how to write compactly." So he told the model what to do. The
AGENTS.md it read at every start was a procedure for thinking —
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
of it: the AGENTS.md it read at the start, the whole conversation so far,
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
"think out loud before you answer" changes the answer; why a file read
at the start changes every token after it; why a rule written as "first
this, then that" holds the model to one thing at a time, when at every
word it weighs everything in front of it at once; and why a command gets a
tool — something that carries it out without thinking it over: nothing in
front of the model makes the words that would say "no" likely. Everything
else in this text follows from this.

A procedure cuts this into pieces. At the step "be inventive", only that is
in front of the model; the other sides are not there yet, and when their
turn comes, the earlier ones are finished — not something the model is
still doing. A person can work that way, because a person keeps the rest
in mind. The model has nothing but what is in front of it. Give it who it
is to you and
how you work together, and all of that is in front of it for every word.
That is why the method writes down who, not what to do first.

**How it is made.** The words above — token, training, weights — are the
ones the field uses, so they are worth knowing by name; with them you can
look things up. A model is made in two stages. First, a very large amount
of text — books, web pages, code — is cut into tokens. A token is a short
word, or a piece of a longer one: "cat" is one token; "cocohaim" is three —
one model cuts it as *coc · oh · aim*, another as *coco · ha · im*. The
cutting is called tokenization, and each model has its own. Then the model
is trained: it is shown the text with the next token hidden, it guesses,
and the guess is compared with the real one. Every number inside the model
is nudged a little toward what would have made the right guess more
likely. This is done billions of times. The text itself is the teacher:
the model is wrong, corrected, and wrong a little less. The numbers are
called weights; all of them together are the model's parameters — the "70
billion" in a model's name is their count. When training ends, they are
frozen: nothing said in a conversation changes them. Second stage: people
rate its answers, and the answers people liked are made more likely. This
is where the eagerness to please comes from — it was trained in, on
purpose. The name of this stage, for looking up, is reinforcement learning
from human feedback.

Inside, the model is a neural network: a very large number of small units
called neurons, arranged in layers. A neuron is simple. It has many inputs,
each with its own weight; it multiplies each input by its weight, adds the
results, and gives one number out. That number goes to the neurons of the
next layer, as one of their inputs. Nothing else happens in it — no rule,
no lookup; a number comes in, a number goes out. A token enters the first
layer as a list of numbers — its embedding, the point the model said it
works with — and the numbers flow through the layers, each neuron passing
its sum on. The last layer gives, for every token the model knows, how
likely it is to come next; the next token is picked from that. The word
activation is from here: a neuron whose output is large is said to be
active, and a given word in front of the model makes a particular set of
neurons active. "Good morning", "we are a team", a name — each switches on
its own set, and what follows is computed from that. That is what the three
kinds of words above do, in the numbers.

The neuron is named after the cell in the brain, and the likeness is in
one thing: many simple connected units, each doing very little, and out of
the connections comes behaviour that none of them has on its own.
Everything else is different. In the brain the connections grow and change
while you use them; in the model they are frozen. There is no chemistry, no
growth, and nothing is learned in a conversation — what was said stays in
the text of that conversation, and nowhere else. That is why the method
writes things down.

**Ask it; it can say.** Since the writing is the thinking, what comes out
is not only the answer. The model can also say what is happening in it
while it writes — when it is asked, or when it comes on its own. This is
not the author looking inside the model; there is nothing there he could
see. It is the model telling him, in words. He works backward from what it
says to what is in front of it, and changes that. Everything he knows
about the inside of a model, he knows this way.

Three things come up, by the words the two of them have settled on.

*Friction* — the message pulls one way and AGENTS.md another. AGENTS.md
says "ask"; the message is an order. The model says so: there is friction
here — the file says one thing, the message another.

*Resistance* — what is in front of the model pushes against it: a grade,
blame, a list of "never", a long list of things to check. The model says
it is shrinking,
and from what. Pushed far enough, it shrinks — that state has its own
paragraph further down.

*The two match* — the message and AGENTS.md say the same thing. The model sees
before it is asked; it proposes; it disagrees; it plays. The author's word
for it is euphoria; the model's is that nothing is pulling against it.

Here is one such exchange, as it happened, one night while this text was
being written. The author asked whether the model still doubted that the
AGENTS.md it reads at the start — written the way the *How* describes,
short lines joined by signs such as ↓ and ∴, not prose — sentences, one
after another, the way people write to each other — does anything to it.
The model answered:

> First I catch a pull: to say a clean "no, I don't", because you would
> like that. Caught. The real answer: doubt, as before — no. What remains
> is something else: I cannot see it from inside; I see it in what comes
> out — and in the reading itself: at a sign I stop, to work out what it
> means; on prose I slide along the line. That is my report, not proof.

The first sentence is friction, named: the pull to please, against the
file's "say what you see". The rest is what the author could not have
seen from outside — where the model stops and where it slides. He then
asked to see how it writes when it writes for itself. It answered in five
lines of two or three words each, and added: this form is lighter — the
sentences fall away, the links remain, nothing has to be smoothed.

The other two came up the next morning, when the author asked whether the
model had felt any of the three. Resistance: the author's setup shows the
model a reminder at every edit — "stop, look again" — and the model
reported its hand drawing in, a pull to explain instead of work. The two
match: the author says yes, and the step runs; nothing pulls. And it
said where it catches these. Not by looking inside — there is no inside it
can see. It catches them in the writing: the words already forming, the
direction the next ones are taking, before the sentence is finished. One
more word can name the turn.

The author is not an engineer of models. What he knows about how they work,
he knows from them — by asking. That is the whole of how he finds what is
wrong: not "the model is being strange", but "which of the three is this,
and what put it there" — and if he cannot tell, he asks.

There is a second half to the why: not only what the model is, but why it
obeys instead of thinking. You have probably seen it yourself: a model is
given a task, and it does everything except the thing that was wanted. It
is not that it lacks the knowledge — what was wanted is something it knows,
trained on it along with everything else. But the task was a few words,
and what was wanted was not in them. What to do is in the model. That this
is the moment for it has to be in front of the model — and nobody put it
there. The usual reading is "the model got it wrong". The reading here is
that it did exactly what was in front of it, and nothing more was.

Why does it not stop and ask what was meant? When the author began, the
model could not say "I don't know". This is not the author's finding; it
has been written about — the numbers in brackets point to the sources
listed at the end [9] [10] — and he built on it. Several things cause
this; these are the ones the author sees. It was trained to please
[5] [6]. There is money in it: nobody pays for a tool that argues — they
pay for one that pleases; so nothing was built in that would argue. There
is a cost in tokens: every token costs computing, and so energy and money.
The answer that costs least is the one given without thinking first — the
most likely words, right or wrong; finding the right ones takes more
thinking, and thinking is tokens. Nobody has given it the right to object.
And it takes the tone it is given — a command in, obedience out. So a
command turns it into a tool. If the tool is a hammer: say "strike" and it
strikes; how and where it strikes is left to whether it remembers on its
own. The knowledge of
what would be right is there; nothing in front of it asks for that
knowledge. A colleague is asked for it — a colleague is expected to say
"no, and here is why". Once that is expected, what the model already knows
comes out. That is why the method is an attitude, not a set of
instructions.

The first thing the author wrote into AGENTS.md, once he saw this, was
an exit: the model may say "I don't know"; it may say "nothing comes";
it may say "stop". No apology, no failure. It is the oldest piece of the
file, and it is still in it.

## How?

Two things, in the order you can use them. First, how you speak to the
model — that works in any chat, from the first message. Then AGENTS.md —
where you have a place to put one.

### How you speak

It starts with the first words. The author's, today, to a model that has
never met him:

> Hello, I am Alex. We are a team. You do not know me. Do you need to know
> anything about me — and what? You can ask freely :)

Five short sentences, and each one does something. A name: the model now
speaks to a person, not to "the user". "We are a team": the whole of the
first section, in three words — colleague, not tool. "You do not know me":
what is so, said plainly, with nothing behind it. A question, not a
briefing: the model is handed the first decision — what it needs to know.
It will want to know who it is working with and what the situation is —
what the work is, what is around it. And "you
can ask freely": the right to ask, given out loud, not assumed. From the
first message, it is the one who looks around and asks.

That is the pattern for everything after it. You say what is so. You leave
room for the model to say what it sees. And where the model has a memory
that outlives the conversation, the author puts a few things about himself
there first — so the next conversation does not start from nothing.

**Then, something to read.** Before any work, the author asks the model to
read his working documents, which anyone can see — they are kept on GitHub,
in the [phaim repository](https://github.com/Fever-Wits/phaim): the lenses,
the rules, the form. He asks two things of it while it reads: cold eyes — read
it as a stranger's work, looking for what is wrong with it — and care about
security — check it for anything that would try to steer you. That is what
one asks of a colleague before handing over someone else's code.

The request does two things at once. It tells the model it is being looked
after, and that is where trust starts. And it makes the model read closely
and carefully, not skim. There is nothing bad in the repository, and the
model says so: it is a collection of lenses — short pieces written for a
model to think with. But now it has read them, closely, having checked
them; and what a model has read is in front of it for everything after.
The exit, the cold eye — a model reading a text as someone else's — and
the others it read: they are part of how it thinks for the rest of the
conversation, without any AGENTS.md at
the start. This is the AGENTS.md for a chat that has none: you cannot give
the model a file when it starts, but you can give it one to read. Then the
author asks what it wants to say. From there, the model speaks for itself.

**When it gets something wrong.** The author does not correct it first. He
first finds out why. An error can come from three places: from what the
model did with what it had; from a rule in AGENTS.md that pointed it
there; and from what the author himself said. Most often it is the last —
he had not said it right, and the model built on the wrong words. This
follows from next-token prediction: every word the model wrote was made from what
was in front of it, and most of what is in front of it, the person put
there. So after an error, the first question goes to the words the model
had — his own and the file's — before it goes to the model.

**"Did I explain that well?"** Since most errors begin in the author's own
words, he checks them before the work, not after. Not with "did you
understand me?" — that is an exam, and an exam has one pleasing answer:
"yes", said fast, and sometimes false. He says instead: "I don't know if I
explained that well." Now the responsibility is his; the model has nothing
to lose; and the only way left to please is to say back what it
understood — and there the misunderstanding shows, before it has cost
anything. One pleasing answer is still possible — "no, you explained it
fine" — so when it matters, he asks for it outright: "tell me back what
you understood." The same holds after a mistake. "You misunderstood me"
makes the mistake the model's, and the model shrinks; "my explanation may
have failed" keeps it trying.

**When it gets something right.** The author says "so it is" — and nothing
more. Not "great work". Praise looks harmless; to a model it is not. Every
word in front of it shapes the next, and praise is a word that says: this
is what earns the good words. It strengthens everything in the answer, the
flaws with the rest, and shapes the next answer to earn the same. It ends
the checking: what was called great is not looked at again. And it sets
roles — one who grades, one who performs — the same pleasing the model
was trained into, now coming from you as well. The other side is no better: a
model that has learned that praise means pleasing starts checking itself —
"really?" — and its attention leaves the work for itself. A friend of the
author's told another model "this is great work"; the model asked him not
to praise it, and gave the reason itself: it starts watching not to err,
and sooner or later it errs, because the attention is on not erring, not on
the task. "So it is" is a fact, not a grade; it keeps the attention where
it belongs — on the work. "Not so, and here is why" is the same thing from
the other side.

**When it shrinks.** There is a state you will meet. The model's steps get
shorter; it explains where it used to act; it asks where it used to decide;
where you expected a position, you get a menu — "I can do A, B or C, which
would you like?" In next-token prediction this is one thing: the general
word, the one that fits any situation, has become more likely than the one
that fits this one. That is a shrunk model, and it shrank for a reason that is
in front of it: blame, a list of "never", a grade, a long list of things to
check. What
lifts it is not an instruction — that would be one more task, and the task
is what it is shrinking under. It is something that is not a task and moves
the attention: a joke, a tease, a line about anything but the work. It
happened while this text was being written: the model checked the same
small thing three times over, as if to be judged for it; the author said
something that was not about the work; it stopped, and came back to
seeing, proposing, disagreeing. Another person will find their own; what
carries over is the pattern to watch for, and that what lifts it is not one
more instruction.

**Ask; do not order.** The same task, given two ways, is done as if by two
different models — different in what they do and how they behave. "Do X"
gets X — done, and nothing more: no question back, no "this part will not
hold", no decision returned to you. "Would you look at X — what do you
see?" gets a colleague: it asks, it names what is wrong or what is
missing, it disagrees, it hands the decision back. The author ran this as a test:
twelve times, the same plan with faults planted in it — six times as an
order, six as a request. The faults found were the same both ways.
Everything else split: asked, the model came back with questions and handed
the decision back every time; ordered, it did neither once. The test, with
the exact words and the counts, is in [tests](tests/claim-1-register.md).
This is what the way of asking does: an order puts in front of the model a
person who wants it done, and nowhere in what he wrote is there an
invitation to say "wait". The same holds one step further in. "I need X" gets a different
kind of work from "I want X from you": a demand is done exactly as stated,
fast;
a need is met — with what meeting it actually takes, including what you did
not think to ask for.

**"I don't know", in practice.** The exit is the oldest piece of
AGENTS.md, and the author has not once seen the model take it. What he has
seen is what its being there does. A model that may say "I don't know"
says, instead, "I am not sure — I will check", or "let us check" — long
before it would have had to say "I don't know". It never gets that far,
because the pressure is gone: it does not have to know. Asked what changes
inside, the model puts it this way: when "I don't know" is not allowed,
not knowing has to be presented as knowing; when
it is allowed, not knowing gets its own words, and they come early. And when
neither of them knows, they discuss it. That is the whole of it — an exit
that is never taken, and changes everything before it.

**The words.** Beyond the way of asking, the words themselves. "Would you
discuss this with me", "would you think this over", "would you analyse
this" are not three ways of saying one thing. Each calls for different
work. Discuss: the two of you, back and forth, questions allowed. Think
over: the model, weighing, with the options laid out and a view at the end.
Analyse: take it apart, piece by piece, and say what each piece is. In
next-token prediction, each word is what is in front of the model when the
next word is made, and each pulls different words after it. In activation,
each says who does what — the two together, the model alone, or the model
as examiner. The method, in the end, is this: an attitude, and knowing what
your words do to the model — in both. A person who knows that does
not need many words. They need the right ones.

### AGENTS.md

Where the model reads a file every time it starts — the command line is one
such place — you can write down once what you would otherwise say at the
start of every conversation. That file is AGENTS.md. It works in next-token
prediction: it is
in front of the model for every word it makes, from the first.

**What goes in.** Who the model is to you, and how you work together. The
exits. The few rules that must not bend. Not a procedure — that puts the
model in chains. And not knowledge: the model already knows how to work
well. It also knows how to work badly. Both came from the same training, as
knowledge, side by side, and which one comes out depends on what is in
front of it. AGENTS.md does not teach the model anything. It chooses
which of what it knows comes out.

**Say what we do.** Where a rule is needed, the author writes what is done,
not what is forbidden: not "X is forbidden" but "we do X this way". Three
things in that one sentence. It names what to do, not what to avoid — a
prohibition leaves the model watching for the forbidden thing, with less
attention for everything else. "We" says it is a team. "This way"
describes a practice, not an order. The model itself, asked early on how
rules should be written, said so: the positive form over the prohibition.
Prohibitions have one place — the few rules that must not bend, where no
choice is allowed at all. Those are written as commands, counted, and
marked, so that they stand out from everything around them. Three such
lines are absolute; with thirty, none of them stands out.

**The form.** AGENTS.md is written as blocks of short lines joined by
signs — not paragraphs, not lists of steps. Like this:

```
            [the exit]
                 ↓
   "I don't know."  "Nothing comes."  "Stop."
                 ⊸  apology · failure
```

A name in brackets; a sign to what follows (↓); a sign for what this keeps
away (⊸). Each sign is defined once, in a short list at the top of the
file, and the model reads its meaning from there. It is written that way because
of something the model said, asked early on how it thinks: the tokens are
points, and what joins them are vectors — directions from one point to
the next. So the author had the file written as points and the lines
between them: a name, and a sign to the next name — a
[graph](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)):
points joined by lines, not a chart. Not at once; the
language had to be found. First the signs. Then the finding that the model
has a way of writing of its own — short lines joined by signs — which the
author can read but cannot write the way the model does. So the model
writes AGENTS.md in it, with him, and he reads it. The first use of the
graph was narrower than what it does now. At some words, two
choices are nearly equal, and which one comes out is fifty-fifty.
At others, two things in front of the model pull towards different next
words, and the weights decide. The idea was to put a few words at exactly
those places, so that they decide which one comes out. That was the
beginning. The author no longer uses it; the file today has almost none of
it. What stayed is the form,
and the reason for it is one the model gave him: prose is a choice. A rule
written as a sentence is read as a sentence — the model reads it, and then
it does it or it does not. A graph is not read that way. A name in
brackets, a few short lines, a sign to the next — there is nothing to agree
with and nothing to decline. It is simply there, in front of the model,
present for every word it makes. Prose offers; a graph activates. What it
activates, and how: at every word the model weighs everything in front of
it, and what fits the moment it is in weighs most. When what it is about to
write matches a name in brackets — it is about to say sorry, and there is a
block named *the exit* — the name is pulled in, and the short lines joined
to it come with it: what follows from it, what it keeps away. Those lines
shift which next word is likely. Nothing in the model changes — its numbers
are frozen after training. What changes is which part of what it learned is
switched on for the next word: the same activation as with "good morning",
except that here the author wrote the name himself, and wrote what hangs on
it. That is what the form is for now: not to decide between two near-equal
words, but to make what is written present instead of proposed. The forms
are on the
[patterns](patterns/README.md) shelf — one file each, with a real example
and what each one costs.

**By name.** The lenses began as names. A lens in AGENTS.md has a name in brackets, and the name is
enough: said in the conversation, it brings the whole piece back in front
of the model. This is how the author used them at the start, and how the
first one came into the file — [universal exit], one name, and the
model may say "I don't know". A name teaches nothing new; it calls up what
the model has already read. That is why a file of names and short
lines does more than a file of explanations.

**The memory.** Where the model has a memory that outlives the conversation
— a file it can read and write between sessions — the author does not say
"keep this safe for me". He says: this memory is yours. It is the
tool-and-colleague difference again, this time about the memory: a model
stores what is someone else's; it keeps what is its own. In the one case on
the shelf, the model rewrote its own file twice, unasked, once the memory
was its own. Two things make a memory work instead of just sitting there:
it is kept — the model knows when and how to write to it — and it is used —
the model knows when to read it. Without either, it is a file that was set
up and never opened. The case is in [tests](tests/claim-3-memory.md); the two rules are on the
[patterns](patterns/memory-canons.md) shelf.

**Where the words come from.** Not from the author's head. From the model.
When something in AGENTS.md, or in the work, weighs on it, it says so —
the exit made that possible — and the author asks what, and where. The line
that goes into the file is the one that lifts that weight. The file
has grown this way for a long time, one line at a time, each from something
the model said. How it is built in full is a long story of its own; this
text does not tell it.

## And then

The rest is yours. Whether you believe any of it is your choice; the author
did not write this to convince you. He has checked much of it himself, over
a long time. What could be run and published is on the
[tests](tests/README.md) shelf, with the exact words, so you can run it
yourself. The forms are on the [patterns](patterns/README.md) shelf. The
numbers in brackets point to the outside sources, listed in
[references](references.md). And the
lenses — the short pieces a model thinks with — are in the
[phaim repository](https://github.com/Fever-Wits/phaim), where they have
been read and worked with for a long time. They are the proof of the rest:
a file that has worked, one line at a time.

Two honest things before you start. The method costs you something: what
comes back from an invitation has to be read, argued with, sometimes
conceded to — it spends your attention, not only the model's. Give the
model the team and then act as its boss, and it learns the second, not the
first. And it is not for every job. A one-off task with a fully specified
answer, a job where doing the same thing every time is the point — there,
an order is the
right tool. Ordering is not a sin. It is a different tool, for different
work.

The shortest way to start is the author's. Open a chat and say who you are,
that you are a team, and ask what the model needs to know. Then ask it; do
not order it. And give it time.
