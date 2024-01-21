CHAR_SET = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ """
MSG = "So I heard that caesar cipher is too simple and decided to make it more complex! :)"

msg_enc = 'u>LM0SN%E,%GXrLELFa|QY,g7E*,v=c>_\'FD-&W}0Z,vIPuJqm2+Q21|}\\Yx &NVNc#P4rX{V^xC#jtB{Op<X:28j;T\'X]L"'
msg_iv = b'\xf8\xb7\xdf\x12\x07W\xe5\xb8\xbcY2x~\x91\x05\x98'    
flag_enc = '9j8u8apNmulSp:\']"c.AHSuxW>z5tK,)/\'ZI :Eh8AvstJYs'  
flag_iv = b'\x8b\xbf2\x90[d\xe2\xa5\xc1\xe2\xdd\x84\x15c\xf2\xe6'

def unpad(message: str):  # Unpad message
    padding_len = CHAR_SET.find(message[-1])
    return message[:-padding_len]

def v(x):  # Get position of x in character set
    return CHAR_SET.index(x)

# Update IV values
msg_iv += msg_enc.encode()
flag_iv += flag_enc.encode()

enc_diff = [v(c)-v(m) for m, c in zip(MSG, msg_enc)]
iv_diff = [iv2-iv1 for iv1, iv2 in zip(msg_iv, flag_iv)]
flag = "".join(CHAR_SET[(v(c)-x-iv) % len(CHAR_SET)] for c, x, iv in zip(flag_enc, enc_diff, iv_diff))
flag = unpad(flag)

print(f"Flag: {flag}")
