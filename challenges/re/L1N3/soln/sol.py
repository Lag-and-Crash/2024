from sage.all import Matrix, vector, ZZ

data = bytes([48, 17, 34, 36, 252, 17, 41, 122, 2, 41, 249, 9, 102, 43, 9, 0, 0, 40, 41, 17, 48, 183, 33, 37, 63, 19, 69, 180, 158, 134, 69, 229, 65, 31, 74, 70, 2, 111, 36, 84, 236, 48, 141, 11, 41, 76, 93, 37, 204, 121, 38, 14, 189, 70, 36, 38, 193, 70, 86, 12, 165, 36, 6, 12, 72, 101, 34, 9, 36, 215, 2, 49, 25, 43, 42, 36, 19, 40, 157, 82, 37, 27, 71, 37, 126, 24, 37, 218, 53, 37, 248, 71, 38, 29, 88, 42, 76, 91, 40, 20, 87, 48, 100, 121, 37, 74, 9, 37, 147, 12, 37, 189, 15, 37, 194, 17, 37, 252, 19, 42, 3, 99, 38, 83, 11, 38, 124, 23, 40, 40, 97, 36, 214, 7, 69, 27, 5, 57, 41, 37, 69, 49, 163, 8, 38, 92, 13, 36, 24, 2, 36, 59, 3, 36, 88, 5, 36, 112, 7, 36, 140, 11, 36, 180, 13, 36, 208, 17, 36, 239, 19, 37, 26, 23, 37, 49, 29, 37, 65, 31, 37, 114, 37, 37, 140, 41, 37, 168, 43, 37, 223, 47, 37, 227, 53, 38, 9, 59, 38, 40, 61, 38, 95, 67, 38, 123, 71, 40, 28, 37, 48, 105, 123, 73, 41, 3, 141, 37, 115, 77, 37, 154, 11, 49, 189, 78, 36, 23, 1, 36, 42, 2, 36, 83, 3, 36, 112, 4, 36, 135, 5, 36, 185, 6, 36, 205, 7, 36, 231, 8, 37, 28, 9, 37, 35, 10, 37, 89, 11, 37, 122, 12, 37, 151, 13, 37, 176, 14, 37, 209, 15, 37, 242, 16, 38, 15, 17, 38, 56, 18, 38, 77, 19, 38, 123, 20, 36, 2, 234, 72, 49, 3, 131, 48, 190, 98, 73, 75, 181, 198, 69, 152, 3, 109, 37, 171, 117, 42, 36, 14, 48, 67, 63, 41, 95, 113, 41, 193, 99, 38, 44, 87, 42, 80, 71, 36, 10, 100, 36, 52, 100, 36, 72, 100, 36, 127, 100, 36, 130, 100, 36, 188, 100, 36, 221, 100, 36, 232, 100, 37, 8, 100, 37, 56, 100, 37, 83, 100, 37, 106, 100, 37, 139, 100, 37, 164, 100, 37, 207, 100, 37, 225, 100, 38, 16, 100, 38, 44, 100, 38, 93, 100, 38, 122, 100, 36, 10, 2, 36, 42, 4, 36, 65, 6, 36, 101, 8, 36, 144, 10, 36, 175, 12, 36, 195, 14, 36, 230, 16, 37, 22, 18, 37, 61, 20, 37, 84, 22, 37, 112, 24, 37, 148, 26, 37, 162, 28, 37, 215, 30, 37, 240, 32, 38, 11, 34, 38, 57, 36, 38, 91, 38, 38, 102, 40, 40, 46, 23, 36, 184, 1, 36, 219, 46, 40, 236, 88, 69, 34, 219, 58, 73, 149, 4, 87, 49, 237, 1, 48, 163, 88, 41, 120, 67, 37, 207, 11, 42, 17, 38, 70, 127, 45, 42, 100, 79, 1, 100, 127, 40, 210, 92, 37, 52, 123, 37, 84, 78, 49, 122, 91, 74, 56, 2, 200, 36, 1, 123, 68, 41, 3, 129, 68, 74, 1, 10, 68, 98, 1, 232, 68, 148, 3, 144, 36, 173, 32, 68, 212, 30, 191, 68, 234, 3, 56, 37, 17, 179, 69, 41, 3, 231, 37, 67, 102, 69, 111, 2, 123, 69, 156, 1, 225, 69, 181, 3, 4, 69, 216, 3, 223, 69, 252, 3, 114, 70, 7, 2, 223, 38, 47, 109, 38, 65, 172, 38, 102, 81, 48, 27, 73, 40, 253, 199, 49, 65, 12, 42, 58, 52, 72, 45, 3, 214, 40, 134, 112, 36, 246, 91, 49, 58, 13, 42, 26, 17, 38, 102, 93, 0])
# extract from exe, ida export bytes, can also do idaapi.get_bytes() using ida python

