# May need to swap the " with ' below if the ciphertext contains either character. The challenge will not use a ciphertext that contains both.
ciphertext = "eÑ kÙ Z½ )[ )] rí fØ `Å mã -` qã má #T kÙ _Æ Q° bÔ .b `Î Y½ /_ hÕ S² pâ *Z sç [¼ 0g YÂ jÙ _Í lß z÷"
plaintext = ''

# Remove spaces between pairs
ciphertext = ciphertext.replace(' ','')

pair = ''

# Take out each pair from the ciphertext
for i, letter in enumerate(ciphertext):
    i += 1
    # On even number characters, check the pair
    if i % 2 == 0:
        pair += letter
        letter1 = pair[0]
        letter2 = pair[1]

        # Brute force rotating the characters in their pairs up to 150 times as the highest printable value that could have been used is } which is unicode 150
        for j in range(150):

            # Convert the characters to their unicode values
            num1 = ord(letter1)
            num2 = ord(letter2)

            # Rotate the characters
            num1 += j
            num2 += j

            # Check if the unicode value of the second character is twice the first
            if num1*2 == num2:
                plaintext += chr(num1)
                break
            
        # Reset the pair every even number
        pair = '' 
    else:
        # On odd number characters, skip the check and store the letter in the pair
        pair = letter
        
print(plaintext.upper())