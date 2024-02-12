"""
Deobfuscated python chall.py
"""

from base64 import urlsafe_b64decode
from hashlib import sha256

corrupted_strings_output = ['???????????????M.UAFAFAAgDAgwMUJDVAVAEUw0BQAMIUpwUBVAAEw0BAAxMUIh',
                            '???????????????0.cEEAYCFBAFNSIiJLcEUAaANRITFCZhJAcFUESANQIEIRIjIB',
                            '???????????????a.EAFSJCFARFVQIUEFFiFSKAVANTFAIVkkEhFUCAVANEARIVEh',
                            '???????????????y.IEFCJAEBCEEAIGFNJEVCIUMBICEMJF1EIEVEAEMAIEAAIHEB',
                            '???????????????U.AAFAdBBhREJCEmALBCFAcBxhFABGQkwgABFEQBxgFEIBEmAh',
                            '???????????????9.UAByJABBAFlQAgNCUARyKApBIBFIAhdAUAR0CApAIEAQAhMA']

# Note that each of the keys used (LHS of the .) must be exactly 12 bytes / 96 bits, else urlsafeb64encode() would have them end with `=` instead
# Also note that the length of the RHS after urlsafeb64decode() would be exactly 36 bytes, meaning the original password must be 36 bytes long / 288 bits

def func_2(mval:int, kval:int) -> int:
    output = ""
    mval_binary = format(mval, "08b")
    kval_binary = format(kval, "08b")
    for i,j in zip(mval_binary, kval_binary):
        mbit = int(i) & 1
        kbit = int(j) & 1
        if not mbit^kbit or kbit and not mbit:
            output = "0" + output
        else:
            output = "1" + output
        # Truth table for the if statement would be along the lines of
        #                mbit == 0        mbit == 1
        # kbit == 0         0                 1
        # kbit == 1         0                 0
        # Note that output is only added with a "1" char IFF mbit is 1 and kbit is 0.
    return int(output, 2)


def func_1(msg:bytes, key:bytes) -> bytes:
    result = []
    for ptr in range(0, len(msg)):
        result.append(func_2(msg[ptr], key[ptr % len(key)]))
    return bytes(result)


def func_0(password:bytes, recovered_string:str) -> bool:
    key, func_1_output = recovered_string.split('.')
    key = urlsafe_b64decode(key)
    func_1_output = urlsafe_b64decode(func_1_output)
    return func_1(password, key) == func_1_output


def main_func():
    pw = b"unknown_password_data_but_we_know_it_must_be_36_bytes_long"
    if all([func_0(pw, recovered_string) for recovered_string in corrupted_strings_output]):
        if sha256(pw).hexdigest() == "8c7de08c5330d10d79d966a28d5f3f267c7ac0b605d849f0c6407be1a9a72f1e":
            print("Correct!")
        else:
            print("Wrong!")
    else:
        print("Wrong!")


"""
Solution Writeup
"""
# Observe the truth table for func_2
# When the encrypted output has a bit of 1, it must mean that the corresponding key bit must be 0, and the message bit must be 1
# Also, when the key bit is 0, the encrypted output bit is the exact same as the message bit!

# This lets us recover some amount of the password from the following:
# For each bit in the encrypted outputs provided, if the ith bit is a 1, we would therefore know:
# password[i] has to be 1
# key[i] has to be 0
# and by extension (since we know that the length of the keys must be 12 bytes)
# we would know password[(i + 96) % 288], password[(i + 96*2) % 288]
    
"""
Solution Script
"""
password = ['0'] * 288
# 'You might not be able to fully recover the password. It's okay!'
# 'You can try to replace all the unknown password bits with `0`, maybe that's the password...'

func_1_outs = ['UAFAFAAgDAgwMUJDVAVAEUw0BQAMIUpwUBVAAEw0BAAxMUIh',
        'cEEAYCFBAFNSIiJLcEUAaANRITFCZhJAcFUESANQIEIRIjIB',
        'EAFSJCFARFVQIUEFFiFSKAVANTFAIVkkEhFUCAVANEARIVEh',
        'IEFCJAEBCEEAIGFNJEVCIUMBICEMJF1EIEVEAEMAIEAAIHEB',
        'AAFAdBBhREJCEmALBCFAcBxhFABGQkwgABFEQBxgFEIBEmAh',
        'UAByJABBAFlQAgNCUARyKApBIBFIAhdAUAR0CApAIEAQAhMA']

for item in func_1_outs:
    item = urlsafe_b64decode(item)
    item_bits = format(int.from_bytes(item, "big"), "0288b")
    for item_ptr, item_bit in enumerate(item_bits):
        if item_bit == "1":
            password[item_ptr] = '1'
            password[(item_ptr + 96) % 288] = item_bits[(item_ptr + 96) % 288]
            password[(item_ptr + 96*2) % 288] = item_bits[(item_ptr + 96*2) % 288]
flag_bytes = int(''.join(password), 2).to_bytes(36, "big")
assert sha256(flag_bytes).hexdigest() == "8c7de08c5330d10d79d966a28d5f3f267c7ac0b605d849f0c6407be1a9a72f1e"
print(f'LNC24{{{flag_bytes.decode()}}}')