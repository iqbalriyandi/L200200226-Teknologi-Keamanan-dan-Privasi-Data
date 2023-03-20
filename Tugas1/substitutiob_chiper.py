import string

def substitution_cipher(key, plaintext):
    ciphertext = ""

    alphabet = string.ascii_lowercase
    table = str.maketrans(alphabet, key)

    for char in plaintext:
        if not char.isalpha():
            ciphertext += char
            continue
        if char.islower():
            new_char = key[alphabet.index(char)]
        else:
            new_char = key[alphabet.index(char.lower())].upper()
        ciphertext += new_char

    return ciphertext

ciphertext = substitution_cipher("phqgiumeaylnofdxjkrcvstzwb", "iqbal")
print(ciphertext)
 24  
Tugas1/transposition_chiper.py
Comment on this file
@@ -0,0 +1,24 @@
def transposition_cipher(key, plaintext):
    # inisialisasi variabel
    num_columns = len(key)
    num_rows = -(-len(plaintext) // num_columns)
    matrix = [''] * num_columns

    for col in range(num_columns):
        for row in range(num_rows):
            index = col + row * num_columns
            if index < len(plaintext):
                matrix[col] += plaintext[index]
            else:
                matrix[col] += " "

    ordered_matrix = [""] * num_columns
    for i, char in enumerate(key):
        index = ord(char) - ord('0') - 1
        ordered_matrix[index] = matrix[i]
    ciphertext = "".join(ordered_matrix)

    return ciphertext

ciphertext = transposition_cipher("3142", "iqbal")
print(ciphertext)
