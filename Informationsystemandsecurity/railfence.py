def encrypt_rail_fence(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    dir_down = False
    row, col = 0, 0

    for char in text:
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        rail[row][col] = char
        col += 1
        row += 1 if dir_down else -1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)


def decrypt_rail_fence(cipher, key):
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    dir_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if dir_down else -1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        result.append(rail[row][col])
        col += 1
        row += 1 if dir_down else -1
    return "".join(result)


def columnar_transposition_encrypt(text, key):
    text = text.replace(" ", "").upper()
    col_matrix = [""] * key

    for i in range(len(text)):
        col_matrix[i % key] += text[i]

    return "".join(col_matrix)


def columnar_transposition_decrypt(cipher, key):
    num_cols = key
    num_rows = len(cipher) // key
    if len(cipher) % key:
        num_rows += 1

    col_lengths = [num_rows] * key
    extra_chars = len(cipher) % key
    for i in range(extra_chars):
        col_lengths[i] -= 1

    index = 0
    cols = []
    for length in col_lengths:
        cols.append(cipher[index: index + length])
        index += length

    decrypted_text = ""
    for i in range(num_rows):
        for j in range(num_cols):
            if i < len(cols[j]):
                decrypted_text += cols[j][i]

    return decrypted_text


# Example Usage
text = "HELLO RAIL FENCE CIPHER"
key = 3

# Step 1: Rail Fence Cipher
rail_encrypted = encrypt_rail_fence(text.replace(" ", ""), key)
rail_decrypted = decrypt_rail_fence(rail_encrypted, key)

# Step 2: Columnar Transposition
column_encrypted = columnar_transposition_encrypt(rail_encrypted, key)
column_decrypted = columnar_transposition_decrypt(column_encrypted, key)

print(f"Original Text: {text}")
print(f"Rail Fence Encrypted: {rail_encrypted}")
print(f"Column Transposition Encrypted: {column_encrypted}")
print(f"Column Transposition Decrypted: {column_decrypted}")
print(f"Rail Fence Decrypted: {rail_decrypted}")
