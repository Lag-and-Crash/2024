from Crypto.Util.number import *

zxyyzx = b"LNC24{flag!}"

pqrs_1 = getPrime(1024)
pqrs_2 = getPrime(1024)
fjkdasl = pqrs_1 * pqrs_2
jkl = (pqrs_1 - 1) * (pqrs_2 - 1)
ufdiaskop = 65537
xzyx = inverse(ufdiaskop, jkl)
xnclkvha = (fjkdasl, xzyx)
fdasfdasf = [(fjkdasl, getPrime(512)) for _ in range(5)]
ezxyyzx = bytes_to_long(zxyyzx)
for x in fdasfdasf:
    ezxyyzx = pow(ezxyyzx, x[1], x[0])

print(f"My private key pair: {xnclkvha}")
print(f"The resistance's public keys: {fdasfdasf}")
print(f"Encrypted message: {ezxyyzx}")
