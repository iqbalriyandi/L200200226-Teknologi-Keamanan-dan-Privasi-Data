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
