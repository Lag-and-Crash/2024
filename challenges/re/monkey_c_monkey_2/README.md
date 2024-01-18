# monkey-C-monkey-2
An APT group, known as "monkey-C-monkey-2", has targeted our company and successfully launched a ransomware operation on one of our employees. We have managed to recover a stageless binary that was dropped onto our server, as well as a network capture of the attack.

Unfortunately, we were unable to locate any identify the malicious traffic in the network capture and have made little progress in decrypting our files. However, our threat intelligence tells us that this group is known to use a concept known as Malleable C2, which allows them to disguise their network traffic as legitimate traffic.

Could you help us find out how to decrypt our files?

## Summary
- **Author:** [Zavier]
- **Discord Username:** [gatari]
- **Category:** [Reverse]
- **Difficulty:** [Hard]

## Hints
1. https://github.com/BC-SECURITY/Malleable-C2-Profiles/blob/master/Normal/reddit.profile
    - free
2. One of them is not like the other (User-Agent / Server)
    - 100 points
3. https://www.dcode.fr/ascii-shift-cipher
    - 150 points
4. https://github.com/lucacav/steg-in-the-wild (p.s no there is no steghide nonsense here)
    - 200 points

## Files
- [capture.pcapng](./dist/capture.pcapng)
- [flag.txt.enc](./dist/flag.txt.enc)
- [implant_x64.exe](./dist/implant_x64.exe)

## Flags
- `LNC24{mOnKeY_sEe_M0nkey_7w0_7f7ad80dafbd28f2401ae37a8e0684a9}` (static)