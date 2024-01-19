from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes, bytes_to_long

NB = 700
flag = b"A coppersmith, also known as a brazier, is a person who makes artifacts from copper and brass. Brass is an alloy of copper and zinc. LNC24{a_r3al1y_l0Ng_rsa_keY_rec0verY_cH41n_4nd_a_r3aLLy_l0NG_fl4G} Some coppersmiths can sometimes recover RSA keys"
m = bytes_to_long(flag)

# Generate challenge params
while True:
    rsa = RSA.generate(2048)
    n, p, q = rsa.n, rsa.p, rsa.q
    e = 17
    if gcd(e, (p-1)*(q-1)) == 1:
        break
c = pow(m, e, n)
d = pow(e, -1, (p-1)*(q-1))
dlo = d % 2**NB

# Solve script
found = False
for k in range(1,e):
    if gcd(k, 2**NB) > 1:
        continue

    print(f"Testing for k = {k}")
    # let s = p+q, get low bits of s
    # e*d0 == 1 + k(N - p - q + 1) mod 2**NB
    slo = -((e*dlo - 1) * inverse_mod(k, 2**NB) - n - 1 ) % 2**NB

    # F.<x> = PolynomialRing(Zmod(2**NB))
    # f = x**2 - slo * x + n
    # assert(f(p % 2**NB) == 0) # this also works for q % 2**NB
    # print(f"Quadratic: x**2 - {slo}*x + {n} == 0 % 2**{NB}")
    # solve quadratic for low bits of p or q
    disc = Mod((slo**2 - 4*1*n), 2**NB)
    if not (disc.is_square()):
        print("Bad, discriminant is not a square.")
        continue
    disc = disc.sqrt(all=True)
    roots = list(set([i % 2**NB for j in disc for i in [int(slo + j) // 2, int(slo - j) // 2, \
                                                        int(slo + n + j)//2, int(slo + n - j)//2 ]]))
    print(f"Found {len(roots)} potential solutions")

    # plo = p % 2**NB
    # qlo = q % 2**NB
    # print(f'Debug: lowp in roots is {plo in roots}')
    # print(f'Debug: lowq in roots is {qlo in roots}')
    # possible that LSB of p is among them. Apply small_roots() to solve for p or q
    # note this quadratic solver implementation is very jank and may not find solutions even at right k value. I'm not quite sure why but it could be due to the jank division by 2 modulo N where 2 divides N

    # using coppersmith to recover p or q
    F.<x> = PolynomialRing(Zmod(n))
    for i in roots:
        f = (2**NB * x + i).monic()
        smroots = f.small_roots(X=2**(1025-NB), beta=0.4)
        if len(smroots) == 0:
            continue
        found_p = gcd(int(f(smroots[0])), n)
        print(f"Found prime = {found_p}")
        found = True
        break
    if found:
        break

# recover flag
if not found:
    exit()

found_q = n // found_p
assert found_p * found_q == n
found_d = pow(e, -1, (found_p - 1)*(found_q - 1))
m = pow(c, found_d, n)
print(long_to_bytes(m))
