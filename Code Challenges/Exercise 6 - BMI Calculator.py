#INSTRUCTIONS:Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new_height = float(height)
new_weight = float(weight)

bmi = (new_weight / new_height ** 2)
print(int(bmi))