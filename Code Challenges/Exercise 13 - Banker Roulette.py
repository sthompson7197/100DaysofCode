#INSTRUCTIONS: write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

number_of_names = len(names)

choice = random.randint(0, number_of_names - 1)

person_paying = names[choice]

print(f"{person_paying} is going to buy the meal today!")