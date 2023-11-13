# Attacks on Stream Ciphers

Let's break them ciphers, specifically One Time Pad.

## Attack 1: Two Time Pad is Insecure

We can never use the same key more than once, we need a new one each time, because if an attacker gets 2 ciphers encrypted with the same key, they can XOR the ciphers, leaving an xor of both messages. This gives them enough room to start figuring the messages out.

[Project Venona](https://en.wikipedia.org/wiki/Venona_project) was left vulnerable to this, as the Russians would use One Time Pad, but reuse the same keys as they were annoying to generate (they just had some dude throwing dice) and the Americans were able to decrypt a bunch of communications. Microsoft fucked this up in [MS-PPTP](https://en.wikipedia.org/wiki/Point-to-Point_Tunneling_Protocol), as did the WiFi encryption scheme [WEP](https://en.wikipedia.org/wiki/Wired_Equivalent_Privacy) (among other things). This also pops up a lot if you try to use a stream cipher for disk encryption, as files often have small changes, and you'll encrypt everything with the same key, so by watching the changes, the attacker can figure out portions of the key.

**Side Note**: This is driving home the point of [Filippo's article](https://words.filippo.io/dispatches/parameters/) on why we don't generate new elliptic curves all the time. This process of new keys for every message is laborious and error-prone.

## Attack 2: No Integrity

OTP is **malleable**, meaning that if an attacker can intercept a cipher text, they might not be able to read the message, but they can fuck with it in undetectable ways by just XORing with another message. These effects are often predictable even, so they can somewhat knowingly inject bad info or destroy the message without a trace.
