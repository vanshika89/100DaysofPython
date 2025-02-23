import random
import string

letters = list(string.ascii_lowercase)
symbols = list(string.punctuation)
numbers = list(range(0, 101))

print("Welcome to the PyPassword Generator!")
letter_input = int(input("How many letters would you like in your password?\n"))
symbol_input = int(input("How many symbol would you like in your password?\n"))
number_input = int(input("How many number would you like in your password?\n"))

password = []

for char in range(0, letter_input):
    password.append(str(random.choice(letters)))

for sym in range(0, symbol_input):
    password.append(str(random.choice(symbols)))

for num in range(0, number_input):
    password.append(str(random.choice(numbers)))

print(password)
random.shuffle(password)
print(password)
print('Your password is: ', ''.join(password))