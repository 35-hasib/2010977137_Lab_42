import string
from collections import Counter
import re

# Sample ciphertext (replace with yours)
ciphertext = "QYTTO J XN QXCVV"

# Frequency analysis (single letters)
def single_letter_frequency(text):
    letters = [c.upper() for c in text if c.isalpha()]
    total = len(letters)
    counter = Counter(letters)
    print("\n--- Single Letter Frequency ---")
    for letter, count in counter.most_common():
        percent = (count / total) * 100
        print(f"{letter}: {round(percent, 2)}%")

# Digrams (2-letter patterns)
def digram_frequency(text):
    text = ''.join(c.upper() for c in text if c.isalpha())
    digrams = [text[i:i+2] for i in range(len(text)-1)]
    counter = Counter(digrams)
    print("\n--- Top Digrams ---")
    for digram, count in counter.most_common(10):
        print(f"{digram}: {count}")

# Trigrams (3-letter patterns)
def trigram_frequency(text):
    text = ''.join(c.upper() for c in text if c.isalpha())
    trigrams = [text[i:i+3] for i in range(len(text)-2)]
    counter = Counter(trigrams)
    print("\n--- Top Trigrams ---")
    for trigram, count in counter.most_common(10):
        print(f"{trigram}: {count}")

# Manual substitution helper
def manual_decrypt(text, substitution):
    result = ''
    for char in text:
        upper = char.upper()
        if upper in substitution:
            new_char = substitution[upper]
            # Preserve original case
            result += new_char if char.isupper() else new_char.lower()
        else:
            result += char
    return result

# Example partial substitution (user guesses)
# Replace with your own guesses
substitution_guess = {
    'L': 'H',
    'X': 'E',
    'I': 'L',
    'R': 'O',
    'E': 'T',
    'O': 'U',
    'V': 'F',
    'S': 'I',
    'Z': 'K'
}

# Analyze
single_letter_frequency(ciphertext)
digram_frequency(ciphertext)
trigram_frequency(ciphertext)

# Show partially decrypted text
print("\n--- Manual Decryption Attempt ---")
decrypted = manual_decrypt(ciphertext, substitution_guess)
print("Decrypted (with guesses):", decrypted)
