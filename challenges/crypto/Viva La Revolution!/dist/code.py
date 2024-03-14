import random
from Crypto.Util.number import bytes_to_long, isPrime

VQTR = b"LNC24{answer}"

def X9sm_4sF(zWQ):
    p, q = 0, 0
    while not isPrime(p):
        p = random.getrandbits(zWQ) + random.getrandbits(zWQ // 20)
    while not isPrime(q):
        q = random.getrandbits(zWQ) + random.getrandbits(zWQ // 10)
    return p, q

dL = bytes_to_long(VQTR)
z, Z = X9sm_4sF(2048)
n = z * Z
e = 0x10001
c = pow(dL, e, n)

print(f"{n}")
print(f"{e}")
print(f"{c}")
