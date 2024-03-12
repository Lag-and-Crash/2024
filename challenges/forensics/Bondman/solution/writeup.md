# Solution

1. Read the message and transcript to know what you need to do; locate the eb_checksum value and change it to decimal

2. Open the image of the hex editor, look at offset 2229c120, from 01, go 64 bytes to locate the eb_checksum. Value = 10 6E 98 DA

3. Change to decimal -> 10 6E 98 DA in little endian is DA 98 6E 10 = 3667422736 dec

4. unzip the zip file using the passphrase '3667422736'

5. Inside you will find an excel sheet. In order to find the flag, you have the find the deletion time. from the i_flag, go back 8 bytes = CC 34 27 62

6. Convert that to dec 62 27 34 CC = 1646736588

7. Convert 1646736588 to epoch time and date. in GMT: Tuesday, March 8, 2022 10:49:48 AM

8. If you look at the todo.txt, you will see 2 hints: 1. there should be corrupted flag.xlsx and to remove a cat image from there (somewhere)

9. so, open hex editor and search for 'FF D8' in the file and remove 'FF D8' until 'FF D9' (remove the cat image)

10. ensure that the file signature is 'D0 CF 11 E0 A1 B1 1A E1' (changed 2)

11. save the file and rename it to flag.xlsx

12. Use the password; 142544.8325 to unlock flag.xlsx to get the flag
