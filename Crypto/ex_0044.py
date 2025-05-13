import re

def prepare_key(key):
    """Prepare the key matrix for Playfair cipher"""
    key = key.upper().replace("J", "I")
    key = re.sub(r"[^A-Z]", "", key)  # Remove non-alphabetic characters
    
    # Create key matrix (5x5)
    key_matrix = []
    for char in key:
        if char not in key_matrix:
            key_matrix.append(char)
    print(key_matrix)
    # Fill remaining with alphabet (excluding J)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in key_matrix:
            key_matrix.append(char)
    
    # Convert to 5x5 matrix
    return [key_matrix[i*5:(i+1)*5] for i in range(5)]

def prepare_text(text):
    """Prepare plaintext for encryption"""
    text = text.upper().replace("J", "I")
    text = re.sub(r"[^A-Z]", "", text)  # Remove non-alphabetic characters
    
    # Split into digraphs, adding X if needed
    digraphs = []
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            digraphs.append(text[i] + "X")
        elif text[i] == text[i+1]:
            digraphs.append(text[i] + "X")
            i += 1
        else:
            digraphs.append(text[i] + text[i+1])
            i += 2
    return digraphs

def find_position(matrix, char):
    """Find row and column of a character in the matrix"""
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return (i, j)
    return (None, None)

def encrypt(plaintext, key):
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
    
    return " ".join(ciphertext)

def decrypt(ciphertext, key):
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
    
    return "".join(plaintext)

def main():
    print("Playfair Cipher Implementation")
    
    while True:
        print("\nMenu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            key = input("Enter the key: ")
            plaintext = input("Enter the plaintext: ")
            encrypted = encrypt(plaintext, key)
            print(f"\nEncrypted text: {encrypted}")
        
        elif choice == "2":
            key = input("Enter the key: ")
            ciphertext = input("Enter the ciphertext: ")
            decrypted = decrypt(ciphertext, key)
            print(f"\nDecrypted text: {decrypted}")
        
        elif choice == "3":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()