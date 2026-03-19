import secrets
import string

print("\n=== Secure Password Generator v1.2 ===\n")

# Get password length from user
while True:
    try:
        length = int(input("Enter password length (8-20): "))
        if 8 <= length <= 20:
            break
        print("Please enter a number between 8 and 20.")
    except ValueError:
        print("Please enter a valid number.")

# Ask user for character types
print("\nChoose character types:")
print("1. Letters only")
print("2. Numbers only")
print("3. Letters + Numbers")
print("4. Letters + Numbers + Symbols")

while True:
    choice = input("\nEnter your choice (1-4): ")
    if choice in ["1", "2", "3", "4"]:
        break
    print("Please choose 1, 2, 3, or 4.")

# Build character pool based on choice
if choice == "1":
    character_pool = string.ascii_letters
elif choice == "2":
    character_pool = string.digits
elif choice == "3":
    character_pool = string.ascii_letters + string.digits
else:  # choice 4
    character_pool = string.ascii_letters + string.digits + string.punctuation

# Generate the first password
password = ''.join(secrets.choice(character_pool) for _ in range(length))

# Main loop for generate / regenerate
while True:
    print(f"\nYour generated password:  {password}")
    print(f"Length:                   {length} characters")
    
    regenerate = input("\nGenerate another password? (y/n): ").lower()
    if regenerate != "y":
        break
    
    # Regenerate
    password = ''.join(secrets.choice(character_pool) for _ in range(length))

print("\nThank you for using Secure Password Generator!")
print("⚠️  Remember: Never reuse passwords for important accounts.")
print("   Consider using a password manager.\n")
