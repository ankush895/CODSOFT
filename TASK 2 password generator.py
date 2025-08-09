import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters for good security."

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + symbols

    # Ensure password includes at least one of each type for strength
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols),5
    ]

    # Fill the rest with random characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle to avoid predictable pattern
    random.shuffle(password)

    return ''.join(password)

# User Input
try:
    user_length = int(input("Enter the desired password length: "))
    result = generate_password(user_length)
    print("Generated Password:", result)
except ValueError:
    print("Please enter a valid number.")
