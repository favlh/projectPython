import string
import random

# Step 1: Ask for password length
length = int(input("Enter password length: "))

# Step 2: Show character type options
print("""Choose character types to include in your password:
        1. Digits (0–9)
        2. Letters (a–z, A–Z)
        3. Special Characters (!@#$...)

Enter your choices separated by spaces (e.g. 1 2 3): """)

# Step 3: Get multiple choices from user
choices = input("Your choices: ").split()

# Step 4: Build character list based on selection
character_list = ""

for choice in choices:
    if choice == '1':
        character_list += string.digits
    elif choice == '2':
        character_list += string.ascii_letters
    elif choice == '3':
        character_list += string.punctuation
    else:
        print(f"'{choice}' is not a valid option.")

# Step 5: Validate selection
if not character_list:
    print("No valid character types selected. Exiting.")
else:
    # Step 6: Generate password
    password = [random.choice(character_list) for _ in range(length)]
    print("\nYour generated password is:", ''.join(password))

