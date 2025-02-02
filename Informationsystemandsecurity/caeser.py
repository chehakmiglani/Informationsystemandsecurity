def caesar_cipher(text, shift, encrypt=True):
    result = ""
    shift = shift if encrypt else -shift  # Reverse shift for decryption

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char  # Keep non-alphabet characters unchanged
    return result

# Example usage
plaintext = "HELLO WORLD"
shift = 3
encrypted_text = caesar_cipher(plaintext, shift)
decrypted_text = caesar_cipher(encrypted_text, shift, encrypt=False)

print(f"Encrypted: {encrypted_text}")  # KHOOR ZRUOG
print(f"Decrypted: {decrypted_text}")  # HELLO WORLD
