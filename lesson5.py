# Random Password Generator
import random

letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Inputs from user

characters = int(input("How many characters would you like in your password?\n "))
symbols = int(input("How many symbols would you like?\n "))
numbers = int(input("How many numbers would you like?\n "))

# Randomization Level 1 (not fully random)

# password = ""

# for char in range(0, characters):
#    password += random.choice(letters_list)

# for char in range(0, symbols):
#    password += random.choice(symbols_list)

# for char in range(0, numbers):
#    password += random.choice(numbers_list)


# print(f"Your password is: {password}")

# Level 2, fully random

password_list= []
password = ""

for char in range(0, characters):
    password_list.append(random.choice(letters_list))

for char in range(0, symbols):
    password_list.append(random.choice(symbols_list))

for char in range(0, numbers):
    password_list.append(random.choice(numbers_list))

random.shuffle(password_list)

for char in password_list:
    password += char


print(f"Your password is: {password}")
