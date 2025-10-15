import random
from math import gcd

def generate_keys():
    print("enter p and q")
    p = int(input())
    q = int(input())
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = pow(e,-1, phi)

    return ((e, n), (d, n))

def encrypt(plaintext, public_key):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(ciphertext, private_key):
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

public_key, private_key = generate_keys()
print("Public Key:", public_key)
print("Private Key:", private_key)

message = "kaiju8"
cipher = encrypt(message, public_key)
print("Encrypted:", cipher)

decrypted = decrypt(cipher, private_key)
print("Decrypted:", decrypted)
