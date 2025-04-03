from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def rsa_encrypt(plain_text, public_key):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted_text = cipher.encrypt(plain_text.encode())
    return binascii.hexlify(encrypted_text).decode()

def rsa_decrypt(encrypted_text, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_text = cipher.decrypt(binascii.unhexlify(encrypted_text)).decode()
    return decrypted_text

# Example usage
if __name__ == "__main__":
    private_key, public_key = generate_keys()
    plain_text = "HelloRSA"
    
    encrypted = rsa_encrypt(plain_text, public_key)
    print(f"Encrypted Text: {encrypted}")
    
    decrypted = rsa_decrypt(encrypted, private_key)
    print(f"Decrypted Text: {decrypted}")
