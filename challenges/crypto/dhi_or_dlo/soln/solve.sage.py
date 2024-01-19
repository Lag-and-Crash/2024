

# This file was *autogenerated* from the file solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_700 = Integer(700); _sage_const_2048 = Integer(2048); _sage_const_17 = Integer(17); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_1024 = Integer(1024); _sage_const_4 = Integer(4); _sage_const_1025 = Integer(1025); _sage_const_0p4 = RealNumber('0.4'); _sage_const_0 = Integer(0)
from Crypto.PublicKey import RSA

NB = _sage_const_700 
flag = b""

while True:
    rsa = RSA.generate(_sage_const_2048 )
    n, p, q = rsa.n, rsa.p, rsa.q
    e = _sage_const_17 
    if gcd(e, (p-_sage_const_1 )*(q-_sage_const_1 )) == _sage_const_1 :
        break
d = pow(e, -_sage_const_1 , (p-_sage_const_1 )*(q-_sage_const_1 ))

dlo = d % _sage_const_2 **NB
dhi = d // _sage_const_2 **(_sage_const_1024 -NB)
print(d.bit_length())
for k in range(_sage_const_1 ,e):
    if gcd(k, _sage_const_2 **NB) > _sage_const_1 :
        continue

    print(f"Testing for k = {k}")
    # let s = p+q, get low bits of s
    # e*d0 == 1 + k(N - p - q + 1) mod 2**NB
    slo = -((e*dlo - _sage_const_1 ) * inverse_mod(k, _sage_const_2 **NB) - n - _sage_const_1  ) % _sage_const_2 **NB

    # F.<x> = PolynomialRing(Zmod(2**NB))
    # f = x**2 - slo * x + n
    # assert(f(p % 2**NB) == 0) # this also works for q % 2**NB
    # print(f"Quadratic: x**2 - {slo}*x + {n} == 0 % 2**{NB}")
    # solve quadratic for low bits of p or q
    disc = Mod((slo**_sage_const_2  - _sage_const_4 *_sage_const_1 *n), _sage_const_2 **NB)
    if not (disc.is_square()):
        print("Bad, discriminant is not a square.")
        continue
    disc = disc.sqrt(all=True)
    roots = list(set([i % _sage_const_2 **NB for j in disc for i in [int(slo + j) // _sage_const_2 , int(slo - j) // _sage_const_2 ,                                                         int(slo + n + j)//_sage_const_2 , int(slo + n - j)//_sage_const_2  ]]))
    print(f"Found {len(roots)} potential solutions")

    # plo = p % 2**NB
    # qlo = q % 2**NB
    # print(f'Debug: lowp in roots is {plo in roots}')
    # print(f'Debug: lowq in roots is {qlo in roots}')
    # possible that LSB of p is among them. Apply small_roots() to solve for p or q
    # note this quadratic solver implementation is very jank and may not find solutions even at right k value. I'm not quite sure why but it could be due to the jank division by 2 modulo N where 2 divides N

    # using coppersmith to recover p or q
    F = PolynomialRing(Zmod(n), names=('x',)); (x,) = F._first_ngens(1)
    for i in roots:
        f = (_sage_const_2 **NB * x + i).monic()
        smroots = f.small_roots(X=_sage_const_2 **(_sage_const_1025 -NB), beta=_sage_const_0p4 )
        if len(smroots) == _sage_const_0 :
            continue
        found_p = gcd(int(f(smroots[_sage_const_0 ])), n)
        print(f"Found prime = {found_p}")
        print(f"p = {p}")
        print(f"q = {q}")
        break
