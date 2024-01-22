# Solution
In this challenge, we have our own keypair (N,e,d) and 5 different public keys all using the same modulus N. In order to decrypt the message, we need to get the private keys of all of our friends. For that, we need to compute φ(N) in order to invert the public exponents. But if you lookup an algorithm to factorize N, given N,e,d, you can translate it into code.

In my solution, we import the public exponent (e) and the modulus (N) from the question, here, e is the public exponent, and N is the modulus. In RSA encryption, these values are part of the public key.

Moving on, we calculate the private exponent (d) and the factorization constant (k), the factorization constant k and Euler's totient function phi are calculated based on the relationship between e, d, and N. k is used to derive phi. Euler's totient function phi(N) is crucial in RSA and represents the number of positive integers less than N that are coprime to N.

then, we iterate through the list of public keys (key pairs), and for each key, calculate the private exponent (d) using the modular inverse function, in this loop, the code iterates through a list of public keys, and for each key (which consists of N and a random prime key[1]), it calculates the corresponding private exponent d using the modular multiplicative inverse function inverse(). This private exponent d is used for decryption.

finally, we decrypt the message using the private exponent (d) and the modulus (N), the code uses the private exponent d and the modulus N to perform modular exponentiation and decrypt the original message. This step effectively reverses the RSA encryption process.