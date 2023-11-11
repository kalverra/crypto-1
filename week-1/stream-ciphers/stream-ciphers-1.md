# Stream Ciphers 1: One Time Pad

A cipher is defined over a pair of algorithms, `E` and `D` such that `E` takes a key and a message, and produces a cipher, and `D` takes a key and a cipher and reproduces the message. This should hold for all possible values of the message, key, and cipher. `E` is often randomized, injecting random values into the process, but `D` is always deterministic.

`M` = Message Space

`C` = Cipher Space

`K` = Key Space

## One Time Pad

The first example of a secure cipher, where `M = C = {0, 1}^n` and the key space is the same, `K = {0, 1}^n` where the key is a random string of bits that is as long as the message. For One Time Pad, the encryption algorithm is just an XOR: `C = E(K, M) = K XOR M`, same with decryption, `M = D(K, C) = K XOR C`.

OTP is insanely fast, just a simple XOR, but the keys have to be super long, as long as your message, and you need a new key for each message, and usually need to send it along the same channel.

## Information Theoretic Security

How secure are these encryption methods? [Claude Shannon](https://en.wikipedia.org/wiki/Claude_Shannon) is the "father of [information theory](https://en.wikipedia.org/wiki/Information_theory)", and determined that the cipher text should reveal no information about the plain text.

A cipher has **perfect secrecy** if, when I catch `c`, `Pr[E(K, mn) = c]` is the same for all messages `m`, so it's a uniform distribution of chances that I could guess the correct message. So if I have just the cipher, I shouldn't be able to learn anything about the message. So **cipher text attacks are impossible** (but not all other attacks, we'll get to that). One Time Pad is such a method that has perfect secrecy. The issue is that Shannon also says that any cipher with perfect secrecy has the issue that the length of the key must be greater or equal to the message sent, which complicates things. You need to send both the key and the cipher, and if you have to send both along the same channel, and it's compromised, you've defeated the whole purpose. This is called the "Bad News Lemma".

## Stream Cipher: Let's Make OTP Practical

First step is to replace our perfectly random key with a pseudorandom one. So now we get to know the math stuff behind pseudorandom, specifically, a pseudorandom generator can be defined as a function `G({0, 1}^s)` where the input is considered the "seed space", and the function will produce `{0, 1}^n` where `n` is much larger than `s`. So we can take a small seed space (e.g. current timestamp), and expand that into a much greater amount of results with our function `G`.

Alright, so let's use our seed as our key. Run the seed through the pseudorandom generator, use the result as our "real key" that we XOR the message with. This gives us smaller keys, but we are no longer **perfectly secure**, our keys are shorter than our messages, and this is the case with all stream ciphers, where the security is often based on how good your pseudorandom generator is. Ideally it is **unpredictable**, as a predictable pseudorandom generator is one where, given the first `i` bits of output, I can figure out the next `n`. Even if `n` is only 1 greater than `i`, it's an issue as I can start extrapolating. An unpredictable one is where there exists no "efficient" algorithm that is able to predict the next bit of information for some "non-negligible" probability. "Non-negligible" and "negligible" probability mostly depend on who you ask, and how big your message is. 