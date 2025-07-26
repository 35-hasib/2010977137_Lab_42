import math
# Given ,
p, q = 61, 53  
n = p * q
phi = (p-1)*(q-1)
# e = 17
e = 2
while True:
    e += 1
    if math.gcd(e, phi) == 1:
        break
print("Public key (n, e) :", (n, e))

d = pow(e, -1, phi)
print(f'd = {d}')
# Get input
msg = input("Enter text to encrypt: ")

# Encrypt
cipher = [pow(ord(c), e, n) for c in msg] # c^e mod n
print("Encrypted:", cipher)

# Decrypt
decrypted = ''
for c in cipher:
    decrypted += chr(pow(c,d,n))
print("Decrypted:", decrypted)


