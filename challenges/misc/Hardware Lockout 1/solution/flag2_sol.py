enc = "uwz.0BPft0]-fT`f,Nwf-Wz,]+W~fJq,L+]f[-fJ0_-D"
arr = enc.encode()
xor_dec = []

for i in range(len(arr)):
	c = arr[i] ^ 0x39
	if 0x21 <= c:
		xor_dec.append(c)
	else:
		c = arr[i] - 0x23
		xor_dec.append(c ^ 0x39)
	
print(bytearray(xor_dec).decode())