checks = [65922330018, 52856248257, 20374360149, 76083475041, 3630002, 197308250928, 15601064652, 55966, 352651495789, 18265, 158186551512, 52018338329, 172100, 36530, 1352075240, 140898278897, 119407216875, 1525589, 151362416837, 23894379267]
# extract from exe, convert all to int64s

import struct
int32 = lambda x : struct.unpack('I',x[:4])[0]   # unsigned int
int24 = lambda x : struct.unpack('I',x[:3] + b'\x00')[0]
int16 = lambda x : struct.unpack('H',x[:2])[0]   # unsigned short
int8  = lambda x : struct.unpack('B', x[:1])[0]    # unsigned char

# interpret embedded data, from what we can RE of the exe
ptr = 0
prev = -1

def clen_to_coeff(clen):
    # [::-1] as this is the only instance where the data is interpreted in big endian
    if clen == 1:
        return int8(data[ptr:ptr+1][::-1])
    elif clen == 2:
        return int16(data[ptr:ptr+2][::-1])
    else:
        return int24(data[ptr:ptr+3][::-1])

# for initialising our system of linear equations
row = [0] * 20
coeff_matrix = []

# iterating through data array
while ptr < 609:
    options = int16(data[ptr:])
    clen = (options >> 5) & 0b111
    option = (options >> 2) & 0b111
    offset = (options & 0b11) * 8 + (options >> 13)
    ptr += 2   # skip past first 2 bytes which store attributes before the coeff

    # determine coefficient
    coeff = clen_to_coeff(clen)
    ptr += clen

    if offset <= prev: # one linear equation complete
        coeff_matrix.append(row)
        row = [0] * 20

    # determine flag unknown bytes that are being multiplied by coeff
    if option == 1:                # takes in little endian of int8 flag[offset]
        row[offset] += coeff
    elif option == 2:              # takes in little endian of int16 flag[offset]
        row[offset] += coeff
        row[offset+1] += coeff * 256
    else:                          # takes in little endian of int32 flag[offset]
        row[offset] += coeff
        row[offset+1] += coeff * 256
        row[offset+2] += coeff * 256**2
        row[offset+3] += coeff * 256**3  
        # fun fact, bytestrings are just glorified base-256 encodings :)
    # by default you should actually compute all of these modulo 2**64 to
    # simulate cpp unsigned int64 behaviour, but in this challenge there
    # fortunately isnt any overflow (proven below)

    prev = offset

coeff_matrix.append(row)
# coeff_matrix now contains a system of COEFF * xi for x0...x19, where each x is a character of the flag / user input


# SOLVING SYSTEM OF EQUATIONS
# z3 should work for any pure pythonists out there
coeff_matrix = Matrix(ZZ, coeff_matrix)
check_vector = vector(ZZ, checks)
print("Coefficient matrix of the system of linear equations:")
print(coeff_matrix.str())

assert all([int(i) < 2**64 for i in coeff_matrix * vector(ZZ, [256]*20)])
# note that even when we apply upper bounds of each unknown char being 256, we never breach past the 2**64 limit. There is no overflow!

assert coeff_matrix.rank() == 19 
# unfortunately the rank of the matrix one less than 20, meaning there exist a unique solution for each possible value of a certain x value from 0 to 255.
# its something like a
#     3x+2y = 100
#     6x+4y = 200
# kind of situation, where there are as many solutions as there are possible values of x
# so we brute for the first character, and see what possible solutions exist

for firstchar in range(0x20, 0x7f):
    new_matrix = []
    new_check = checks[::]
    for i in range(20):
        # if there is a non zero multiplier to the first char, deduct it accordingly
        new_check[i] -= coeff_matrix[i][0] * firstchar
        new_matrix.append(list(coeff_matrix[i])[1:])  # skips first char
    new_matrix = Matrix(ZZ, new_matrix)
    new_check = vector(ZZ, new_check)
    try:
        ans = new_matrix.solve_right(new_check)
        if all([0x20 <= j <= 0x7f and int(j) == j for j in ans]):
            print(f"Found valid solution {ans}")
            print(f"LNC24{{{ bytes( [firstchar] + [int(j) for j in ans] ).decode() }}}")
    except:
        continue



