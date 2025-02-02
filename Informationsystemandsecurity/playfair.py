import itertools

def generate_playfair_matrix(key):
    key = "".join(dict.fromkeys(key.upper().replace("J", "I")))  # Remove duplicates, replace J with I
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = list(dict.fromkeys(key + alphabet))  # Remove duplicates again
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None, None

def playfair_cipher(text, key, encrypt=True):
    matrix = generate_playfair_matrix(key)
    text = text.upper().replace("J", "I")
    text_pairs = []

    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'

        if a == b:
            text_pairs.append((a, 'X'))
            i += 1  # Don't move i+2 since we inserted 'X'
        else:
            text_pairs.append((a, b))
            i += 2

    result = ""
    for a, b in text_pairs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:  # Same row: Shift right (encrypt) or left (decrypt)
            col1 = (col1 + 1) % 5 if encrypt else (col1 - 1) % 5
            col2 = (col2 + 1) % 5 if encrypt else (col2 - 1) % 5
        elif col1 == col2:  # Same column: Shift down (encrypt) or up (decrypt)
            row1 = (row1 + 1) % 5 if encrypt else (row1 - 1) % 5
            row2 = (row2 + 1) % 5 if encrypt else (row2 - 1) % 5
        else:  # Rectangle swap
            col1, col2 = col2, col1

        result += matrix[row1][col1] + matrix[row2][col2]

    return result

# Example usage
key = "KEYWORD"
plaintext = "HELLO"
ciphertext = playfair_cipher(plaintext, key, encrypt=True)
decrypted_text = playfair_cipher(ciphertext, key, encrypt=False)

print(f"Encrypted: {ciphertext}")
print(f"Decrypted: {decrypted_text}")
