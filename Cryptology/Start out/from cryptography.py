from cryptography.fernet import Fernet
import csv

# Generate a key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Save the key to a file (important to keep this secure!)
with open('secret.key', 'wb') as key_file:
    key_file.write(key)

# Encrypt the CSV file
with open('file.csv', 'rb') as file:
    file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)

# Save the encrypted data to a new file
with open('file_encrypted.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted_data)

# Load the key
with open('secret.key', 'rb') as key_file:
    key = key_file.read()
    cipher_suite = Fernet(key)

# Decrypt the CSV file
with open('file_encrypted.csv', 'rb') as encrypted_file:
    encrypted_data = encrypted_file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)

# Save the decrypted data to a new file
with open('file_decrypted.csv', 'wb') as decrypted_file:
    decrypted_file.write(decrypted_data)
