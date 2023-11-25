"""
The goal here is to implement AES encryption and decryption with CBC and CTR modes using the PyCryptoDome library.
But I'm a little confused about the instructions, it says I can use an AES library, but that seems to also be cheating?
Because at least in Pycryptodome (https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html), I'm just flipping
a switch to use CBC or CTR mode. So I'm not sure how I utilize the AES library without skipping the whole assignment?
That's what I would do in a real world scenario, so we're just going to leave it at that.
"""
from Crypto.Cipher import AES

def encode_cbc(key:str, message:str) -> bytes:
  """returns the AES encoded message using CBC mode"""
  parsed_key = bytes.fromhex(key)
  parsed_message = bytes.fromhex(message)
  return AES.new(parsed_key, AES.MODE_CBC).encrypt(parsed_message)

def encode_ctr(key:str, message:str) -> bytes:
  """returns the AES encoded message using CTR mode"""
  parsed_key = bytes.fromhex(key)
  parsed_message = bytes.fromhex(message)
  return AES.new(parsed_key, AES.MODE_CTR).encrypt(parsed_message)

def decode_cbc(key:str, encoded_message:str) -> str:
  """returns the AES decoded message using CBC mode"""
  parsed_key = bytes.fromhex(key)
  parsed_message = bytearray.fromhex(encoded_message)
  iv = parsed_message[:16]
  parsed_message = parsed_message[16:]
  return AES.new(parsed_key, AES.MODE_CBC, iv=iv).decrypt(parsed_message).decode("utf-8", "replace")

def decode_ctr(key:str, encoded_message:bytes) -> str:
  """returns the AES decoded message using CTR mode"""
  parsed_key = bytes.fromhex(key)
  parsed_message = bytearray.fromhex(encoded_message)
  iv = parsed_message[:16]
  parsed_message = parsed_message[16:]
  return AES.new(parsed_key, AES.MODE_CTR, initial_value=iv, nonce=b'').decrypt(parsed_message).decode("utf-8", "replace")

decoded_cbc = decode_cbc("140b41b22a29beb4061bda66b6747e14", "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81")
print("CBC 1")
print(decoded_cbc)
print()

print("CBC 2")
decoded_cbc = decode_cbc("140b41b22a29beb4061bda66b6747e14", "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253")
print(decoded_cbc)
print()

print("CTR 3")
decoded_ctr = decode_ctr("36f18357be4dbd77f050515c73fcf9f2", "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329")
print(decoded_ctr)
print()

print("CTR 4")
decoded_ctr = decode_ctr("36f18357be4dbd77f050515c73fcf9f2", "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451")
print(decoded_ctr)