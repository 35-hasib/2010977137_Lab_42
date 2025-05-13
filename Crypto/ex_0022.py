import string
import random
from collections import Counter

def generate_key():
    alphabet = list(string.ascii_uppercase)
    shuffled = alphabet[:]
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled))

def encrypt(text, key):
    result = ''
    for char in text:
        if char.upper() in key:
            enc = key[char.upper()]
            result += enc if char.isupper() else enc.lower()
        else:
            result += char  
    return result

def decrypt(ciphertext, key):
    reversed_key = {v: k for k, v in key.items()}
    result = ''
    for char in ciphertext:
        if char.upper() in reversed_key:
            dec = reversed_key[char.upper()]
            result += dec if char.isupper() else dec.lower()
        else:
            result += char
    return result

def frequency_analysis(text):
    letters_only = [c.upper() for c in text if c.upper() in string.ascii_uppercase]
    total = len(letters_only)
    counts = Counter(letters_only)
    for letter, count in counts.most_common():
        print(f"{letter}: {round((count / total) * 100, 2)}%")


message = input("Enter Message : ")
key = generate_key()
print(key)
encrypted = encrypt(message, key)
print(f"\nEncrypted Message: {encrypted}")

decrypted = decrypt(encrypted, key)
print(f"\nDecrypted Message: {decrypted}")

print("\nFrequency Analysis of Encrypted Message:")
frequency_analysis(encrypted)
