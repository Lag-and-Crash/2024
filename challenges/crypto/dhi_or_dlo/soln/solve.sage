from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes, bytes_to_long
from time import time

flag = b"A coppersmith, also known as a brazier, is a person who makes artifacts from copper and brass. Brass is an alloy of copper and zinc. LNC24{a_r3al1y_l0Ng_rsa_keY_rec0verY_cH41n_4nd_a_r3aLLy_l0NG_fl4G} Some coppersmiths can sometimes recover RSA keys"
m = bytes_to_long(flag)
r = 3**333
# Generate challenge params
while True:
    rsa = RSA.generate(2048)
    n, p, q = rsa.n, rsa.p, rsa.q
    e = 5
    if gcd(e, (p-1)*(q-1)) == 1:
        break
c = pow(m, e, n)
d = pow(e, -1, (p-1)*(q-1))
dlo = d % r

# Solve script
start = time()
found = False
for k in range(1,e):
    print(f"Testing for k = {k}")
    kstart = time()
    if gcd(k, r) > 1:
        print("Cannot find solution.")
        continue
    # let s = p+q, get low bits of s
    # e*d0 == 1 + k(N - p - q + 1) mod 2**NB
    slo = -((e*dlo - 1) * inverse_mod(k, r) - n - 1 ) % r

    # F.<x> = PolynomialRing(Zmod(2**NB))
    # f = x**2 - slo * x + n
    # assert(f(p % r) == 0) # this also works for q % r
    # print(f"Quadratic: x**2 - {slo}*x + {n} == 0 % r")
    # solve quadratic for low bits of p or q
    a = var('a')    
    roots = [int(i[0]) for i in solve_mod([a**2 - slo*a + n == 0], r)]
    print(f"Found {len(roots)} potential solutions")

    # plo = p % r
    # qlo = q % r
    # print(f'plo {plo in roots}')
    # print(f'qlo {qlo in roots}')
    # in this case it is possible that LSB of p is among them. Apply coppersmith / small_roots() to solve for p or q
    F.<x> = PolynomialRing(Zmod(n))
    for i, plo in enumerate(roots):
        print(f'{i+1}/{len(roots)}',end='\r')
        f = (r * x + plo).monic()
        smroots = f.small_roots(X=2**(1026-r.bit_length()), beta=0.3, epsilon=0.005)
        if len(smroots) == 0:
            continue
        found_p = gcd(int(f(smroots[0])), n)
        print(f"Found prime = {found_p}")
        found = True
        break
    print(f"Round {k} took {time() - kstart} seconds.") 
    if found:
        break

print(f"Total time elapsed: {time() - start} seconds.")
# recover flag
if not found:
    exit()

found_q = n // found_p
assert found_p * found_q == n
found_d = pow(e, -1, (found_p - 1)*(found_q - 1))
m = pow(c, found_d, n)
print(long_to_bytes(m))
