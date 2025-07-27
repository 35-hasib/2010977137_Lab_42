p = 1051
q = 863
e = 6521

n = p * q
phi = (p-1) * (q-1)

d = pow(e,-1,phi)
print(d)
print(f"Public key (e, n): ({e}, {n})")

c = int(input("Enter a number: "))
m = pow(c,d,n)

print(f"M: {m}")

M = str(m)
if(len(M) % 2 != 0): M = '0' + M

result = ''
for i in range(0,len(M),2):
    result += chr(ord('A')-1+(int(M[i]+M[i+1]) % 26))
print("Decrypted message:", result)
