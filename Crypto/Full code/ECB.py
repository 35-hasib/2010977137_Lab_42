# Helper functions
def to_bit_string(text):
    return ''.join(f'{ord(c):08b}' for c in text)

def from_bit_string(bits):
    return ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))

def xor_bits(bits1, bits2):
    return ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(bits1, bits2))

# Encrypt function
def simple_bit_encrypt(plaintext, key):
    plain_bits = to_bit_string(plaintext)
    key_bits = to_bit_string(key)

    repeated_key_bits = (key_bits * ((len(plain_bits) // len(key_bits)) + 1))[:len(plain_bits)]

    encrypted_bits = xor_bits(plain_bits, repeated_key_bits)
    return from_bit_string(encrypted_bits)

# Decrypt function (same logic as encrypt)
def simple_bit_decrypt(ciphertext, key):
    encrypted_bits = to_bit_string(ciphertext)
    key_bits = to_bit_string(key)

    repeated_key_bits = (key_bits * ((len(encrypted_bits) // len(key_bits)) + 1))[:len(encrypted_bits)]

    decrypted_bits = xor_bits(encrypted_bits, repeated_key_bits)
    return from_bit_string(decrypted_bits)

# Example
key = "k"
text = "Hasib"

encrypted = simple_bit_encrypt(text, key)
decrypted = simple_bit_decrypt(encrypted, key)

print("Original :", text)
print("Encrypted:", encrypted)  # This might show strange symbols
print("Decrypted:", decrypted)
