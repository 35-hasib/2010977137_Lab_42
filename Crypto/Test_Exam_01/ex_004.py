import random

def power(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

# Prime number and primitive root
p = 23  # public
g = 5   # public

# Private keys
a = random.randint(1, p-2)
b = random.randint(1, p-2)

# Public keys
A = pow(g, a, p)
B = pow(g, b, p)

# Shared keys (should match)
shared_key_A = pow(B, a, p)
shared_key_B = pow(A, b, p)

print("Alice's Shared Key:", shared_key_A)
print("Bob's Shared Key:", shared_key_B)
