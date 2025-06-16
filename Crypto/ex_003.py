
p, q = 61, 53  
n = p * q
phi = (p-1)*(q-1)
e = 17
d = pow(e, -1, phi)  # Modular inverse
print(d)
# Get input
msg = 'Crypto/test.txt'
with open(msg, 'r') as f:
    msg = f.read()

# Encrypt
cipher = [pow(ord(c), e, n) for c in msg]
print("Encrypted:", cipher)

# Decrypt
decrypted = ''.join([chr(pow(c, d, n)) for c in cipher])
print("Decrypted:", decrypted)