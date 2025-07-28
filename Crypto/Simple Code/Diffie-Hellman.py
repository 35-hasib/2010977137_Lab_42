# Diffie-Hellman

import random

def power(base, exponent, modulus=None):
    if modulus is None:
        return pow(base, exponent)
    
    result = 1
    base = base % modulus  # Ensure base is within modulus
    
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result



# Prime number and primitive root
p = 23  # public
g = 5   # public

# Private keys
a = random.randint(1, p-2)
b = random.randint(1, p-2)

print(f'a = {a}')
print(f'b = {b}')

# Public keys
A = power(g, a, p)
B = power(g, b, p)

shared_key_A = pow(B, a, p)
shared_key_B = pow(A, b, p)

print("Alice's Shared Key:", shared_key_A)
print("Bob's Shared Key:", shared_key_B)

# print(power(5,-1,6))
# try:
#     print(pow(3,-1,9))
# except Exception as e:
#     print(e)