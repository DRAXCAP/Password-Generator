# password_generator.py
# v1.1 - Secure CLI Password Generator

import secrets

# === Core Engine ===

# 1. Decide password length (random between 8 and 20)
password_length = secrets.randbelow(13) + 8   # gives 8 to 20 inclusive

# 2. Create the character pool (letters + numbers)
character_pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# 3. Build the password securely
password = ''.join(secrets.choice(character_pool) for _ in range(password_length))

# === Output ===
print("\n=== Secure Password Generator ===")
print(f"\nYour generated password:  {password}")
print(f"Length:                   {password_length} characters")
print("\n⚠️  Remember: Never reuse this password for important accounts!")
print("   Consider using a password manager.\n")