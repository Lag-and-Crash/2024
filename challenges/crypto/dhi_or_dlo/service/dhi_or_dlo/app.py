from Crypto.PublicKey import RSA
from math import gcd
from secret import flag
from Crypto.Util.number import bytes_to_long

NB = 700
m = bytes_to_long(flag)
while True:
    rsa = RSA.generate(2048)
    n, p, q = rsa.n, rsa.p, rsa.q
    e = 17
    if gcd(e, (p-1)*(q-1)) == 1:
        break
d = pow(e, -1, (p-1)*(q-1))
c = pow(m, e, n)

print(f"n = {n}")
print(f"e = {e}")
print(f"c = {c}")
print("dhi or dlo?")
userinput = str(input(">> "))
if userinput == "dhi":
    print(f"dhi = {d // 2**(2048 - NB)}")
elif userinput == "dlo":
    print(f"dlo = {d % 2**NB}")
else:
    print("Invalid input.")

