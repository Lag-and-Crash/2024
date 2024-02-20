flag_shares = generate_shares(FLAG, 31)
flag_out = serve(flag_shares)
shares = generate_shares(b'\x00', 31)
shares_out = serve(shares)

M = []
for i in shares_out[1:]:
    A = [int(j) for j in format(i, '0512b')]
    M.append(A)
M = Matrix(Zmod(2), M)
v = vector(Zmod(2), [int(j) for j in format(shares_out[0], '0512b')])

# assume pn is in out[0]. Works 50% of the time
ans = [False] + [i == 0 for i in M.solve_left(v)]
# print(ans == spillage)

ct = flag_out[0]
for oops, share in zip(ans[1:], flag_out[1:]):
    if not oops:
        ct ^^= share
print(ct.to_bytes(512 // 8, "big"))
