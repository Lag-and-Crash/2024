import random 
flag = 'lnc24{rev3rt1ng_r4nd0m_r0ta7ions}'

# Encryption function
def encrypt():
    ciphertext = ''

    for letter in flag:

        # 1. Double each letter's unicode decimal value. This will represent another unicode character.
        letter1 = ord(letter)
        letter2 = letter1 * 2

        # 2. Rotate the original letter and the doubled letter's unicode values a random number of times. Limited at 16 as subtracting past 16 may result in unprintable characters.
        random_num = random.randint(1,16)
        letter1 -= random_num
        letter2 -= random_num

        # 3. Convert the values back to unicode characters
        letter1 = chr(letter1)
        letter2 = chr(letter2)

        # 4. Combine both letters to form a pair and append to ciphertext
        pair = letter1 + letter2
        ciphertext += pair + ' '

    return ciphertext

# Create 3 ciphertexts
for i in range(3):
    ciphertext = ''
    while len(ciphertext.replace(' ','')) != len(flag)*2 or '"' in ciphertext: # Just makes sure the ciphertext did not generate with blank unicode characters or the " character (make it easier to create a solve script). If it did, regenerate.
        ciphertext = encrypt()
    print(ciphertext)
