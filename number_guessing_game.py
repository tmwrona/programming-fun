import random

NUM = random.randint(1,100)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else:
    print("That is not a proper difficulty level.")

print(f"You have {attempts} attempts.")

while attempts > 0:
    guess = int(input("Make a guess: "))
    if guess == NUM:
        print("That is correct! You've won the guessing game.")
        exit()
    elif guess > NUM:
        attempts -= 1
        print("Too high.")
    else:
        attempts -= 1
        print("Too low.")

    print(f"You have {attempts} attempts left.")

print("I'm sorry, you have no more attempts. You've lost the game.")