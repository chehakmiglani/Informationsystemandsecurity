from Crypto.Cipher import AES
import binascii
from Crypto.Util.Padding import pad, unpad

def aes_encrypt(plain_text, key):
    cipher = AES.new(key, AES.MODE_ECB)  # AES with ECB mode
    padded_text = pad(plain_text.encode(), AES.block_size)  # Padding text
    encrypted_text = cipher.encrypt(padded_text)
    return binascii.hexlify(encrypted_text).decode()

def aes_decrypt(encrypted_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(binascii.unhexlify(encrypted_text)), AES.block_size).decode()
    return decrypted_text

# Example usage
if __name__ == "__main__":
    key = b'16byteAESkey1234'  # AES key must be exactly 16 bytes
    plain_text = "HelloAES"
    
    encrypted = aes_encrypt(plain_text, key)
    print(f"Encrypted Text: {encrypted}")
    
    decrypted = aes_decrypt(encrypted, key)
    print(f"Decrypted Text: {decrypted}")
