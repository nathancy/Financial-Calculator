# Script to generate salt and hashed password for the admin user

import hashlib, random

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" 
new_password = input("Enter new password: ")

# Generate salt
salt = ''.join(random.choice(ALPHABET) for i in range(16))
print(salt)

# Generate hashed_password using SHA512
hashed_password = hashlib.sha512(str(new_password + salt).encode('utf-8')).hexdigest()
print(hashed_password)
