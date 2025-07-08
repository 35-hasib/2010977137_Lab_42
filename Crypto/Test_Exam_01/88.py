def affine_point(a,b,p):
    points = []
    for x in range(p):
        rhs = (pow(x,3,p) + (a*x)%p + b%p ) % p #x^3+ax+b
        for y in range(p):
            lhs = pow(y,2,p)
            if(lhs == rhs):
                points.append({x,y})
    return points

# a = 0
# b = 9
# p = 936

# print(affine_point(a,b,p))
# print(len(affine_point(a,b,p)))

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


max_a = []
max_l = 0
for i in range(1001):
    if(is_prime(i)):
        for j in range(i):
            for k in range(i):
                l = len(affine_point(j,k,i))
                if(l > max_l):
                    max_a = [j,k,i,l]
                    max_l = l
                    print(max_a)

