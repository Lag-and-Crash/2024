from secret import flag
from random import randint
from Crypto.Util.number import isPrime
from math import gcd

# https://en.wikipedia.org/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem
def gen_pub(n):
    W = []
    s = 0
    while len(W) < n:
        w = s + randint(2, 1337)
        W.append(w)
        s += w
    q = s*2
    while not isPrime(q):
        q = randint(2*s, 3*s)
    r = randint(2, q)
    assert gcd(r,q) == 1
    pub = [r*w % q for w in W]
    return pub

assert len(flag) == 24
for i in range(0, len(flag), 6):

    fblock = flag[i:i+6]
    pub = gen_pub(len(fblock)*8)
    ct = 0
    m = int.from_bytes(fblock, "big")

    cnt = 0
    while m:
        ct += (m & 1) * pub[cnt]
        cnt += 1
        m >>= 1
    print(f"pub{i//6} = {pub}")
    print(f"c{i//6} = {ct}")
