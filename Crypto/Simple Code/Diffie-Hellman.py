# Diffie-Hellman

import random

# Prime number and primitive root
p = 23  # public
g = 5   # public

# Private keys
a = random.randint(1, p-2)
b = random.randint(1, p-2)

print(f'a = {a}')
print(f'b = {b}')

# Public keys
A = pow(g, a, p)
B = pow(g, b, p)

shared_key_A = pow(B, a, p)
shared_key_B = pow(A, b, p)

print("Alice's Shared Key:", shared_key_A)
print("Bob's Shared Key:", shared_key_B)
