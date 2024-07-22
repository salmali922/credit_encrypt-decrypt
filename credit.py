from cryptography.fernet import Fernet

# Generate a key for encryption (this should be securely stored and not hardcoded in production)
def generate_key():
    return Fernet.generate_key()

# Function to encrypt credit card number
def encrypt(number,key):
    cipher_suite = Fernet(key)
    encrypted_num = cipher_suite.encrypt(number.encode())
    return encrypted_num

# Function to decrypt credit card number
def decrypt(encrypted_num, key):
    cipher_suite = Fernet(key)
    decrypted_num = cipher_suite.decrypt(encrypted_num).decode()
    return decrypted_num

# Example usage
if __name__ == "__main__":
    # Generate and store a key securely
   
    
    # Example credit card number
    number = input("Enter the number :")
    key = generate_key()
    print("Generated Key:", key)
    
    # Encrypt the credit card number
    encrypted = encrypt(number, key)
    print("Encrypted:", encrypted)
    
    # Decrypt the encrypted number
    decrypted = decrypt(encrypted, key)
    print("Decrypted:", decrypted)


