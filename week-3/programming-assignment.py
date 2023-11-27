# We're building a hashing algo for a video file, where we break the file up into 1KB chunks and then hash each chunk,
# starting from the final one. We hash the chunk, then append it to the previous chunk, and hash that, and so on.
# Our test is 

import sys
import os
import hashlib

if len(sys.argv) != 2:
    print("Specify filename to hash")
    sys.exit(1)

file_name = sys.argv[1]

if not os.path.isfile(file_name):
    print("File does not exist")
    sys.exit(1)

# Read file into memory
file_data = []
with open(file_name, 'rb') as f:
    while (chunk := f.read(1024)):
        file_data.append(chunk)

# Hash each chunk, append, and move on
# Normally we'd store it, but we just want the last bit for the assignment
running_hash = None
for chunk in reversed(file_data):
    if running_hash:
        chunk += running_hash
    running_hash = hashlib.sha256(chunk).digest()

print("Found Hash of File", file_name)
print(running_hash.hex())