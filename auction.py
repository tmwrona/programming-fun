from replit import clear
from art import logo
print(logo)

bids = {}
finished = False

def highest_bidder(bids):
  print("The winner is " + max(bids, key=bids.get) + "!!!")
  

while not finished:
  name = input("What is your name? ")
  price = input("What is your bid? ")
  bids[name] = price
  cont = input("Are there any other bidders? Type y or n. ")
  if cont == 'n':
    finished = True
  elif cont == 'y':
    clear()

highest_bidder(bids)
