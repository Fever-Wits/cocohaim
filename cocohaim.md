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
