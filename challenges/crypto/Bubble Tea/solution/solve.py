import pwn
from itertools import combinations
from Crypto.Util.number import long_to_bytes

HOST = "127.0.0.1"
PORT = 1337
MSG = b"message"

def recv_share():
    conn.recvuntil(b"it!\n")
    return [int(conn.recvline()) for _ in range(64)]

def get_flag_shares():
    conn.recvuntil(b"have: ")
    conn.sendline(b"1")
    return recv_share()

def get_custom_shares():
    conn.recvuntil(b"have: ")
    conn.sendline(b"2")
    conn.recvuntil(b"share: ")
    conn.sendline(MSG)
    return recv_share()

conn = pwn.remote(HOST, PORT)

flag_share = get_flag_shares()
# 40 requests have a reasonably high chance of getting enough values
shares = [print(f"share: {_}") or get_custom_shares() for _ in range(40)]

possible = [0] * 64
for share in shares:
    for i, p in enumerate(share):
        possible[i] += p%2 == 0

# Get min 38 values (almost good enough (sorta))
possible_indexes = sorted(range(64), key=lambda i: possible[i])[:38]

possible_shares = [flag_share[i] for i in possible_indexes]

for share in combinations(possible_shares, 32):
    p = 0
    for x in share:
        p ^= x
    flag = long_to_bytes(p)
    if b"LNC24" in flag:
        print(flag.decode())
        break
