import random
import string
length = int(input("Enter the length of the password: "))
if length < 3:
    print("Password length should be at least 3 characters.")
else:
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

all_characters = letters + digits + symbols
for i in range(length - 3):
       password.append(random.choice(all_characters))
       random.shuffle(password)
       final_password = ''.join(password)
       print("Generated password:", final_password)