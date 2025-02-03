import hashlib
import random
import string

N = 15

map = {}

for i in range(1_000_000_000):
    input_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

    md5_hash = hashlib.md5(input_string.encode()).hexdigest()

    binary_hash = bin(int(md5_hash, 16))[2:].zfill(128)

    first_40_bits = binary_hash[:40]

    if first_40_bits in map:
        print(f"Found after {i} tries")
        print("First string: ", input_string)
        print("Second string: ", map[first_40_bits]["source"])

        print("First hash: ", md5_hash)
        print("Second hash: ", map[first_40_bits]["hash"])
        break

    map[first_40_bits] = { "hash" : md5_hash, "source": input_string }
