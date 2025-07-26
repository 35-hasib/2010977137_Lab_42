def encryption(text, shift):
    result = ''
    for i in text:
        if i.isalpha():
            shift_base = ord('A') if i.isupper() else ord('a')
            result += chr((ord(i) - shift_base + shift) %26 + shift_base)
        else:
            result += i
    return result

text = input("Enter text : ")
shift = int(input("Enter shift value (0-25): "))

print("Encrypted text:", encryption(text, shift))