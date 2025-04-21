import string
import random

length = int(input("Enter password length: "))

print("""Choose character set from this list:
        1. Digits
        2. Letters
        3. Special Characters
        4. Done selecting character types""")

characterList = ""

while True:
    choice = int(input("Pick a number: "))
    if choice == 1:
        characterList += string.digits
        print("✔ Digits added.")
    elif choice == 2:
        characterList += string.ascii_letters
        print("✔ Letters added.")
    elif choice == 3:
        characterList += string.punctuation
        print("✔ Special characters added.")
    elif choice == 4:
        if characterList == "":
            print("❌ You haven't selected any character types yet!")
        else:
            break
    else:
        print("Please pick a valid option!")

password = []

for i in range(length):
    randomchar = random.choice(characterList)
    password.append(randomchar)

print(f"\n🔐 The random password is: {''.join(password)}")

