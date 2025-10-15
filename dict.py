import itertools
import string
import hashlib

letters = string.ascii_letters    # a-zA-Z (52 chars)
digits = string.digits            # 0-9 (10 chars)

out_path = "dictionary_with_sha256.txt"

with open(out_path, "w", encoding="utf-8") as f:
    for a, b, c, d in itertools.product(letters, letters, digits, digits):
        pwd = f"{a}{b}{c}{d}"
        h = hashlib.sha256(pwd.encode("utf-8")).hexdigest()
        f.write(f"{pwd}:{h}\n")

print("Written", out_path)
