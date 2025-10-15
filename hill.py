
def text_to_num(text):
    return [ord(c) - 65 for c in text]

def num_to_text(nums):
    return ''.join(chr(n % 26 + 65) for n in nums)

def matmul3x3(A, B):
    res = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            res[i] += A[i][j] * B[j]
        res[i] %= 26
    return res

def det3x3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])) % 26

def modinv(a):
    for i in range(1,26):
        if (a*i)%26==1:
            return i
    return None

def adj3x3(M):
    a,b,c = M[0]; d,e,f = M[1]; g,h,i = M[2]
    adj = [
        [(e*i - f*h), -(b*i - c*h), (b*f - c*e)],
        [-(d*i - f*g), (a*i - c*g), -(a*f - c*d)],
        [(d*h - e*g), -(a*h - b*g), (a*e - b*d)]
    ]
    # transpose
    return [[adj[j][i] for j in range(3)] for i in range(3)]

def inv3x3(M):
    det = det3x3(M)
    invdet = modinv(det)
    adj = adj3x3(M)
    return [[(adj[i][j]*invdet)%26 for j in range(3)] for i in range(3)]

def encrypt(pt, key):
    pt = pt.upper().replace(" ","")
    while len(pt)%3!=0:
        pt += 'X'
    ct = ""
    for i in range(0,len(pt),3):
        block = text_to_num(pt[i:i+3])
        enc = matmul3x3(key, block)
        ct += num_to_text(enc)
    return ct

def decrypt(ct, key):
    inv = inv3x3(key)
    pt = ""
    for i in range(0,len(ct),3):
        block = text_to_num(ct[i:i+3])
        dec = matmul3x3(inv, block)
        pt += num_to_text(dec)
    return pt

# Example key
key = [
    [6,24,1],
    [13,16,10],
    [20,17,15]
]

text = input("Enter text: ").upper()
cipher = encrypt(text, key)
plain = decrypt(cipher, key)

print("Ciphertext:", cipher)
print("Decrypted:", plain)