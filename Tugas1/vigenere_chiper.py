def vigenere_cipher(key, plaintext):
    plaintext = "".join([chr(int(digit) + 97) for digit in plaintext])

    ciphertext = ""
    key_index = 0

    for char in plaintext:
        if not char.isalpha():
            ciphertext += char
            continue

        key_char = key[key_index % len(key)]
        key_index += 1
        key_index = key_index % len(key)
        key_offset = ord(key_char) - 97

        char_offset = ord(char.lower()) - 97
        new_offset = (char_offset + key_offset) % 26

        new_char = chr(new_offset + 97)
        if char.isupper():
            new_char = new_char.upper()
        ciphertext += new_char

    return ciphertext

ciphertext = vigenere_cipher("secret", "iqbal")
print(ciphertext)
