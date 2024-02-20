# Observe that after applying urlsafeb64decode(), the code takes each
# <LHS>.<RHS> string in strings list, then does
# <LHS><LHS><LHS>.... xored with the flag,
# and checks if the value is RHS
# Due to the symmetric nature of xor we only really need a single one, eg.

from base64 import urlsafe_b64decode

def xor(msg:bytes, key:bytes) -> str:
    out = ""
    for i in range(0,len(msg)):
        mval = msg[i]   # in this case our msg, key are in bytes so we dont have to call ord() as if we were dealing with strings
        kval = key[i % len(key)]
        out += chr(mval ^ kval)
    return out

s = 'dOpl3PA4RINDiQQr.OKQm7sRDNNo34TRFK5gAipVKceoNzltCB7UW7K9VEcAr1jdKB9sArq9MDLct1mYaGt4XtcVLOQ=='
key = urlsafe_b64decode(s.split('.')[0])
xored_output = urlsafe_b64decode(s.split('.')[1])
flag = xor(xored_output, key)
print(flag)   # LNC24{pYth0n_reVer5iNG_is_s0_mUCh_3as1er_tH4n_b1n4ri5s}