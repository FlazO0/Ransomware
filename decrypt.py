from cryptography.fernet import Fernet
import os

# Load the key
key_path = 'key.key'

with open(key_path, 'rb') as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Decrypt files in the docs directory
docs_dir = 'PC'

for filename in os.listdir(docs_dir):
    if os.path.isfile(os.path.join(docs_dir, filename)) and filename.startswith('encrypted_'):
        with open(os.path.join(docs_dir, filename), 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
            decrypted_data = fernet.decrypt(encrypted_data)

        # Delete the encrypted file
        os.remove(os.path.join(docs_dir, filename))

        # Rename and write the decrypted data to the original file
        original_filename = filename.replace('encrypted_', '')
        with open(os.path.join(docs_dir, original_filename), 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)

print("Files decrypted successfully.")