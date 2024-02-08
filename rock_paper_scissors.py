""" 
This is the rock, paper, scissors game. This started as a code challenge from the Udemy course 100 Days of Code: The Complete Python Pro Bootcamp Day 4.
"""

import random

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
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
if user_choice.isdigit() == False:
    print("That is not a number. Try again.")
    exit()

user_choice = int(user_choice)

computer_choice = random.randint(0,2)
images = [rock, paper, scissors]

# first check the invalid case
if user_choice > 2 or user_choice < 0:
    print("That number is not valid. Please try again.")
else:

    print(f"You chose: {images[user_choice]}")
    print(f"Computer chose: {images[computer_choice]}")

    if user_choice == computer_choice:
        print("You tied!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose.")
    elif user_choice > computer_choice:
        print("You win!")
    elif user_choice < computer_choice:
        print("You lose.")
    else:
        print("This statement should never be reached.")

    



  
