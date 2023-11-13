# Secure Ciphers

Let's actually define what makes a PRG "secure". A PRG can be called "secure" when it is indistinguishable from a truly random function. A truly random function can conceptually have a massive universe, and PRGs will be limited in the subset that they can generate, but if an attacker can't distinguish the output of your PRG from a truly random function, you've made a secure one.

## Statistical Tests

You can run a bunch of different statistical tests on a PRG output to see if it is truly random or not. How you approach this depends on your standards and situation, you could say if there are way more 0s than 1s it's not random. Or too many of the same value popping up, etc. We used to have a fixed set of these and run them against the PRG output, if they couldn't find anything, your PRG was considered secure.

## Advantage

If we run a statistical test `A(x)` on our PRG output, and on a truly random output, we can define **advantage** as the difference in probabilities between the two results. So, the higher the difference, the lower the advantage of the PRG, so the test is able to figure out the PRG. But if it's close to 0, then `A(x)` can't figure it out, and the PRG has a good advantage.

You're a secure PRG if, for all "efficient" statistical tests, the advantage is "negligible". If you include "inefficient" tests, this breaks, but isn't a practical concern. This definition is full of "good enoughs" as it's not known if we can mathematically prove any PRG is secure. If you **can**, you're on track to prove that `P!=NP`.

So we default to something a bit easier to work with, a secure PRG is unpredictable. If, given some previous output, I can start predicting future output reliably (greater than 1/2 + epsilon probability), you're fucked.

## Semantic Security

Most definitions of perfect security in cryptography are super high standards that can't practically be met, or even truly proven. So we can define "semantic security", our standard for "good 'nough", through an experiment. If an adversary sends us 2 messages of the same length, and we encrypt the messages, and send one back, can the adversary tell if we sent the cipher for their first or second message? If they can't tell with some decent level of probability which message the cipher belongs to, we've done a good job, and we're semantically secure if this holds for all "efficient" adversaries.
