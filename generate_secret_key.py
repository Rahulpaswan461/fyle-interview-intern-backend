# generate_secret_key.py
import secrets

# Generate a secure random key
secret_key = secrets.token_hex(24)  # Generates a 48-character hexadecimal key
print(secret_key)
