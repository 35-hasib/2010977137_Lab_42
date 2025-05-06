def mod_inverse(n, m):
    t, new_t = 0, 1
    r, new_r = m, n
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        return None
    if t < 0:
        t += m
    return t

p = int(input('Enter prime number 1 : '))
q = int(input('Enter Prime number 2 : '))
n = p*q
pn = (p-1)*(q-1)
print(f'Phi of n : {pn}')

e = int(input('Enter e for encryption : '))
d = mod_inverse(e,pn)
print(f'd = {d}')
M = int(input(('Enter M : ')))
C = M**e % n
print(f'C = {C}')
M = C**d % n
print(f'M = {M}')




