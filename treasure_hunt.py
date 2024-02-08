""" 
This code is the treasure hunt challenge from the Udemy course 100 Days of Code: The Complete Python Pro Bootcamp Day 3.
It's an interactive program that takes user input and determines your fate on whether you find the treasure or fail!
"""

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

direction = input("Would you like to go left or right? ").lower()

if direction == "left":
    print("You made it to the lake!")
    lake_choice = input("Would you like to swim or wait? ").lower()
    if lake_choice == "wait":
        print("Congrats! You've made it to the island!")
        door_choice = input(
            "There are three doors. Which one do you choose? Red, yellow, or blue? "
        ).lower()
        if door_choice == "yellow":
            print("You win!")
        elif door_choice == "red":
            print("You've been burned by fire. Game over.")
        elif door_choice == "blue":
            print("You've been eaten by beasts. Game over.")
        else:
            print("Game over.")
    else:
        print("You've been attacked by a trout. Game over.")
else:
    print("You've fallen into a hole. Game over.")

exit()
