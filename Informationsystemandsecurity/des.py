from Crypto.Cipher import DES
import binascii

def pad(text):
    # Pad text to be a multiple of 8 bytes (DES block size)
    while len(text) % 8 != 0:
        text += ' '
    return text

def des_encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)  # Creating DES cipher object
    padded_text = pad(plain_text)  # Padding text
    encrypted_text = cipher.encrypt(padded_text.encode())
    return binascii.hexlify(encrypted_text).decode()

def des_decrypt(encrypted_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(binascii.unhexlify(encrypted_text)).decode().rstrip(' ')
    return decrypted_text

# Example usage
if __name__ == "__main__":
    key = b'8charKey'  # DES key must be exactly 8 bytes
    plain_text = "HelloDES"
    
    encrypted = des_encrypt(plain_text, key)
    print(f"Encrypted Text: {encrypted}")
    
    decrypted = des_decrypt(encrypted, key)
    print(f"Decrypted Text: {decrypted}")
