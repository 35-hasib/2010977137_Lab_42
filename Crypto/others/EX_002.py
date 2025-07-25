import string
import random
from collections import Counter

# 1. Generate a substitution key (A-Z shuffled)
def generate_key():
    alphabet = list(string.ascii_uppercase)
    shuffled = alphabet[:]
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled))

# 2. Encrypt message
def encrypt(text, key):
    text = text.upper()
    result = ''
    for char in text:
        if char in key:
            result += key[char]
        else:
            result += char  # Keep spaces, punctuation unchanged
    return result

# 3. Decrypt message
def decrypt(ciphertext, key):
    reversed_key = {v: k for k, v in key.items()}
    result = ''
    for char in ciphertext:
        if char in reversed_key:
            result += reversed_key[char]
        else:
            result += char
    return result

# 4. Frequency analysis
def frequency_analysis(text):
    letters_only = [c for c in text.upper() if c in string.ascii_uppercase]
    total = len(letters_only)
    counts = Counter(letters_only)
    for letter, count in counts.most_common():
        print(f"{letter}: {round((count / total) * 100, 2)}%")

# --- Example Usage ---
message = input("Enter Message : ")
key = generate_key()

encrypted = encrypt(message, key)
print(f"\nEncrypted Message: {encrypted}")

decrypted = decrypt(encrypted, key)
print(f"\nDecrypted Message: {decrypted}")

print("\nFrequency Analysis of Encrypted Message:")
frequency_analysis(encrypted)
