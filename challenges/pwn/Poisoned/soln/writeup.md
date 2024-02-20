# Poisoned Solution
This is a classic UAF challenge. Let's first examine the vulnerability, before discussing the exploit.

When it comes to finding heap exploits, Dhaval Kapil's [secure coding guidelines](https://heap-exploitation.dhavalkapil.com/secure_coding_guidelines) is a good reference. Looking through the provided source, we find that in `delete_user()`, the freed pointer is not set to null.
```c
if (users[choice] != NULL)
{
    free(users[choice]);
    // MISSING: users[choice] = NULL;
}
```
This means that the other functions fail to distinguish this freed pointer from a pointer that is still currently in-use. This is a Use After Free (UAF) vulnerability. The `view_user()` function allows us to read the contents of this freed chunks, while the `modify_user()` function allows us to write to a freed chunk. These are two powerful primitives that will allow us to pwn the heap.

It is also important to note that the challenge container is running on Ubuntu 18.04, which uses glibc 2.27 by default. This version of glibc is lacking in many modern heap protection measures (for reference, the latest glibc version is 2.36!). This simplifies heap exploitation quite a bit. The next step is to choose an attack. Given that we already have two powerful primitives, many types of attacks are possible, but we'll choose one of the simplest - tcache poisoning.

Many [resources](https://github.com/shellphish/how2heap/blob/master/glibc_2.27/tcache_poisoning.c) already exist detailing how the exploit works, but I'll briefly summarise the concept.
- When the `User` chunk is freed, it goes into the 'tcache'.
- Each freed chunk forms a linked list, with a pointer pointing to the next freed chunk in the tcache.
- When `malloc()` is called, it tries to use on of the freed chunks in the tcache. If it finds one, it returns that chunk and modifies the linked list accordingly.
- If we can modify the `next` pointer, we can force `malloc()` to return an arbitrary chunk.

In other words, we free 2 chunks to set up the linked list. Then, we use our UAF to point the first freed chunk's next pointer to our win chunk. After calling `malloc()` twice, the 2nd chunk returned will point to the win chunk, allowing us to overwrite it.

> One extra detail is that we need to determine the address of our win chunk. To do so, we can use `view_user()` on the freed chunk to leak a heap address, from which we can calculate the address of the win chunk.

## Takeaways
As an exercise, try compiling the binary with glibc 2.31 and 2.35. See if you can get around the mitigation measures in place.
