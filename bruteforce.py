cipher = input("Enter ciphertext: ")
cipher = cipher.strip()

for key in range(26):
    plain = ""
    for ch in cipher:
        if ch.isalpha():
            if ch.isupper():
                base = ord('A')
            else:
                base = ord('a')
            plain += chr((ord(ch) - base - key) % 26 + base)
        else:
            plain += ch
    print(f"Key {key:2d}: {plain}")
