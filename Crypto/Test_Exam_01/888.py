P = 23
def affine_point(a,b,p):
    points = []
    for x in range(p):
        rhs = (pow(x,3,p) + (a*x)%p + b%p ) % p #x^3+ax+b
        for y in range(p):
            lhs = (y*y)%p
            if(lhs == rhs):
                points.append([x,y])
    return points

def point_add(G,A):
    p1 = G[0]
    p2 = G[1]
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


# ------------
a = 9
b = 7
p = 23
points = affine_point(a,b,p)
print(points)

G = points[0]

G2 = point_add(G,a)


