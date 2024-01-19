# Solution
1. (for first qn)
2. Replace the hex characters with the following:
3. '7E' -> 'l'
4. '73' -> 'a'
5. '75' -> 'g'
6. '4D' -> '_'
7. '71' -> 'c'
8. '60' -> 'r'
9. '61' -> 's'
10. '7A' -> 'h'
11. '74' -> 'f'
12. '7D' -> 'o'
13. '77' -> 'e'
14. '64' -> 'v'
15. the result will be the code 'lagcrash_forever'
16. (for second qn)
17. do an XOR of '9D A2 BC A0' with '32 30 30 30' to get 'AF 92 8C 90'. this cancels the original data to return the portion of the encryption key
18. do an XOR of 'AF 92 8C 90' with '39 39 39 39' to get '96 AB B5 A9'. this re-encrypts the new data with the original encryption key
19. concatenate 'lagcrash_forever' with '96 AB B5 A9 C1 CF BC 32 68 EF E4 49 52 E7 38 61 E4 46 5C A2 4C 5A E8 FD 12 E8 4E E6 FC 4D F7 08 46 5D A8 55 4D CE', to get 'lagcrash_forever96 AB B5 A9 C1 CF BC 32 68 EF E4 49 52 E7 38 61 E4 46 5C A2 4C 5A E8 FD 12 E8 4E E6 FC 4D F7 08 46 5D A8 55 4D CE'
20. do a CRC-32 checksum on 'lagcrash_forever96 AB B5 A9 C1 CF BC 32 68 EF E4 49 52 E7 38 61 E4 46 5C A2 4C 5A E8 FD 12 E8 4E E6 FC 4D F7 08 46 5D A8 55 4D CE', to get '2ce416b4'
21. decrypt the zip file using this password and get the flag!