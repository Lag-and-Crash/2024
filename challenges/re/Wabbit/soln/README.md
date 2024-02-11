# How to solve Wabbit
## Tools
1. Ghidra
2. Ghidra Wasm Extension

## Steps
1. Visit website and press button to receive program output
2. Inspect Element and find /src/main.ts
3. Follow source code to find boot() function in /src/terminal.ts
4. Observe that output is actually a wasm file `go.wasm` being executed in a webcontainer
5. Download `go.wasm`
6. Open Ghidra
7. Install Ghidra WASM Extension
8. Open `go.wasm` in Ghidra Code Viewer
9. Decompile `go.wasm` into C, notice that file was not actually a C binary file.
10. Follow program main function until you find a getFlag() function.
11. (a) Patch the program to skip the `if` check while still updating stack pointers to correct positions (harder solution as golang does fancy things with their stack pointer)
11. (b) Follow source code of getFlag() function until you find portion where flag value is being loaded into an array.
>     puVar2[0x20] = 0x480000005a;
>     puVar2[0x1f] = 0x6800000064;
>     puVar2[0x1e] = 0x3200000059;
>     puVar2[0x1d] = 0x3500000046;
>     puVar2[0x1c] = 0x470000004f;
>     puVar2[0x1b] = 0x3500000038;
>     puVar2[0x1a] = 0x3100000063;
>     puVar2[0x19] = 0x790000004e;
>     puVar2[0x18] = 0x6a00000062;
>     puVar2[0x17] = 0x7800000051;
>     puVar2[0x16] = 0x4400000064;
>     puVar2[0x15] = 0x7500000042;
>     puVar2[0x14] = 0x7a00000059;
>     puVar2[0x13] = 0x660000004a;
>     puVar2[0x12] = 0x320000004d;
>     puVar2[0x11] = 0x3300000039;
>     puVar2[0x10] = 0x6c00000062;
>     puVar2[0xf] = 0x7800000038;
>     puVar2[0xe] = 0x4600000062;
>     puVar2[0xd] = 0x300000004d;
>     puVar2[0xc] = 0x6e00000063;
>     puVar2[0xb] = 0x7a00000059;
>     puVar2[10] = 0x330000004d;
>     puVar2[9] = 0x7900000039;
>     puVar2[8] = 0x5600000062;
>     puVar2[7] = 0x7a00000052;
>     puVar2[6] = 0x7a00000064;
>     puVar2[5] = 0x6600000042;
>     puVar2[4] = 0x7a0000005a;
>     puVar2[3] = 0x3700000052;
>     puVar2[2] = 0x6a0000004d;
>     puVar2[1] = 0x4400000035;
>     *puVar2 = 0x4500000054;

This is the interesting bit of C code. This is the data being loaded into the puVar2 array before being parsed into `runtime.stringFromUnicode()`.

An optimisation technique makes go combine 2 integer values into the same line, so each line above actually stores 2 ascii values, read in little endian format.

Get all the individual ASCII integer values and you'll get this:
```
[84, 69, 53, 68, 77, 106, 82, 55, 90, 122, 66, 102, 100, 122, 82, 122, 98, 86, 57, 121, 77, 51, 89, 122, 99, 110, 77, 48, 98, 70, 56, 120, 98, 108, 57, 51, 77, 50, 74, 102, 89, 122, 66, 117, 100, 68, 81, 120, 98, 106, 78, 121, 99, 49, 56, 53, 79, 71, 70, 53, 89, 50, 100, 104, 90, 72, 48, 61]
```

Simply convert to ASCII characters in Python and you'll get:
TE5DMjR7ZzBfdzRzbV9yM3YzcnM0bF8xbl93M2JfYzBudDQxbjNyc185OGF5Y2dhZH0=

Finally, Base64 decode to get the flag.
LNC24{g0_w4sm_r3v3rs4l_1n_w3b_c0nt41n3rs_98aycgad}