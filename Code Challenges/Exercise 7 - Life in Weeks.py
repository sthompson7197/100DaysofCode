#INSTRUCTIONS: Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_left = 90 - int(age)

#days left
x = years_left * 365

#weeks left
y = years_left * 52

#months left
z = years_left * 12

print(f"You have {x} days, {y} weeks, and {z} months left.")

