# Solution for Caesar is so simple

## Solution

- Challenge uses a ROT-13-like cipher and code written to look similar to AES encryption
    - But it's actually very insecure lmao
- Notice that 2 plaintexts encrypted with the same key will result in the same like "rotation" for each respective characters
    - Can find this either through static code analysis or through testing
- Since there's a known plaintext and it's encrypted value, reversing the encryption is trivial

## Solve script

Solve script: [solve.py](solve.py)
