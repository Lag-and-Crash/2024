# Solution for Bubble Tea

## Solution

- There's 2 possible solutions to the challenge, one was by me, the other by a fellow challenge creator
- Main idea is this:
    - Message is "split" into 32 secret shares, you need all 32 to be able to calculate value of message
    - These 32 values are scattered amongst 32 other random numbers
    - Which of the 64 values are the random numbers is determined by `spillage`
    - The idea is to find out what the value of `spillage` is so that you can recover the flag

### Solution 1

The random numbers are generated using the `bubble_tea()` function.

```py
def bubble():
    return rand.getrandbits(512 // 2)

def tea():
    return rand.getrandbits(512 // 2)

def bubble_tea():
    return bubble() * tea()
```

The function returns a number which is calculated from 2 random numbers.
Since any product of an even number is also even, the function `bubble_tea()` yields an even number 75% of the time.
```
even * even = even
even * odd = even
odd * even = even
odd * odd = odd
```
This means that the "bubble tea" numbers will tend to be an even number way more often than the "secret share" numbers

We can use this property to find out what the `spillage` is:
- Make enough number of requests for generating message shares
- From these requests inspect the frequency of the nth value being an even number
- Choose the values with a lower frequency of being an even number
- Calculate flag shares from these values

Solve script: [solve.py](solve.py)


### Solution 2

Since XOR is essentially addition modulo 2
```
1 ^ 1 = 0
1 + 1 ≡ 0 (Mod 2)
```
The challenge becomes solving a system of linear equations, which is trival for computers to calculate

What he said:
> xor is just addition modulo 2  
> so it devolves into solving a system of linear equations, mod 2  
> the idea is u want to find a vector (1, 0, 0, .....) whereby for the served shares, if vector_i is 1 then you xor it else you skip it (i.e. this vector is spillage)  
> and because xor is addition modulo 2 for each bit, you can take every 512-bit number in served shares as 512 different equations with 64 unknowns total  
> i basically just had sagemath solve the system of equations to get a unique solution vector, which would naturally be spillage
> each bit represents one equation that you can make involving `spillage` and the final `pn`

Solve script: [solve.sage](solve.sage)
