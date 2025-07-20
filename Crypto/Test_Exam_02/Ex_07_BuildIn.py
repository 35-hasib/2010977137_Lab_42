# Block cipher modes of operation

# ECB mode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def ecb_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return base64.b64encode(ciphertext).decode()

def ecb_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(ciphertext))
    return unpad(decrypted, AES.block_size).decode()

# Example usage
key = b'Sixteen byte key'  # Must be 16, 24, or 32 bytes
plaintext = "Hello World ECB mode"
encrypted = ecb_encrypt(plaintext, key)
decrypted = ecb_decrypt(encrypted, key)

print(f"ECB Mode:\nOriginal: {plaintext}\nEncrypted: {encrypted}\nDecrypted: {decrypted}\n")


# CBC mode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def cbc_encrypt(plaintext, key):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return base64.b64encode(iv + ciphertext).decode()

def cbc_decrypt(ciphertext, key):
    data = base64.b64decode(ciphertext)
    iv = data[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(data[AES.block_size:])
    return unpad(decrypted, AES.block_size).decode()

# Example usage
key = b'Sixteen byte key'
plaintext = "Hello World CBC mode"
encrypted = cbc_encrypt(plaintext, key)
decrypted = cbc_decrypt(encrypted, key)

print(f"CBC Mode:\nOriginal: {plaintext}\nEncrypted: {encrypted}\nDecrypted: {decrypted}\n")


# CFB mode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def cfb_encrypt(plaintext, key):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    ciphertext = cipher.encrypt(plaintext.encode())
    return base64.b64encode(iv + ciphertext).decode()

def cfb_decrypt(ciphertext, key):
    data = base64.b64decode(ciphertext)
    iv = data[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return cipher.decrypt(data[AES.block_size:]).decode()

# Example usage
key = b'Sixteen byte key'
plaintext = "Hello World CFB mode"
encrypted = cfb_encrypt(plaintext, key)
decrypted = cfb_decrypt(encrypted, key)

print(f"CFB Mode:\nOriginal: {plaintext}\nEncrypted: {encrypted}\nDecrypted: {decrypted}\n")


# OFB mode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def ofb_encrypt(plaintext, key):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_OFB, iv)
    ciphertext = cipher.encrypt(plaintext.encode())
    return base64.b64encode(iv + ciphertext).decode()

def ofb_decrypt(ciphertext, key):
    data = base64.b64decode(ciphertext)
    iv = data[:AES.block_size]
    cipher = AES.new(key, AES.MODE_OFB, iv)
    return cipher.decrypt(data[AES.block_size:]).decode()

# Example usage
key = b'Sixteen byte key'
plaintext = "Hello World OFB mode"
encrypted = ofb_encrypt(plaintext, key)
decrypted = ofb_decrypt(encrypted, key)

print(f"OFB Mode:\nOriginal: {plaintext}\nEncrypted: {encrypted}\nDecrypted: {decrypted}\n")

