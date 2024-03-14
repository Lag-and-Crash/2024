from Crypto.Util.number import long_to_bytes

DIR = "LnC CTF\\ECB Penguin\\src\\"
ENC = "encrypted.bin"
OUT = "ecb.bmp"

with open(DIR+ENC, "rb") as f:
    enc = f.read()

# https://en.wikipedia.org/wiki/BMP_file_format#File_structure
# https://docs.fileformat.com/image/bmp/

# Bitmap file header
header1 = b"BM"
header1 += long_to_bytes(len(enc), 4)[::-1]
# header += long_to_bytes(len(enc)-2)[::-1]
header1 += b"\x00" * 4
header1 += long_to_bytes(54, 4)[::-1]

# DIB header (BITMAPINFOHEADER)
header1 += long_to_bytes(40, 4)[::-1]
# header2 = long_to_bytes(..., 4)[::-1]     # bruteforce image width in pixels
# header2 += long_to_bytes(..., 4)[::-1]     # bruteforce image height in pixels
header3 = long_to_bytes(1, 2)[::-1]
header3 += long_to_bytes(24, 2)[::-1]    # Need to bruteforce 1, 4, 8, 16, 32
header3 += long_to_bytes(0, 4)[::-1]
header3 += long_to_bytes(0, 4)[::-1]     # Just 0 it lol
header3 += long_to_bytes(222, 4)[::-1]   # Random number lol doesn't matter
header3 += long_to_bytes(222, 4)[::-1]   # Random number lol doesn't matter
header3 += long_to_bytes(0, 4)[::-1]     # Also just 0 this lol
header3 += long_to_bytes(0, 4)[::-1]     # 0 this too lol

size = len(enc) * 8 // 24   # Smart guess for approximate size of image
# for w in range(3390, 3391, 1):  # Answer is 3390
for w in range(3000, 4000, 1):  # Guessed 3000 (would need to bruteforce a lot lol)
    with open(f"output\\{w}.bmp", "wb") as f:
        h = size // w - 300     # Minus 300 to prevent "wrong format"
        header2 = long_to_bytes(w, 4)[::-1]
        header2 += long_to_bytes(h, 4)[::-1]
        header = header1 + header2 + header3
        f.write(header + enc[len(header):])
