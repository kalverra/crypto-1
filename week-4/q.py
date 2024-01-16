def hex_to_ascii(hex_string):
    """Converts a hexadecimal string to ASCII."""
    try:
        ascii_string = bytes.fromhex(hex_string).decode('utf-8', 'replace')
        return ascii_string
    except ValueError as e:
        return f"Error: {e}"

def ascii_to_hex(ascii_string):
    """Converts an ASCII string to hexadecimal."""
    try:
        hex_string = ''.join(format(ord(char), '02x') for char in ascii_string)
        return hex_string
    except Exception as e:
        return f"Error: {e}"
    
def xor_strings(str1, str2):
    """XORs two strings of possibly different lengths."""
    max_len = max(len(str1), len(str2))
    
    # Pad the shorter string with spaces to match the length of the longer string
    str1 = str1.ljust(max_len, ' ')
    str2 = str2.ljust(max_len, ' ')

    result = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(str1, str2))
    return result

encrypted = "20814804c1767293b99f1d9cab3bc3e7 ac1e37bfb15599e5f40eef805488281d"
decrypted = "Pay Bob 100$"
new = "Pay Bob 500$"
decrypted_hex = ascii_to_hex(decrypted)
new_hex = ascii_to_hex(new)
new_encrypted = xor_strings(xor_strings(encrypted, decrypted_hex), new_hex)
print(new_encrypted)
