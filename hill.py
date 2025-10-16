def modinv(a, m=26):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def det_mod(M, mod=26):
    n = len(M)
    if n == 1:
        return M[0][0] % mod
    if n == 2:
        return (M[0][0]*M[1][1] - M[0][1]*M[1][0]) % mod
    det = 0
    for c in range(n):
        minor = [row[:c] + row[c+1:] for row in M[1:]]
        det += ((-1)**c) * M[0][c] * det_mod(minor, mod)
    return det % mod

def matrix_minor(M, i, j):
    return [row[:j] + row[j+1:] for r, row in enumerate(M) if r != i]

def adjugate(M, mod=26):
    n = len(M)
    adj = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            minor = matrix_minor(M, i, j)
            adj[j][i] = ((-1)**(i+j)) * det_mod(minor, mod)
    return [[adj[i][j] % mod for j in range(n)] for i in range(n)]

def inverse_matrix(M, mod=26):
    det = det_mod(M, mod)
    inv_det = modinv(det, mod)
    if inv_det is None:
        raise ValueError("Matrix not invertible mod 26")
    adj = adjugate(M, mod)
    return [[(adj[i][j]*inv_det) % mod for j in range(len(M))] for i in range(len(M))]

def text_to_num(text):
    return [ord(c) - 65 for c in text.upper() if c.isalpha()]

def num_to_text(nums):
    return ''.join(chr(n % 26 + 65) for n in nums)

def matmul(A, B, mod=26):
    n = len(A)
    res = [0]*n
    for i in range(n):
        for j in range(n):
            res[i] += A[i][j] * B[j]
        res[i] %= mod
    return res

def encrypt(pt, key):
    n = len(key)
    nums = text_to_num(pt)
    while len(nums) % n != 0:
        nums.append(ord('X') - 65)
    ct = ""
    for i in range(0, len(nums), n):
        block = nums[i:i+n]
        enc = matmul(key, block)
        ct += num_to_text(enc)
    return ct

def decrypt(ct, key):
    inv = inverse_matrix(key)
    n = len(inv)
    nums = text_to_num(ct)
    pt = ""
    for i in range(0, len(nums), n):
        block = nums[i:i+n]
        dec = matmul(inv, block)
        pt += num_to_text(dec)
    return pt
key = [
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
]

text = input("Enter text: ").upper()
cipher = encrypt(text, key)
plain = decrypt(cipher, key)

print("Ciphertext:", cipher)
print("Decrypted:", plain)
