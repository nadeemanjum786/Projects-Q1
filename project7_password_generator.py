import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Get user input for number of passwords and length
try:
    num_passwords = int(input("Enter the number of passwords to generate: "))
    length = int(input("Enter the length of each password: "))

    print("\n Generated Passwords:")
    for i in range(num_passwords):
        print(f"{i+1}: {generate_password(length)}")

except ValueError:
    print(" Please enter a valid number!")
