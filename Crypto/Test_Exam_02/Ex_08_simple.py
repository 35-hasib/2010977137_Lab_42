class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

class TinyECC:
    def __init__(self):
        # Using a tiny curve: y² = x³ + 2x + 2 mod 17
        self.a = 2
        self.b = 2
        self.p = 17
    
    def add(self, P, Q):
        if P.x == 0 and P.y == 0: return Q
        if Q.x == 0 and Q.y == 0: return P
        if P.x == Q.x and P.y != Q.y: return Point(0, 0)
        
        if P != Q:
            # Slope for point addition
            m = (Q.y - P.y) * pow(Q.x - P.x, -1, self.p) % self.p
        else:
            # Slope for point doubling
            m = (3 * P.x**2 + self.a) * pow(2 * P.y, -1, self.p) % self.p
        
        x_r = (m**2 - P.x - Q.x) % self.p
        y_r = (m * (P.x - x_r) - P.y) % self.p
        
        return Point(x_r, y_r)
    
    def multiply(self, P, n):
        result = Point(0, 0)
        current = P
        
        while n > 0:
            if n % 2 == 1:
                result = self.add(result, current)
            current = self.add(current, current)
            n = n // 2
        
        return result

# Create our tiny curve
tiny_curve = TinyECC()

# Base point (one of the points on our tiny curve)
G = Point(5, 1)

# Alice's key pair (small numbers for demonstration)
alice_private = 3
alice_public = tiny_curve.multiply(G, alice_private)

# Bob's key pair
bob_private = 7
bob_public = tiny_curve.multiply(G, bob_private)

# Shared secret computation
alice_shared = tiny_curve.multiply(bob_public, alice_private)
bob_shared = tiny_curve.multiply(alice_public, bob_private)

print("Tiny ECC Example")
print("---------------")
print(f"Base point G: {G}")
print(f"Alice's private key: {alice_private}")
print(f"Alice's public key: {alice_public}")
print(f"Bob's private key: {bob_private}")
print(f"Bob's public key: {bob_public}")
print("\nKey Exchange Results:")
print(f"Alice's shared secret: {alice_shared}")
print(f"Bob's shared secret: {bob_shared}")
print(f"Secrets match: {alice_shared == bob_shared}")