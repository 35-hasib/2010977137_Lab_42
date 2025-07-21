import numpy as np

def prepare_text(text, block_size):
    """Prepare text by removing non-letters and padding with 'X' if needed"""
    text = ''.join([c.upper() for c in text if c.isalpha()])
    padding = (block_size - len(text) % block_size) % block_size
    return text + 'X' * padding

def text_to_numbers(text):
    """Convert letters to numbers (A=0, B=1, ..., Z=25)"""
    return [ord(c) - ord('A') for c in text]

def numbers_to_text(numbers):
    """Convert numbers back to letters"""
    return ''.join([chr(n + ord('A')) for n in numbers])

def get_key_matrix(key, size):
    """Convert key string into a square matrix"""
    key_numbers = text_to_numbers(key)
    return np.array(key_numbers).reshape(size, size)

def mod_inverse_matrix(matrix, modulus):
    """Calculate modular inverse of matrix"""
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)
    adjugate = np.round(np.linalg.inv(matrix) * det).astype(int)
    return (det_inv * adjugate) % modulus

def hill_encrypt(plaintext, key_matrix):
    """Encrypt plaintext using Hill cipher"""
    block_size = key_matrix.shape[0]
    print(f"Block size: {block_size}")
    plaintext = prepare_text(plaintext, block_size)
    numbers = text_to_numbers(plaintext)
    
    ciphertext = []
    for i in range(0, len(numbers), block_size):
        block = numbers[i:i+block_size]
        encrypted_block = np.dot(key_matrix, block) % 26
        ciphertext.extend(encrypted_block)
    
    return numbers_to_text(ciphertext)

def hill_decrypt(ciphertext, key_matrix):
    """Decrypt ciphertext using Hill cipher"""
    block_size = key_matrix.shape[0]
    numbers = text_to_numbers(ciphertext)
    inv_matrix = mod_inverse_matrix(key_matrix, 26)
    
    plaintext = []
    for i in range(0, len(numbers), block_size):
        block = numbers[i:i+block_size]
        decrypted_block = np.dot(inv_matrix, block) % 26
        plaintext.extend(decrypted_block)
    
    return numbers_to_text(plaintext)

# Example usage with 3x3 matrix
if __name__ == "__main__":
    # Key must be 9 letters for 3x3 matrix
    key = "HILLHASIB"  # Example 3x3 key
    plaintext = "ATTACK ON TITAN"
    
    # Convert key to matrix
    key_matrix = get_key_matrix(key, 3)
    
    # Encryption
    ciphertext = hill_encrypt(plaintext, key_matrix)
    print(f"Plaintext:  {plaintext}")
    print(f"Key Matrix:\n{key_matrix}")
    print(f"Ciphertext: {ciphertext}")
    
    # Decryption
    decrypted = hill_decrypt(ciphertext, key_matrix)
    print(f"Decrypted:  {decrypted}")