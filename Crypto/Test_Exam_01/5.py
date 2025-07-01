import numpy as np
from math import gcd

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise Exception("Modular inverse does not exist.")

def is_invertible_mod26(matrix):
    det = int(round(np.linalg.det(matrix)))
    return gcd(det, 26) == 1, det

def create_matrix_of_text(text, size):
    text = text.upper().replace(" ", "")
    while len(text) % size != 0:
        text += 'X'
    nums = [ord(char) - ord('A') for char in text]
    return np.array(nums).reshape(-1, size)

def encrypt(plaintext, key):
    n = key.shape[0]
    blocks = create_matrix_of_text(plaintext, n)
    cipher = (np.dot(blocks, key) % 26).astype(int)
    return ''.join(chr(num + ord('A')) for row in cipher for num in row)

def decrypt(ciphertext, key):
    n = key.shape[0]
    blocks = create_matrix_of_text(ciphertext, n)
    det = int(round(np.linalg.det(key)))
    det_inv = mod_inverse(det, 26)
    adj = np.round(det * np.linalg.inv(key)).astype(int)
    key_inv = (det_inv * adj) % 26
    plain = (np.dot(blocks, key_inv) % 26).astype(int)
    return ''.join(chr(num + ord('A')) for row in plain for num in row)

# === Main ===
key = np.array([[3, 3], [2, 5]])
plaintext = "HELLO"

invertible, det = is_invertible_mod26(key)
if not invertible:
    print(f"Key is not invertible mod 26. Determinant = {det}")
else:
    print("Plaintext:", plaintext)
    ciphertext = encrypt(plaintext, key)
    print("Encrypted:", ciphertext)
    decrypted = decrypt(ciphertext, key)
    print("Decrypted:", decrypted)
