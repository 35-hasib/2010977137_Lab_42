import random
import math

p, q = 61, 53  
n = p * q
phi = (p-1)*(q-1)
# e = 17
e = 2
while True:
    print('Try to Finding e...')
    e = random.randint(2, phi - 1)
    if math.gcd(e, phi) == 1:
        break
print("Public key (n, e):", (n, e))

d = pow(e, -1, phi)
print(d)
# Get input
msg = open('input.txt').read().strip() or input("Enter text to encrypt: ")

# Encrypt
cipher = [pow(ord(c), e, n) for c in msg]
print("Encrypted:", cipher)

# Decrypt
decrypted = ''.join([chr(pow(c, d, n)) for c in cipher])
print("Decrypted:", decrypted)