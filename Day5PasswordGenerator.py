import random
import string
from random import shuffle

print("Welcome to the PyPassword Generator!")

number_of_letters = int(input("How many letters would you like in your password? "))
number_of_symbols = int(input("How many symbols would you like? "))
number_of_numbers = int(input("How many numbers would you like? "))

#create list of symbols
list_of_symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

letters = []
symbols = []
numbers = []

#create for loop to add required number of letters/symbols/numbers to list
for i in range(0,number_of_letters):
    letters += (random.choices(string.ascii_letters))

for i in range(0,number_of_symbols):
    symbols += (random.choices(list_of_symbols))

for i in range(0,number_of_numbers):
    numbers += (random.choices(string.digits))

#concatenate list
password = letters + symbols + numbers

shuffle(password)

#convert list to string
password_as_string = "".join(password)

print(f"Here is your password: {password_as_string}")

