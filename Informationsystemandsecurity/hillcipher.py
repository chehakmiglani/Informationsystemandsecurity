import numpy as np

def text_to_numbers(text):
    """Convert text to numerical values (A=0, B=1, ..., Z=25)"""
    return [ord(char) - ord('A') for char in text.upper()]

def numbers_to_text(numbers):
    """Convert numerical values back to text"""
    return ''.join(chr(num + ord('A')) for num in numbers)

def mod_inverse_matrix(matrix, modulus):
    """Find the modular inverse of a matrix under given modulus"""
    det = int(np.round(np.linalg.det(matrix)))  # Compute determinant
    det_inv = pow(det, -1, modulus)  # Modular inverse of determinant
    
    # Compute adjugate matrix
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    return (det_inv * adjugate) % modulus  # Apply modular inverse

def hill_cipher_encrypt(plaintext, key_matrix):
    """Encrypts plaintext using Hill Cipher"""
    plaintext = plaintext.upper().replace(" ", "")
    n = len(key_matrix)  # Size of the key matrix
    
    # Pad plaintext if necessary
    while len(plaintext) % n != 0:
        plaintext += 'X'
    
    # Convert plaintext to numbers
    plaintext_nums = text_to_numbers(plaintext)
    ciphertext_nums = []
    
    # Encrypt block by block
    for i in range(0, len(plaintext_nums), n):
        block = np.array(plaintext_nums[i:i+n]).reshape(-1, 1)
        cipher_block = np.dot(key_matrix, block) % 26
        ciphertext_nums.extend(cipher_block.flatten())
    
    return numbers_to_text(ciphertext_nums)

def hill_cipher_decrypt(ciphertext, key_matrix):
    """Decrypts ciphertext using Hill Cipher"""
    key_inverse = mod_inverse_matrix(key_matrix, 26)
    ciphertext_nums = text_to_numbers(ciphertext)
    plaintext_nums = []
    
    # Decrypt block by block
    for i in range(0, len(ciphertext_nums), len(key_matrix)):
        block = np.array(ciphertext_nums[i:i+len(key_matrix)]).reshape(-1, 1)
        plain_block = np.dot(key_inverse, block) % 26
        plaintext_nums.extend(plain_block.flatten())
    
    return numbers_to_text(plaintext_nums)

# Example usage
key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])  # 3x3 key matrix
plaintext = "HELLO"
ciphertext = hill_cipher_encrypt(plaintext, key_matrix)
decrypted_text = hill_cipher_decrypt(ciphertext, key_matrix)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted_text)
