
text = input("Enter text: ")
key = int(input("Enter key (0-25): "))
choice = input("Type 'e' for encrypt or 'd' for decrypt: ")

result = ""
for ch in text:
    if ch.isalpha():  
        if ch.isupper():
            base = ord('A')
        else:
            base = ord('a')

        if choice == 'e':  
            result += chr((ord(ch) - base + key) % 26 + base)
        else: 
            result += chr((ord(ch) - base - key) % 26 + base)
    else:
        result += ch 

print("Result:", result)
