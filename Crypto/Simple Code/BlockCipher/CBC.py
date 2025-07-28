B = 16

def string_tobinary(text):
    result = ''
    for i in text:
        result += format(ord(i),'08b')
    return result

def binary_tostring(text,bit=8):
    return_text = ''
    for i in range(0,len(text),bit):
        result = ''
        result = text[i:i+bit]
        number = int(result,2)
        return_text += chr(number)
    return return_text

def x_or_str(block,key):
    result = ''
    for i in range(len(block)):
        if(block[i] == key[i]): result += '0'
        else: result += '1'
    return result

def ecb_en(text,key,bit=B):
    iv = '0101010101010101'
    pre = iv
    result = ''
    for i in range(0,len(text),bit):
        block = text[i:i+bit]
        pre_en = x_or_str(block,pre)
        en = x_or_str(pre_en,key)
        pre = en
        result += en
    return result

def ecb_de(text,key,bit=B):
    iv = '0101010101010101'
    pre = iv
    result = ''
    for i in range(0,len(text),bit):
        block = text[i:i+bit]
        pre_de = x_or_str(block,key)
        en = x_or_str(pre_de,pre)
        pre = block
        result += en
    return binary_tostring(result)
        

text = input('Enter a text : ')

text = string_tobinary(text)
key = 'SK'
key = string_tobinary(key)

padd_len = B - len(text) % B
text += '0'*padd_len
print(text)
cipher_text = ecb_en(text,key)
print(cipher_text)
plan_text = ecb_de(cipher_text,key)
print(plan_text)