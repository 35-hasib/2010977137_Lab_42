B = 2


def padd(text,padd_len):
    return text + bytes([padd_len] * padd_len)

def unpadd(text,padd_len):
    return text[:-padd_len]

def x_or(block,key):
    return bytes([block[i] ^ key[i % len(key)] for i in range(B)])

def x_or_str(block,key):
    result = ''
    for i in range(len(block)):
        if(block[i] == key[i]): result += '0'
        else: result += '1'
    return result

def ecb_en(text,key,padd_len):
    text = padd(text,padd_len)
    result = b''
    for i in range(0,len(text),B):
        block = text[i:i+B]
        result += x_or(block,key)
    return result

def ecb_de(text,key,padd_len):
    result = b''
    for i in range(0,len(text),B):
        block = text[i:i+B]
        result += x_or(block,key)
    return unpadd(result,padd_len)

text = input('Enter a text : ')

rr = ''

for i in text:
    rr += format(ord(i),'08b')

key = b'SK'
padd_len = B - len(text) % B
text = text.encode()

en_text = ecb_en(text,key,padd_len)
de_text = ecb_de(en_text,key,padd_len)

print(en_text)
print(de_text.decode())

print(x_or_str('01010101','01010100'))


