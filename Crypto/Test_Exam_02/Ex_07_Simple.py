import base64

# Simplified ECB mode AES implementation (educational purposes only)
def simple_ecb_encrypt(plaintext, key):
    # Pad the plaintext to be multiple of 16 bytes
    padding_length = 16 - (len(plaintext) % 16)
    padded_text = plaintext.encode() + bytes([padding_length] * padding_length)
    
    # Split into 16-byte blocks
    blocks = [padded_text[i:i+16] for i in range(0, len(padded_text), 16)]
    
    # Simple XOR "encryption" (in real AES this would be much more complex)
    ciphertext = b''
    for block in blocks:
        encrypted_block = bytes([block[i] ^ key[i % len(key)] for i in range(16)])
        ciphertext += encrypted_block
    
    return base64.b64encode(ciphertext).decode()

def simple_ecb_decrypt(ciphertext, key):
    # Decode from base64
    ciphertext = base64.b64decode(ciphertext)
    
    # Split into 16-byte blocks
    blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    
    # Simple XOR "decryption"
    decrypted = b''
    for block in blocks:
        decrypted_block = bytes([block[i] ^ key[i % len(key)] for i in range(16)])
        decrypted += decrypted_block
    
    # Remove padding
    padding_length = decrypted[-1]
    return decrypted[:-padding_length].decode()

# Example usage
key = b'Sixteen byte key'  # Must be 16 bytes for this simple version
plaintext = "Hello World ECB"
encrypted = simple_ecb_encrypt(plaintext, key)
decrypted = simple_ecb_decrypt(encrypted, key)

print(f"Simplified ECB Mode:")
print(f"Original: {plaintext}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")


# CFB mode (simplified version)
import os
import base64

def simple_cbc_encrypt(plaintext, key):
    # Generate random IV (16 bytes)
    iv = os.urandom(16)
    
    # Pad plaintext to multiple of 16 bytes
    padding_length = 16 - (len(plaintext) % 16)
    padded_text = plaintext.encode() + bytes([padding_length] * padding_length)
    
    # Split into blocks
    blocks = [padded_text[i:i+16] for i in range(0, len(padded_text), 16)]
    
    # Encrypt each block
    ciphertext = b''
    previous_block = iv
    for block in blocks:
        # XOR with previous ciphertext block (or IV for first block)
        xored = bytes([block[i] ^ previous_block[i] for i in range(16)])
        # "Encrypt" with simple XOR (in real AES this would be complex)
        encrypted_block = bytes([xored[i] ^ key[i % len(key)] for i in range(16)])
        ciphertext += encrypted_block
        previous_block = encrypted_block
    
    return base64.b64encode(iv + ciphertext).decode()

def simple_cbc_decrypt(ciphertext, key):
    data = base64.b64decode(ciphertext)
    iv = data[:16]
    ciphertext_blocks = [data[i:i+16] for i in range(16, len(data), 16)]
    
    decrypted = b''
    previous_block = iv
    for block in ciphertext_blocks:
        # "Decrypt" with simple XOR
        decrypted_block = bytes([block[i] ^ key[i % len(key)] for i in range(16)])
        # XOR with previous ciphertext block
        plain_block = bytes([decrypted_block[i] ^ previous_block[i] for i in range(16)])
        decrypted += plain_block
        previous_block = block
    
    # Remove padding
    padding_length = decrypted[-1]
    return decrypted[:-padding_length].decode()

# Example usage
key = b'Sixteen byte key'
plaintext = "Hello World CBC mode"
encrypted = simple_cbc_encrypt(plaintext, key)
decrypted = simple_cbc_decrypt(encrypted, key)

print(f"Simplified CBC Mode:\nOriginal: {plaintext}\nEncrypted: {encrypted}\nDecrypted: {decrypted}\n")


# CFB mode (simplified version)

def simple_cfb_encrypt(plaintext, key):
    iv = os.urandom(16)
    cipher = bytes([iv[i] ^ key[i % len(key)] for i in range(16)])  # "Encrypt" IV
    
    ciphertext = b''
    previous_block = cipher
    for i in range(0, len(plaintext), 16):
        block = plaintext.encode()[i:i+16]
        # XOR plaintext with encrypted previous block
        encrypted_block = bytes([block[j] ^ previous_block[j] for j in range(len(block))])
        ciphertext += encrypted_block
        # Next block uses current ciphertext as input
        previous_block = bytes([encrypted_block[j] ^ key[j % len(key)] for j in range(len(encrypted_block))])
    
    return base64.b64encode(iv + ciphertext).decode()

def simple_cfb_decrypt(ciphertext, key):
    data = base64.b64decode(ciphertext)
    iv = data[:16]
    ciphertext_blocks = data[16:]
    
    decrypted = b''
    previous_block = bytes([iv[i] ^ key[i % len(key)] for i in range(16)])
    for i in range(0, len(ciphertext_blocks), 16):
        block = ciphertext_blocks[i:i+16]
        # XOR ciphertext with encrypted previous block
        decrypted_block = bytes([block[j] ^ previous_block[j] for j in range(len(block))])
        decrypted += decrypted_block
        # Next block uses current ciphertext as input
        previous_block = bytes([block[j] ^ key[j % len(key)] for j in range(len(block))])
    
    return decrypted.decode()

# Example usage
plaintext = "Hello World CFB mode"
encrypted = simple_cfb_encrypt(plaintext, key)
decrypted = simple_cfb_decrypt(encrypted, key)

print(f"Simplified CFB Mode:\nOriginal: {plaintext}\nEncrypted: {encrypted}\nDecrypted: {decrypted}\n")


# OFB mode (simplified version)

def simple_ofb_encrypt(plaintext, key):
    iv = os.urandom(16)
    
    ciphertext = b''
    feedback = bytes([iv[i] ^ key[i % len(key)] for i in range(16)])  # Initial encryption
    
    for i in range(0, len(plaintext), 16):
        block = plaintext.encode()[i:i+16]
        # XOR plaintext with feedback
        encrypted_block = bytes([block[j] ^ feedback[j] for j in range(len(block))])
        ciphertext += encrypted_block
        # Generate next feedback
        feedback = bytes([feedback[j] ^ key[j % len(key)] for j in range(len(feedback))])
    
    return base64.b64encode(iv + ciphertext).decode()

def simple_ofb_decrypt(ciphertext, key):
    data = base64.b64decode(ciphertext)
    iv = data[:16]
    ciphertext_blocks = data[16:]
    
    decrypted = b''
    feedback = bytes([iv[i] ^ key[i % len(key)] for i in range(16)])
    
    for i in range(0, len(ciphertext_blocks), 16):
        block = ciphertext_blocks[i:i+16]
        # XOR ciphertext with feedback
        decrypted_block = bytes([block[j] ^ feedback[j] for j in range(len(block))])
        decrypted += decrypted_block
        # Generate next feedback
        feedback = bytes([feedback[j] ^ key[j % len(key)] for j in range(len(feedback))])
    
    return decrypted.decode()

# Example usage
plaintext = "Hello World OFB mode"
encrypted = simple_ofb_encrypt(plaintext, key)
decrypted = simple_ofb_decrypt(encrypted, key)

print(f"Simplified OFB Mode:\nOriginal: {plaintext}\nEncrypted: {encrypted}\nDecrypted: {decrypted}\n")



