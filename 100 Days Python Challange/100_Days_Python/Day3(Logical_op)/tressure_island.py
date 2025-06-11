print("Welcome to the tressure island")

print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')


print("Your Mission is to find the tressure")

choice1 = input('You\'r at a crossroad,Where do you want to go? Type "left" or "right".').lower()

if choice1 == "left":
    choice2 = input(' have come to a lake , there is an island in the middle of the lake. Type "wait" to ' \
    '' \
    '' \
    'wait for Boat. Type "swim" to swim across : ').lower()
    if choice2 == "swim":
        print("You are attcked by trought Game Over")
    elif choice2 =="wait":

        choice3 = input('Which door You want to select :"red" , "blue" or "yellow" ?').lower()

        if choice3=="red":
            print("You are Brned By Fire Game Over")

        elif choice3=="blue":
            print("You are Eaten By Beasts. Game Over")

        elif choice3 =="yellow":
            print("You win")

        else:
            print("You type the Wrong thing")

    else:
        print("You type the wrong thing")


elif choice1 =="right":
    print("You Fell into Hole. Game Over")

    print("You type the wrong thing")

else:
    print("You type Wrong Thing")




