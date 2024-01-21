CHAR_SET = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ """
MSG = "So I heard that caesar cipher is too simple and decided to make it more complex! :)"

msg_enc = 'H7t*a&qqGtE@/nPv0qMMadh{796W`-kxW8j< /rf~F@%qxG6gvAUH9w%,V;DHa7zBd:\\ wC1(,1,d/a*/HK@H==r%k:BxpwB'
msg_iv = b'Iu\x11\x90l\xc5\x0c3\xc0\xf3y\xa9\xea0\x05\xf0'    
flag_enc = "E}'mLQDAMl(>9]<\\@RJo;VZBcX[z:^;01Al`Vrn.D/caYK,v"
flag_iv = b'MRp\xe8\x8cmt\xce\x89.\x91\xad\x15\\E\\'

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
