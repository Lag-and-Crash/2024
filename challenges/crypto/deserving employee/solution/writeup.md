# Solution
1. (for first qn)
2. Replace the hex characters with the following:
3. '93' -> 'l'
4. '9E' -> 'a'
5. '98' -> 'g'
6. 'A0' -> '_'
7. '9C' -> 'c'
8. '8D' -> 'r'
9. '8C' -> 's'
10. '97' -> 'h'
11. '99' -> 'f'
12. '90' -> 'o'
13. '9A' -> 'e'
14. '89' -> 'v'
15. '92' -> 'm'
16. 'DF' -> ' '
17. '8B' -> 't'
18. '96' -> 'i'
19. '91' -> 'n'
20. '9D' -> 'b'
21. '9B' -> 'd'
22. '8A' -> 'o'
23. 'DF' -> 'u'
15. the result will be the code 'lag_crash_forever'
16. (for second qn)
17. do an XOR of '9D A2 BC A0' with '32 30 30 30' to get 'AF 92 8C 90'. this cancels the original data to return the portion of the encryption key
18. do an XOR of 'AF 92 8C 90' with '39 39 39 39' to get '96 AB B5 A9'. this re-encrypts the new data with the original encryption key
19. concatenate 'lag_crash_forever' with '96 AB B5 A9 C1 CF BC 32 68 EF E4 49 52 E7 38 61 E4 46 5C A2 4C 5A E8 FD 12 E8 4E E6 FC 4D F7 08 46 5D A8 55 4D CE', to get 'lag_crash_forever96 AB B5 A9 C1 CF BC 32 68 EF E4 49 52 E7 38 61 E4 46 5C A2 4C 5A E8 FD 12 E8 4E E6 FC 4D F7 08 46 5D A8 55 4D CE'
20. do a md5 checksum on 'lag_crash_forever96 AB B5 A9 C1 CF BC 32 68 EF E4 49 52 E7 38 61 E4 46 5C A2 4C 5A E8 FD 12 E8 4E E6 FC 4D F7 08 46 5D A8 55 4D CE', to get '0c019503a833675624b7b868ea6c1839'
21. decrypt the zip file using this password and get the flag!