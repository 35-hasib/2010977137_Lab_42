def prepare_key(key):
    """Prepare the key matrix for Playfair cipher"""
    key = key.upper().replace("J", "I")
    key = key.replace(" ", "")
    
    # Add remaining letters (I and J share same position)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_matrix = []
    
    for char in key + alphabet:
        if char not in key_matrix:
            key_matrix.append(char)
            if len(key_matrix) == 25:
                break
    
    # Convert to 5x5 matrix
    return [key_matrix[i*5:(i+1)*5] for i in range(5)]

def prepare_text(text):
    """Prepare plaintext for encryption"""
    text = text.upper().replace("J", "I")
    text = text.replace(" ", "")
    
    # Split into digraphs and handle double letters
    digraphs = []
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            digraphs.append(text[i] + 'X')
            break
        if text[i] == text[i+1]:
            digraphs.append(text[i] + 'X')
            i += 1
        else:
            digraphs.append(text[i] + text[i+1])
            i += 2
    return digraphs

def find_position(matrix, char):
    """Find row and column of a character in the key matrix"""
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return -1, -1

def playfair_encrypt(plaintext, key):
    """Encrypt plaintext using Playfair cipher"""
    matrix = prepare_key(key)
    digraphs = prepare_text(plaintext)
    ciphertext = []
    
    for digraph in digraphs:
        a, b = digraph[0], digraph[1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        
        # Same row
        if row_a == row_b:
            ciphertext.append(matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5])
        # Same column
        elif col_a == col_b:
            ciphertext.append(matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b])
        # Rectangle
        else:
            ciphertext.append(matrix[row_a][col_b] + matrix[row_b][col_a])
    
    return ' '.join(ciphertext)

def playfair_decrypt(ciphertext, key):
    """Decrypt ciphertext using Playfair cipher"""
    matrix = prepare_key(key)
    ciphertext = ciphertext.replace(" ", "")
    digraphs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    plaintext = []
    
    for digraph in digraphs:
        a, b = digraph[0], digraph[1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        
        # Same row
        if row_a == row_b:
            plaintext.append(matrix[row_a][(col_a - 1) % 5] + matrix[row_b][(col_b - 1) % 5])
        # Same column
        elif col_a == col_b:
            plaintext.append(matrix[(row_a - 1) % 5][col_a] + matrix[(row_b - 1) % 5][col_b])
        # Rectangle
        else:
            plaintext.append(matrix[row_a][col_b] + matrix[row_b][col_a])
    
    # Remove any padding X's that don't make sense
    decrypted = ''.join(plaintext)
    if decrypted[-1] == 'X':
        decrypted = decrypted[:-1]
    for i in range(1, len(decrypted)):
        if decrypted[i] == 'X' and decrypted[i-1] == decrypted[i+1]:
            decrypted = decrypted[:i] + decrypted[i+1:]
    
    return decrypted

def print_matrix(matrix):
    """Print the 5x5 key matrix"""
    print("Playfair Key Matrix:")
    for row in matrix:
        print(' '.join(row))
    print()

# Example usage
if __name__ == "__main__":
    key = "MONARCHY"
    plaintext = "HELLO"
    
    print("Key:", key)
    matrix = prepare_key(key)
    print_matrix(matrix)
    
    print("Plaintext:", plaintext)
    ciphertext = playfair_encrypt(plaintext, key)
    print("Encrypted:", ciphertext)
    
    decrypted = playfair_decrypt(ciphertext, key)
    print("Decrypted:", decrypted)