# Encryption of the flag:
    1. Double each letter's unicode decimal value. This will represent another unicode character.
    2. Rotate the original letter and the doubled letter's unicode values a random number of times. Limited at 16 as subtracting past 16 may result in unprintable characters.
    3. Convert the values back to unicode characters
    4. Combine both letters to form a pair and append to ciphertext
    Refer to cipher.py in the solution files for a code representation

# Solution:
1. Seeing as all 3 ciphertexts were generated from the same script but have different outputs, the script must have an element of randomness.
2. Knowing that the ciphertext is the flag, it should start with 'LNC24{'. Since the text file states that the flag must be converted all to uppercase, the flag that was encrypted was likely in lowercase and hence starts with 'lnc24{'. With a known plaintext in mind, the player should find a way to match the ciphertext with 'lnc24{'.
3. The correct solution would be to rotate aka 'turn' each pair using the characters' unicode values until the first letter of each pair matches 'lnc24{'. 
    - First letter:     fÒ -> lØ    (rotated until first letter is 'l')
    - Second letter:    aÏ -> nÜ    (rotated until first letter is 'n')
    - Third letter:     bÅ -> cÆ    (rotated until first letter is 'c')
    - Fourth letter:    #U -> 2d    (rotated until first letter is '2')
    - Fifth letter:     .b -> 4h    (rotated until first letter is '4')
    - Sixth letter:     lç -> {ö    (rotated until first letter is '{')
4. The player will have to recognise a pattern from these 6 pairs:
    The unicode value of the second letter in each pair is always double the unicode value of the first. 
        *Looking at the first pair 'lØ'*
        *The first character 'l' has unicode value 108. The second character is 'Ø' which has unicode value 216 (108 x 2)*
        *Looking at the second pair 'nÜ'*
        *The first character 'n' has unicode value 110. The second character is 'Ü' which has unicode value 220 (110 x 2)*
5. With this, the player can create a script to rotate through the letters of each pair such that the unicode value of the second character is twice the unicode value of the first. An example script is provided as solve.py in the solution files

# Alternate Solution:
After steps 1 and 2 from above
3. Looking at the unicode value of each letter, the player can see that in the first pair of all the strings, the difference between the 2 characters is 108.
    - Ciphertext 1, First pair:     k×    unicode values: 107, 215    difference: 215 - 107 = 108
    - Ciphertext 2, First pair:     dÐ    unicode values: 100, 208    difference: 208 - 100 = 108
    - Ciphertext 3, First pair:     eÑ    unicode values: 101, 209    difference: 209 - 101 = 108
4. Looking at the unicode table, the character with value 108 is 'l'. This happens to be the first letter of the flag. (The player should already know the flag will start with lowercase 'lnc24{'
5. The player can then repeat the subtraction for all the values to obtain the flag.
