key = 'HILL'
m_key = [[ord(key[0])-65,ord(key[1])-65],
         [ord(key[2])-65,ord(key[3])-65]]

def en(text):
    result = ''
    for i in range(0,len(text),2):
        a = ord(text[i]) - 65
        b = ord(text[i+1]) - 65
        
        c = (a * m_key[0][0] + b * m_key[1][0]) % 26
        d = (a * m_key[0][1] + b * m_key[1][1]) % 26
        
        result += chr(c+65) + chr(d+65)
    return result
    
def de(text):
    det = (m_key[0][0] * m_key[1][1] - m_key[0][1] * m_key[1][0]) % 26
    inv_det = pow(det,-1,26)
    
    inv_key = [[(m_key[1][1] * inv_det) % 26 , (-m_key[0][1] * inv_det) % 26],
               [(-m_key[1][0] * inv_det) % 26 , (m_key[0][0] * inv_det) % 26]]
    
    
    result = ''
    for i in range(0,len(text),2):
        a = ord(text[i]) - 65
        b = ord(text[i+1]) - 65
        
        c = (a * inv_key[0][0] + b * inv_key[1][0]) % 26
        d = (a * inv_key[0][1] + b * inv_key[1][1]) % 26
        
        result += chr(c+65) + chr(d+65)
    return result

text = input('Enter text : ').upper().replace(" ","")
lenth = len(text)
if(len(text) % 2 != 0) : text += 'X'

cipher_text = en(text)
print(cipher_text)
de_text = de(cipher_text)
# remove padding
actual_text = ''
for i in range(lenth):
    actual_text += de_text[i]
print(actual_text)

