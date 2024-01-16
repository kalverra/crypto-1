import requests

# https://www.coursera.org/learn/crypto/lecture/8s23o/cbc-padding-attacks
# g = guess for last byte of m[1]
# last byte of c[0] xor g xor 1
# When I do the above, the message will decrypt so that that last byte of m[1] is 1 = m[1]-last-byte xor g xor 0x1
# If g is the correct guess, then we will have a valid pad
# We can then repeat this process to keep guessing the last byte
# using padding that increases with each guess, e.g. 0x1, (0x2, 0x2), (0x3, 0x3, 0x3), etc.
TARGET = 'http://crypto-class.appspot.com/po?er='
OG = "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4"

def hex_to_ascii(hex_string):
    """Converts a hexadecimal string to ASCII."""
    ascii_string = bytes.fromhex(hex_string).decode('utf-8', "replace")
    return ascii_string

def query(q:str) -> int:
  """Query target with q param and return 200 if all good, 403 if invalid padding error, 404 if padding is correct but message is invalid"""
  return requests.get(TARGET + q).status_code

def xor_multi(*to_xor) -> str:
  """XOR multiple hex strings of possibly different lengths"""
  to_xor = [x.replace('0x', '') for x in to_xor]
  print(to_xor)
  for x in to_xor:
     print(x)
     bytes.fromhex(x)
  to_xor = [bytes.fromhex(x) for x in to_xor]
  result = to_xor[0]
  for x in to_xor[1:]:
      result = bytes(a ^ b for a, b in zip(result, x))
  return result.hex()


if query(OG) != 200:
  raise Exception("Invalid OG query")
message = ""
pad_count = 1

# Iterate over all possible guesses
for guess in range(256):
  pad = pad_count * hex(pad_count)[2:]
  q = xor_multi(OG, hex(guess), pad)
  print(q)
  # If we have a valid pad, then we have the correct guess
  if query(q) == 404:
    message = chr(guess) + message
    print(f"Good guess {chr(guess)}")
    break
  
print(f"Found Message: {hex_to_ascii(message)}")