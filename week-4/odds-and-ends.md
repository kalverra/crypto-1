# Odds and Ends

We're near the end of symmetric encryption, so here's a grab bag of stuff.

## Key Derivation

We usually have some source key (e.g. from a RNG), but we need multiple keys for a lot of symmetric encryption schemes. So we uses a Key Derivation Function (KDF). This usually works on app-by-app basis. We have some central source key for a machine that we derive a lot of other keys from, like your SSH key and your video game's DRM key etc. So they all include a "context" to help differentiate keys between different apps, even when they all come from the same source.

20814804c1767293b99f1d9cab3bc3e7 ac1e37bfb15599e5f40eef805488281d
Pay Bob 100$