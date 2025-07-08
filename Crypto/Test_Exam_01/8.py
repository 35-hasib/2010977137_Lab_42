# Minimal ECDH using secp256k1 (Bitcoin's curve)
P = 23  # Prime field
A = 9
B = 7
Gx = 5
Gy = 4
# N = 23

def affine_point(a,b,p):
    points = []
    for x in range(p):
        rhs = (pow(x,3,p) + (a*x)%p + b%p ) % p #x^3+ax+b
        for y in range(p):
            lhs = pow(y,2,p)
            if(lhs == rhs):
                points.append({a,b})
    return points


def point_add(p1, p2):
    if p1 is None:
        return p2
    if p2 is None:
        return p1
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2 and y1 != y2:
        return None
    if x1 == x2:
        m = (3 * x1 * x1 + A) * pow(2 * y1, P-2, P)
    else:
        m = (y2 - y1) * pow(x2 - x1, P-2, P)
    x3 = (m * m - x1 - x2) % P
    y3 = (m * (x1 - x3) - y1) % P
    return (x3, y3)

def scalar_mult(k, point):
    result = None
    current = point
    while k:
        if k & 1:
            result = point_add(result, current)
        current = point_add(current, current)
        k >>= 1
    return result




# # Alice's private key 
# a = 3
# # Bob's private key
# b = 9


# # Public keys
# A_pub = scalar_mult(a, (Gx, Gy))
# B_pub = scalar_mult(b, (Gx, Gy))

# # Shared secrets
# shared_a = scalar_mult(a, B_pub)
# shared_b = scalar_mult(b, A_pub)

# print("Shared secrets match:", shared_a == shared_b)  # Should print True