############### Blackjack Project #####################

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random

print(logo)

print("""############### Our Blackjack House Rules #####################\n
\n
## The deck is unlimited in size.\n
## There are no jokers.\n
## The Jack/Queen/King all count as 10.\n
## The the Ace can count as 11 or 1.\n
## Use the following list as the deck of cards:\n
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]\n
## The cards in the list have equal probability of being drawn.\n
## Cards are not removed from the deck as they are drawn.\n
## The computer is the dealer.""")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
  return random.choice(cards)


# Deal the user and dealer 2 cards each to start.
user_cards = []
computer_cards = []
user_cards.append(deal_card())
user_cards.append(deal_card())
computer_cards.append(deal_card())
computer_cards.append(deal_card())


# Take a List of cards as input and return the score.
# Make sure to check for blackjack and return 0 if blackjack occurred.
# If there is an Ace (11) and the score is over 21, turn the 11 into a 1.
def calculate_score(cards):
  score = sum(cards)
  if 11 in cards and 10 in cards and len(cards) == 2:
    score = 0
  elif 11 in cards and score > 21:
    while score > 21 and 11 in cards:
      cards.remove(11)
      cards.append(1)
      score = sum(cards)

  return score

# If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
cont = True
while cont == True:
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)

  if user_score == 0:
    print("Congrats! You got blackjack and win!")
    print("Your cards: ", user_cards)
    print("Dealer's cards: ", computer_cards)
    exit()
  elif computer_score == 0:
    print("I'm sorry, the house got a blackjack. You lose.")
    print("Your cards: ", user_cards)
    print("Dealer's cards: ", computer_cards)
    exit()
  elif user_score > 21:
    print("Bust! You lose.")
    print("Your cards: ", user_cards)
    print("Dealer's cards: ", computer_cards)
    exit()
  else:
    # If the game has not ended, ask the user if they want to draw another card. If yes, then add another card to the user_cards List. If no, then the game has ended.
    draw = input(f"Your current score is {user_score} Do you want to draw another card? Type 'y' or 'n': ")
    if draw == 'n':
      cont = False
    else:
      user_cards.append(deal_card())

computer_score = calculate_score(computer_cards)

while computer_score < 17:
  computer_cards.append(deal_card())
  computer_score = calculate_score(computer_cards)
  if computer_score > 21:
    print("Congrats! Dealer busted! You win!")
    print("Your cards: ", user_cards)
    print("Dealer's cards: ", computer_cards)
    

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
if user_score > computer_score:
  print("You win!")
elif user_score < computer_score:
  print("You lose! :(")
else:
  print("It's a draw :O")

print("Your cards: ", user_cards)
print("Dealer's cards: ", computer_cards)


