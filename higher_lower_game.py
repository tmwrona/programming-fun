from art import logo, vs
from game_data import data
import random

print(logo)

# boolean for ending the while loop once the game is over
correct = True

# select the first two to compare
first_choice = random.choice(data)
second_choice = random.choice(data)

# initialize the score
score = 0

# set the while loop to keep going until the player loses
while correct == True:
  
    # print options A and B to the console for the player
    print(f"Compare A: {first_choice['name']}.")
    print(vs)
    print(f"Compare B: {second_choice['name']}.")

    # ask the player to guess
    guess = input("Which account has the higher number of followers? Type 'A' or 'B': ")

    # check if the guess is correct for both cases (option A higher, option B higher)
    # if it's incorrect, tell the player they lost and end the while loop
    if first_choice['follower_count'] > second_choice['follower_count'] and guess == 'A':
        print("Correct!\n")
        score += 1
    elif first_choice['follower_count'] < second_choice['follower_count'] and guess == 'B':
        print("Correct!\n")
        score += 1
    else:
        print(f"That is incorrect. Your final score is {score}.")
        correct = False

    # make the second choice the new first choice, and pick a new second choice
    first_choice = second_choice
    second_choice = random.choice(data)

    # make sure the first choice isn't equal to the second choice, and pick again if it is.
    while first_choice == second_choice:
        second_choice = random.choice(data)
