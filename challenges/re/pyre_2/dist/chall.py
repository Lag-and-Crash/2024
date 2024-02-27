# Note that ? means unknown character
corrupted_strings_output = ['???????????????M.UAFAFAAgDAgwMUJDVAVAEUw0BQAMIUpwUBVAAEw0BAAxMUIh',
                            '???????????????0.cEEAYCFBAFNSIiJLcEUAaANRITFCZhJAcFUESANQIEIRIjIB',
                            '???????????????a.EAFSJCFARFVQIUEFFiFSKAVANTFAIVkkEhFUCAVANEARIVEh',
                            '???????????????y.IEFCJAEBCEEAIGFNJEVCIUMBICEMJF1EIEVEAEMAIEAAIHEB',
                            '???????????????U.AAFAdBBhREJCEmALBCFAcBxhFABGQkwgABFEQBxgFEIBEmAh',
                            '???????????????9.UAByJABBAFlQAgNCUARyKApBIBFIAhdAUAR0CApAIEAQAhMA']

def fix_corrupted_output(corrupted_strings_output):
    # step 1. ???
    # step 2. Recover all the original values of ? in corrupted_strings_output
    # step 3. Replace all the ?s in corrupted_strings_output with the original values
    # step 4. Submit flag
    return corrupted_strings_output

"""
Once you find the password, wrap it with LNC24{} headers and submit it to the ctf site
eg. password = "helloworld" -> flag is LNC24{helloworld}

You might not be able to fully recover the password. It's okay!
You can try to replace all the unknown password bits with `0`, maybe that's the password...
"""
from base64 import urlsafe_b64decode as _3
from hashlib import sha256 as _4
_2=lambda c,x:int("".join([["1","0"][not i&1^j&1 or j&1 and not i&1] for i,j in zip([int(_) for _ in format(c,"08b")],[int(_) for _ in format(x,"08b")])]),2)
_1=lambda b,y:bytes([_2(b[d],y[d%len(y)]) for d in range(0,len(b))])
_0=lambda a,z:_1(a,[_3(_) for _ in z.split('.')][0])==[_3(_) for _ in z.split('.')][1]
pw=open("pw.txt","rb").read()
print("Welcome user!" if all([_0(pw, i) for i in fix_corrupted_output(corrupted_strings_output)]) and _4(pw).hexdigest()=="8c7de08c5330d10d79d966a28d5f3f267c7ac0b605d849f0c6407be1a9a72f1e" else "Invalid user!")