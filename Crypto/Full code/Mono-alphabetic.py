import random
import string

def generate_key():
    letters = list(string.ascii_uppercase)
    random.shuffle(letters)
    return dict(zip(string.ascii_uppercase, letters))

def encrypt(text, key):
    encrypted_text = ""
    for char in text.upper():
        if char in key:
            encrypted_text += key[char]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(ciphertext, key):
    reverse_key = {i: j for j, i in key.items()}
    return encrypt(ciphertext, reverse_key)

# Example usage
key = generate_key()
print("Key:", key)

text = "HELLO WORLD Hello 123"
print("Original:", text)

ciphertext = encrypt(text, key)
print("Encrypted:", ciphertext)

plaintext = decrypt(ciphertext, key)
print("Decrypted:", plaintext)