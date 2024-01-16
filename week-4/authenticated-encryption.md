# Authenticated Encryption

* We know how the encrypt messages with stream and block ciphers so we have **confidentiality**
* We know how to ensure **integrity** so that no one has tampered with a message with MACs

So if we need just message integrity, but no secrecy, a MAC works pretty well on its own. But if we want secrecy, we also need integrity, so we need a scheme that puts these together, enter authenticated encryption. These systems sometimes include a "bottom" symbol in their decryptions that will indicate that the decryption should not be trusted, has been tampered with, or is otherwise invalid. These are meant to ensure the usual semantic security, but also **ciphertext integrity**. So if our attacker gets access to tons of plain text and ciphers, he still wouldn't be able to construct a valid ciphertext.

## Attacks

This does still leave us open to a replay attack (you can intercept a message, and just resend it a bunch of times and it'll look valid). It does however save us from a chosen ciphertext attack where I can build or modify valid ciphertexts to trick someone into decrypting them for me. Authenticated encryption has chosen ciphertext security.

First thought is we just slap a MAC on a CBC cipher and call it a day, but not all MAC-Encryption combos work well (you want to stick with encrypting the message, then do a MAC on the cipher, enc-then-mac). The other way around opens you up to a bunch of attacks.

There's then an exploration of how earlier TLS versions worked. It's interesting, but I won't note it here, just the takeaways:

* Using a "chained IV", where the IV for your next message is chosen based on your last message, is not CPA secure, and can be exploited with a [BEAST attack](https://www.acunetix.com/blog/web-security-zone/what-is-beast-attack/).
* Don't give information out as to WHY decryption failed. Similar to why giving detailed error messages when a user fails to login is a bad idea: you're revealing info. Just say "you fucked up" and leave it at that.