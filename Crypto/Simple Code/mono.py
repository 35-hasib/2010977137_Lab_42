key = 'QWERTYUIOPASDFGHJKLZXCVBNM'
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

maping = [[0 for _ in range(2)] for _ in range(26)]

for i in range(26):
    maping[i][0] = alpha[i]
    maping[i][1] = key[i]


def for_en(c):
    for i in range(26):
        if(c == maping[i][0]):
            return maping[i][1]

def for_de(c):
    for i in range(26):
        if(c == maping[i][1]):
            return maping[i][0]

def en(text):
    result = ''
    for i in text:
        if i in alpha:
            result += for_en(i)
        else:
            result += i
    return result

def de(text):
    result = ''
    for i in text:
        if i in alpha:
            result += for_de(i)
        else:
            result += i
    return result

text = input('Enter Text : ')
text = text.upper()
cipher_text = en(text)
print(cipher_text)
de_text = de(cipher_text)
print(de_text)