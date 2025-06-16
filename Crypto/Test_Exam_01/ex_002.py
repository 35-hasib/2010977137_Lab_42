def generate_matrix(key):
    matrix = []
    used = set()
    key = key.upper().replace("J", "I")

    for char in key:
        if char not in used and char.isalpha():
            matrix.append(char)
            used.add(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            matrix.append(char)
            used.add(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt(text, key):
    matrix = generate_matrix(key)
    print(matrix)
    text = text.upper().replace("J", "I").replace(" ", "")
    
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i + 1 < len(text) else 'X'
        if a == b:
            b = 'X'
            i += 1
        else:
            i += 2
        pairs.append((a, b))
        print(f"Pair: {a}, {b}")

    encrypted = ""
    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            encrypted += matrix[r1][(c1 + 1) % 5]
            encrypted += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            encrypted += matrix[(r1 + 1) % 5][c1]
            encrypted += matrix[(r2 + 1) % 5][c2]
        else:
            encrypted += matrix[r1][c2]
            encrypted += matrix[r2][c1]
    return encrypted

def playfair_decrypt(ciphertext, key):
    matrix = generate_matrix(key)
    text = ciphertext.upper().replace("J", "I").replace(" ", "")
    
    decrypted = ""
    for i in range(0, len(text), 2):
        a = text[i]
        b = text[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            decrypted += matrix[r1][(c1 - 1) % 5]
            decrypted += matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            decrypted += matrix[(r1 - 1) % 5][c1]
            decrypted += matrix[(r2 - 1) % 5][c2]
        else:
            decrypted += matrix[r1][c2]
            decrypted += matrix[r2][c1]
    return decrypted

# Example
key = "alpha"
plaintext = "HELLO WORLD"
ciphertext = playfair_encrypt(plaintext, key)
original = playfair_decrypt(ciphertext, key)

print("Encrypted:", ciphertext)
print("Decrypted:", original)
