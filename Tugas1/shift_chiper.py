def shift_cipher(key, plaintext):
    plaintext = "".join([chr(int(digit) + 97) for digit in plaintext])

    ciphertext = ""

    for char in plaintext:
        if not char.isalpha():
            ciphertext += char
            continue

        char_offset = ord(char.lower()) - 97
        new_offset = (char_offset + key) % 26
        new_char = chr(new_offset + 97)
        if char.isupper():
            new_char = new_char.upper()
        ciphertext += new_char

    return ciphertext

ciphertext = shift_cipher(5, "33")
print(ciphertext)
