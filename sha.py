a = 0x67452301
b = 0xEFCDAB89
c = 0x98BADCFE
d = 0x10325476
e = 0xC3D2E1F0
o=input()
w=int(o,16)
def f(b, c, d):
    return (b & c) | ((~b) & d)

K = 0x5A827999

def left_rotate(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

temp = (left_rotate(a, 5) + f(b, c, d) + e + K + w) & 0xFFFFFFFF
e = d
d = c
c = left_rotate(b, 30)
b = a
a = temp

print(hex(a), hex(b), hex(c), hex(d), hex(e))
