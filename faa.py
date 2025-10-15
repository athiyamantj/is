cipher = input("Enter ciphertext: ").strip()

counts = [0] * 26
for ch in cipher:
    if ch.isalpha():
        counts[ord(ch.lower()) - ord('a')] += 1

if sum(counts) == 0:
    print("No letters found.")
else:
    idx = max(range(26), key=lambda i: counts[i])
    most = chr(idx + ord('a'))
    print("Most frequent ciphertext letter:", most)

    def decrypt_with_key(text, key):
        out = ""
        for ch in text:
            if ch.isalpha():
                base = ord('A') if ch.isupper() else ord('a')
                out += chr((ord(ch) - base - key) % 26 + base)
            else:
                out += ch
        return out

    for plain_guess in ('e', 't','a'):
        key = (idx - (ord(plain_guess) - ord('a'))) % 26
        print("\nAssume", most, "->", plain_guess, "(key=", key, "):")
        print(decrypt_with_key(cipher, key))
