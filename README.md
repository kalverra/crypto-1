# Crypto 1

My notes on [Stanford's Cryptography 1 course presented by Coursera](https://www.coursera.org/learn/crypto). These notes are meant for my own personal understanding and chronicling, it's not really intended to be consumed by others. They are riddled with misunderstandings, profanity, and outright incorrect assumptions that I haven't bothered to go back and correct. If you're looking to learn this stuff yourself, you'd be better served by just going to the course.

Things to look at after this:

* [Crypto 2](https://www.coursera.org/learn/crypto2)
* A course on [applied cryptogrophy](https://toc.cryptobook.us/)

## Big Takeaways

* We knew it already, but say it loud for the whole room to hear, **don't roll your own crypto**, shit's hard. Let the PhDs do it.
* "Perfectly Encrypted" is sort a of a fool's game, we're operating off probabilities here, let's make em small. Words like "efficient" and "negligible" are highly dependent on how powerful your computer is.
* The [semantic security](https://en.wikipedia.org/wiki/Semantic_security) game and how [advantage](https://en.wikipedia.org/wiki/Advantage_(cryptography)) works to evaluate the security of encryption schemes.
* Cryptography isn't just about hiding the message, it's also about preventing tampering with the message with things like [HMACs](https://en.wikipedia.org/wiki/HMAC).
