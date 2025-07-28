
matrix = [[0 for _ in range(5)] for _ in range(5)]

def genarate_matrix(text):
    
    used = set()
    final = []
    for char in text:
        if char not in used and char.isalpha():
            used.add(char)
            final.append(char)
    index = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = final[index]
            index += 1
    return matrix

def padding(text):
    result = ''
    i = 0
    while i < len(text):
        b = text[i+1] if i+1 < len(text) else 'X'
        if(text[i] == b):
            result += text[i] + 'X'
            i += 1
        else:
            result += text[i] + b
            i+=2
    return result

def find_position(char,m):
    for i in range(5):
        for j in range(5):
            if(char == m[i][j]): return i,j

def encrypt(text,m):
    result = ''
    
    for i in range(0,len(text),2):
        r1,c1 = find_position(text[i],m)
        r2,c2 = find_position(text[i+1],m)
        
        if r1 == r2 :
            result += m[r1][(c1+1)%5] + m[r2][(c2+1)%5]
        elif c1 == c2 :
            result += m[(r1+1)%5][c1] + m[(r2+1)%5][c2]
        else:
            result += m[r1][c2] + m[r2][c1]
    return result

def dencrypt(text,m):
    result = ''
    
    for i in range(0,len(text),2):
        r1,c1 = find_position(text[i],m)
        r2,c2 = find_position(text[i+1],m)
        
        if r1 == r2 :
            result += m[r1][(c1-1)%5] + m[r2][(c2-1)%5]
        elif c1 == c2 :
            result += m[(r1-1)%5][c1] + m[(r2-1)%5][c2]
        else:
            result += m[r1][c2] + m[r2][c1]
    return result

key = 'HGFDS'
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
all = key + alpha
all = all.replace('J', 'I')

mat = genarate_matrix(all)
for i in range(5):
    print(mat[i])


text = 'Hellou'.upper()

padd_text = padding(text)
print(padd_text)

cipher_text = encrypt(padd_text,mat)
print(cipher_text)

cipher_text = dencrypt(cipher_text,mat)
print(cipher_text)
