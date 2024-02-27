# Solution

1. Read the message and transcript to know what you need to do; locate the eb_checksum value and change it to decimal

2. Open the image of the hex editor, look at offset 2229c120, from 01, go 64 bytes to locate the eb_checksum. Value = 10 6E 98 DA

3. Change to decimal -> 10 6E 98 DA in little endian is DA 98 6E 10 = 3667422736 dec

4. unzip the zip file using the passphrase '3667422736'

5. Inside you will find an excel sheet. In order to find the flag, you have the find the deletion time. from the i_flag, go back 8 bytes = CC 34 27 62

6. Convert that to dec 62 27 34 CC = 1646736588

7. Convert 1646736588 to epoch time and date. in GMT: Tuesday, March 8, 2022 10:49:48 AM

8. Fill in the blank to see and use the password; 142544.8325 to unlock the sheet 'nothing to see here' to get the flag