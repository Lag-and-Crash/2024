n = 21460311723118679257542775946648406659538310516025259879782956062834251755333097666316019653948694097948006810859082678707326628006885191903346486899454481216732633853981279300824522187032129975332379189406320294241096938883564593577090018380272661625146084623502964347988575587827909752769145842163799134580556376633288287989245051234547576647325305523264793615287019697952339197665592287897606799991498576383974672619703141517059734203078106863070075907116591293931485163228054347099486620761576051492600694610880129338414115809735553278990455562441911695748197719372214335030692140700093900065988102489943619049249
e = 5
c = 15642520536758795637632604116513454339698877690138915481049257096372284913661126042417909310774448004216038555076680531469094858334859718539181401399247226420242896340789013486392951742444263033033836978174049607257446753311763864946534155553634633010737057200499555414274553445783129543622065037292358093356964514503272490898786596756183697870390776074994226006072984957872410830147780337527385894836682852111941283758329104231125207606078399396130920467961503320777337868171069433635323379433135186819802671078129383364561040033926336711445594599234306040819937275019932246368867298846203233001059987887825040458145
dlo = 50656960598253328982206152153994408785710864182237665546141428568764683301362304335276532842198833934033261475448987172211777081646632369090173287059317720642
r = 3**333

from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes, bytes_to_long
from time import time


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