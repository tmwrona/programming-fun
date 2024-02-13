#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for x in range(nr_letters):
    which_letter = random.randint(0, len(letters) - 1)
    password += letters[which_letter]

for y in range(nr_symbols):
    which_symbol = random.randint(0, len(symbols) - 1)
    password += symbols[which_symbol]

for z in range(nr_numbers):
    which_number = random.randint(0, len(numbers) - 1)
    password += numbers[which_number]

# randomize the order of the letters, symbols, and numbers
password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)

print(password)

