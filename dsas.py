import random

p = 23
q = 11
h = 2

g = pow(h, (p - 1) // q, p)
x = random.randint(1, q - 1)     
y = pow(g, x, p)                 

print("Public key:", p, q, g, y)
print("Private key:", x)

msg = "HELLO"
H = sum(ord(c) for c in msg) % q   
k = random.randint(1, q - 1)       
r = pow(g, k, p) % q
k_inv = pow(k, -1, q)
s = (k_inv * (H + x * r)) % q

print("\nMessage:", msg)
print("Signature:", r, s)

w = pow(s, -1, q)
u1 = (H * w) % q
u2 = (r * w) % q
v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

print("\nVerification value v:", v)
print("Expected r:", r)

if v == r:
    print("Signature is VALID")
else:
    print("Signature is INVALID")
