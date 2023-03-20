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
