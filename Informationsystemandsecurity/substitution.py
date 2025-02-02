# Substitution Technique: Caesar Cipher

def caesar_cipher_encrypt(plaintext, shift):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher_encrypt(ciphertext, -shift)


# Example Usage
plaintext = "HELLO WORLD"
shift = 3

# Encryption
encrypted_text = caesar_cipher_encrypt(plaintext, shift)
# Decryption
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)

# Results
print("Original Text:", plaintext)
print("Encrypted Text (Substitution):", encrypted_text)
print("Decrypted Text (Substitution):", decrypted_text)
