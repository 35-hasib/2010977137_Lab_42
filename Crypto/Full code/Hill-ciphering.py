def hill_cipher_3x3():
    # Key matrix (3x3, must be invertible mod 26)
    key = [
        [6, 24, 1],
        [13, 16, 10],
        [20, 17, 15]
    ]
    
    # Prepare text (uppercase, no spaces, pad with 'X' if needed)
    text = input("Enter text: ").upper().replace(" ", "")
    while len(text) % 3 != 0: text += 'X'  # Pad to multiple of 3
    
    # Encrypt/decrypt
    choice = input("Encrypt (E) or Decrypt (D)? ").upper()
    result = []
    
    for i in range(0, len(text), 3):
        # Convert 3 letters to numbers (A=0, B=1, ...)
        a, b, c = [ord(char)-65 for char in text[i:i+3]]
        
        if choice == 'E':
            # Encryption: Multiply key × block
            new_a = (key[0][0]*a + key[0][1]*b + key[0][2]*c) % 26
            new_b = (key[1][0]*a + key[1][1]*b + key[1][2]*c) % 26
            new_c = (key[2][0]*a + key[2][1]*b + key[2][2]*c) % 26
            result.extend([chr(new_a + 65), chr(new_b + 65), chr(new_c + 65)])
        else:
            # Decryption: Calculate inverse key first
            det = (
                key[0][0]*(key[1][1]*key[2][2] - key[1][2]*key[2][1]) -
                key[0][1]*(key[1][0]*key[2][2] - key[1][2]*key[2][0]) +
                key[0][2]*(key[1][0]*key[2][1] - key[1][1]*key[2][0])
            ) % 26
            
            det_inv = pow(det, -1, 26)  # Modular inverse of determinant
            
            # Calculate adjugate matrix
            adj = [
                [
                    (key[1][1]*key[2][2] - key[1][2]*key[2][1]) % 26,
                    (key[0][2]*key[2][1] - key[0][1]*key[2][2]) % 26,
                    (key[0][1]*key[1][2] - key[0][2]*key[1][1]) % 26
                ],
                [
                    (key[1][2]*key[2][0] - key[1][0]*key[2][2]) % 26,
                    (key[0][0]*key[2][2] - key[0][2]*key[2][0]) % 26,
                    (key[0][2]*key[1][0] - key[0][0]*key[1][2]) % 26
                ],
                [
                    (key[1][0]*key[2][1] - key[1][1]*key[2][0]) % 26,
                    (key[0][1]*key[2][0] - key[0][0]*key[2][1]) % 26,
                    (key[0][0]*key[1][1] - key[0][1]*key[1][0]) % 26
                ]
            ]
            
            # Inverse key = adjugate × det_inv mod 26
            inv_key = [[(adj[i][j] * det_inv) % 26 for j in range(3)] for i in range(3)]
            
            # Multiply inverse key × block
            new_a = (inv_key[0][0]*a + inv_key[0][1]*b + inv_key[0][2]*c) % 26
            new_b = (inv_key[1][0]*a + inv_key[1][1]*b + inv_key[1][2]*c) % 26
            new_c = (inv_key[2][0]*a + inv_key[2][1]*b + inv_key[2][2]*c) % 26
            result.extend([chr(new_a + 65), chr(new_b + 65), chr(new_c + 65)])
    
    print(''.join(result))

# Run
hill_cipher_3x3()