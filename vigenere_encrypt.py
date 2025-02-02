def vigenere_encrypt(plaintext, key):
    """Encrypt plaintext using Vigenere Cipher"""
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper()
    
    key_extended = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]
    ciphertext = ""

    for p, k in zip(plaintext, key_extended):
        c = (ord(p) - ord('A') + (ord(k) - ord('A'))) % 26 + ord('A')
        ciphertext += chr(c)

    return ciphertext

def vigenere_decrypt(ciphertext, key):
    """Decrypt ciphertext using Vigenere Cipher"""
    ciphertext = ciphertext.upper()
    key = key.upper()

    key_extended = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    plaintext = ""

    for c, k in zip(ciphertext, key_extended):
        p = (ord(c) - ord('A') - (ord(k) - ord('A'))) % 26 + ord('A')
        plaintext += chr(p)

    return plaintext

# Example usage
plaintext = "HELLO WORLD"
key = "KEY"

ciphertext = vigenere_encrypt(plaintext, key)
decrypted_text = vigenere_decrypt(ciphertext, key)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted_text)
