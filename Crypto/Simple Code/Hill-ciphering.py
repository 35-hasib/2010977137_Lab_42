def hill_cipher():
    key = [[3, 3], [2, 5]]
    
    text = input("Enter text: ").upper().replace(" ", "")
    if len(text) % 2 != 0: text += 'X'  
    
    # Encrypt/decrypt
    choice = input("Encrypt (E) or Decrypt (D)? ").upper()
    result = ''
    
    for i in range(0, len(text), 2):
        # Convert letters to numbers (A=0, B=1, ...)
        a, b = ord(text[i])-65, ord(text[i+1])-65
        if choice == 'E':
            c1 = (key[0][0]*a + key[0][1]*b) % 26
            c2 = (key[1][0]*a + key[1][1]*b) % 26
            result += chr(c1 + 65) + chr(c2 + 65)
        else:
            det = (key[0][0]*key[1][1] - key[0][1]*key[1][0]) % 26
            print(det)
            det_inv = pow(det, -1, 26)
            
            inv_key = [
                [ (key[1][1] * det_inv) % 26, (-key[0][1] * det_inv) % 26 ],
                [ (-key[1][0] * det_inv) % 26, (key[0][0] * det_inv) % 26 ]
            ]
            
            p1 = (inv_key[0][0]*a + inv_key[0][1]*b) % 26
            p2 = (inv_key[1][0]*a + inv_key[1][1]*b) % 26
            result += chr(p1 + 65) + chr(p2 + 65)
    
    print(result)

# Run
hill_cipher()