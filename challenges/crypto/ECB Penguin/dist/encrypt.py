from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

with open("tux.bmp", "rb") as f:
    penguin = f.read()

key = get_random_bytes(32)
cipher = AES.new(key, AES.MODE_ECB)
enc = cipher.encrypt(pad(penguin, AES.block_size))

with open("encrypted.bin", "wb") as f:
    f.write(enc)
