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
print("Do you want ot go left or right??\n")
direction = input("Type 'left' or 'right'\n")
if direction == "left":
          print("Ther is a lake in front of you. Do you want to swim or wait for a boat??\n")
          lake = input("Type 'swim' or 'wait'\n")
          if lake == "wait":
                    print("You have arrived at a house with 3 doors red, blue and yellow. which one do you choose??\n")
                    door = input("Type 'red', 'blue' or 'yellow'\n")
                    if door == "red":
                              print("You have been burned by fire. Game Over.")
                    elif door ==  "blue":
                              print("You have been eaten by beasts. Game Over.")
                    elif door == "yellow":
                              print("Congratulations!! You win!!")
                    else:
                              print("Game Over.")
          else:
                    print("Attacked by trout by trout Game Over.")          
else:
          print("Fall into a hole. Game Over.")



