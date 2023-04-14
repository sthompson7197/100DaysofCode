rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

options = [rock, paper, scissors]

human_choice = int(input('What do you choose? Type "O" for Rock, "1" for Paper or "2" for Scissors.'))

computer_choice = random.randint(0, 2)


print(options[human_choice])
print("Computer chose:")
print(options[computer_choice])

if human_choice == computer_choice:
    print("Tie")
elif human_choice == 0 and computer_choice == 1:
    print("You lose")
elif human_choice == 0 and computer_choice == 2:
    print("You win")
elif human_choice == 1 and computer_choice == 0:
    print("You win")
elif human_choice == 1 and computer_choice == 2:
    print("You lose")
elif human_choice == 2 and computer_choice == 0:
    print("You lose")
elif human_choice == 2 and computer_choice == 1:
    print("You win")
else:
    print("You have entered an invalid number. Please try again.")
