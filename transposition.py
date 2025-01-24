# Transposition Technique: Columnar Transposition Cipher

def columnar_transposition_encrypt(plaintext, key):
    matrix = ['' for _ in range(len(key))]
    for index, char in enumerate(plaintext):
        column = index % len(key)
        matrix[column] += char

    # Arrange columns by the order of the key
    sorted_columns = sorted([(k, matrix[i]) for i, k in enumerate(key)])
    encrypted = ''.join(column for _, column in sorted_columns)
    return encrypted

def columnar_transposition_decrypt(ciphertext, key):
    num_columns = len(key)
    num_rows = len(ciphertext) // num_columns
    extra_chars = len(ciphertext) % num_columns

    sorted_columns = sorted(enumerate(key), key=lambda x: x[1])
    column_lengths = [num_rows + 1 if i < extra_chars else num_rows for i in range(num_columns)]

    index = 0
    matrix = ['' for _ in range(num_columns)]
    for col_index, _ in sorted_columns:
        matrix[col_index] = ciphertext[index:index + column_lengths[col_index]]
        index += column_lengths[col_index]

    decrypted = ''
    for row in range(num_rows + 1):
        for col in range(num_columns):
            if row < len(matrix[col]):
                decrypted += matrix[col][row]

    return decrypted


# Example Usage
plaintext = "HELLO WORLD".replace(" ", "")  # Removing spaces for transposition
key = "31542"

# Encryption
encrypted_text = columnar_transposition_encrypt(plaintext, key)
# Decryption
decrypted_text = columnar_transposition_decrypt(encrypted_text, key)

# Results
print("Original Text:", plaintext)
print("Encrypted Text (Transposition):", encrypted_text)
print("Decrypted Text (Transposition):", decrypted_text)
