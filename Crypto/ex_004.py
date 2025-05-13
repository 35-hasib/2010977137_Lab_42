import string


key_word = input('Enter 5 letter word : ')
text = input('Plan text : ')
ff_matrix = [
    [key_word[0],key_word[1],key_word[2],key_word[3],key_word[4]],
    ['','','','',''],
    ['','','','',''],
    ['','','','',''],
    ['','','','','']
]
all_letters = list(string.ascii_lowercase)
remaining_letters = [ch for ch in all_letters if ch not in key_word]

middle1 = ''
middle2 = ''
index = 0
for i in range(1,5):
    for j in range(5):
        if i == 2 and j == 2:
            middle1 = remaining_letters[index]
            middle2 = remaining_letters[index+1]
            index += 2
            continue
        ff_matrix[i][j] = remaining_letters[index]
        index += 1

i1 = 0
i2 = 0
j1 = 0
j2 = 0
for i in range(5):
    for j in range(5):
        if text[0] == ff_matrix[i][j]:
            i1 = i
            j1 = j
        if text[1] == ff_matrix[i][j]:
            i2 = i
            j2 = j
        
ch_text = ff_matrix[i1][j2] + ff_matrix[i2][j1]

print(text,ch_text)
