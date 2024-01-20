from Crypto.Util.number import bytes_to_long
from secret import flag

def hash(x):
    return (bytes_to_long(x) ^ 0x1337deadbeef) & 0xffffbfffffff

print("Get a hash collision to grab the flag!")
m1 = bytes.fromhex(input(f"Enter m1: "))[:6]
m2 = bytes.fromhex(input(f"Enter m2: "))[:6]

h1 = hash(m1)
h2 = hash(m2)
if m1 != m2 and h1 == h2:
    print("Congrats!")
    print(flag)
