import random
import string

def generate_key():
    """Generate a random substitution key preserving case handling"""
    letters = list(string.ascii_uppercase)
    shuffled = letters[:]
    random.shuffle(shuffled)
    return dict(zip(letters, shuffled))

def is_valid_key(key):
    """Check if substitution key is valid"""
    return (
        set(key.keys()) == set(string.ascii_uppercase) and
        set(key.values()) == set(string.ascii_uppercase)
    )

def monoalphabetic_encrypt(text, key):
    """Encrypt text with case preservation"""
    if not is_valid_key(key):
        raise ValueError("Invalid substitution key")
    
    cipher_text = []
    for char in text:
        upper_char = char.upper()
        if upper_char in key:
            # Preserve original case
            new_char = key[upper_char]
            cipher_text.append(new_char.lower() if char.islower() else new_char)
        else:
            cipher_text.append(char)
    return ''.join(cipher_text)

def monoalphabetic_decrypt(cipher_text, key):
    """Decrypt text using substitution key"""
    reverse_key = {v: k for k, v in key.items()}
    return monoalphabetic_encrypt(cipher_text, reverse_key)

# Example Usage
if __name__ == "__main__":
    key = generate_key()
    text = "Hello World! 123 Hello"
    
    print("Substitution Key:")
    for plain, cipher in sorted(key.items()):
        print(f"{plain} → {cipher}")
    
    encrypted = monoalphabetic_encrypt(text, key)
    print(f"\nOriginal:  {text}")
    print(f"Encrypted: {encrypted}")
    
    decrypted = monoalphabetic_decrypt(encrypted, key)
    print(f"Decrypted: {decrypted}")