from Crypto.Util.number import bytes_to_long, long_to_bytes
from os import urandom

def hash(x):
    return (bytes_to_long(x) ^ 0x1337deadbeef) & 0xffffbfffffff

m1 = urandom(6)
m2 = long_to_bytes(bytes_to_long(m1) ^ 0x40000000)

print(f"m1 = {m1.hex()}")
print(f"m2 = {m2.hex()}")

h1, h2 = hash(m1), hash(m2)
print(m1 != m2 and h1 == h2)

# soln:
# & 0xffffbfffffff is a bitmask;
# bin(0xff...) is 0b111111111111111110111111111111111111111111111111, 
# and the & means any binary value that lies on the `1` passes through, whereas that which lies on `0` just terminates
    
# what this means, is that:
# 0b11111111111111111 0 111111111111111111111111111111 & 0xffffbfffffff
# 0b11111111111111111 1 111111111111111111111111111111 & 0xffffbfffffff
# both give the same value.
# note the 1s in the first line doesnt matter and can have any value
# for example,
# 0b01101110110000001 0 111010010010011001100011001111 & 0xffffbfffff
# 0b01101110110000001 1 111010010010011001100011001111 & 0xffffbfffff
# both give the same value too!
