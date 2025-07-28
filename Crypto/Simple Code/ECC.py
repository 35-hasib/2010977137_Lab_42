a = 1
b = 2
p = 13


def add(A,B):
    if A == [0,0]: return B
    if B == [0,0]: return A
    if A[0] == B[0] and A[1] != B[1]: return [0, 0]
    
    if A != B:
        s = (B[1] - A[1]) * pow(B[0] - A[0], -1, p) % p
    else:
        if A[1] == 0: return [0, 0]
        s = (3 * A[0]**2 + a) * pow(2 * A[1], -1, p) % p
    
    g_x = (s**2 - A[0] - B[0]) % p
    g_y = (s * (A[0] - g_x) - A[1])% p
    
    return [g_x, g_y]

def multiply(GG, n):
    result = [0,0]
    current = GG
    while n > 0:
        if n%2 != 0:
            result = add(result, current)
        current = add(current,current)
        n //= 2
    return result

G = [7,1]


alice_private = 3
bob_private = 7

alice_public = multiply(G, alice_private)
bob_public = multiply(G, bob_private)

print("Alice's public key:", alice_public)
print("Bob's public key:", bob_public)

alice_sheared = multiply(bob_public, alice_private)
bob_sheared = multiply(alice_public, bob_private)

print("Alice's shared secret:", alice_sheared)
print("Bob's shared secret:", bob_sheared)


