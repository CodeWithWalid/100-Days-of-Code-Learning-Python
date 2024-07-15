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

import random
user_choice = int(input("What do you want to choose rock = 0, paper = 1, scissor = 2???"))
computer_choice = random.randint(0,2)

if user_choice == 0:
    print("Rock")
elif user_choice == 1:
    print("Paper")
else:
    print("Scissors")

if computer_choice == 0:
    print("Rock")
elif computer_choice == 1:
    print("Paper")
else:
    print("Scissors")

if (user_choice == 0 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1) or (user_choice == 1 and computer_choice == 0):
    print("You win")
elif user_choice == computer_choice:
    print("Draw! Try Again")
else:
    print("You lose")
