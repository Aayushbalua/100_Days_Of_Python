print("Welcome to the Aayush tressure island")

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
print("This Game Is start at forest edge")
start = input('Which direction You Want to go "left" or "right"').lower()

if start=="left":
    print("Hello I am Mr.Owl")

    owl = input('Type "follow " if you want to follow the owl or type "ignore" if you want to ignore').lower()
    if owl == "follow":
        print("There is Glowing Cave")
        cave = input('"Do You Want to enter in the Cave "yes" or "no" :').lower()

        if cave == "yes":
            print("You Died Man Game Over")

        elif cave =="no":
            print("Good Decision You save your Life")

        else:
            print("You type the wrong thing")

    elif owl == "ignore":
        print("There is Hidden Path")

        path = input('Type "t" to take path or If you want to Go Back type "b" :').lower()

        if path=="b":
            print("You Lost Forever Game Over")

        elif path =="t":
            print("There is Sparkling Lake")

            lake = input('Do You want to raft or take boat type "r" for raft or "b" for Boat').lower()

            if lake =="b":
                print("there is Storm Game Over")

            elif lake =="r":
                print("there is Tower on Lake:")
                tower = input('Which Door You want to enter "red" , "blue" or "yellow": ').lower()
                if  tower== "red":
                    print("Your Body Caught Fire Game Over")
                elif tower == "blue":
                    print("Ice spikes Damge Your whole Body Game Over")

                elif tower =="yellow":
                    print("There is Crystal Light You won")

                else:
                    print("You type the wrong thing")
                    

elif start=="right":
    print("There is Bridge with troll")

    riddle = input('If You want to answer the riddle type "a" , if You want to refuse type "r":')
    if riddle =="r":
        print("You are thrown into river Correct")

    elif riddle == "a":
        print("Riddle is correct")
        lake = input('Do You want to raft or take boat type "r" for raft or "b" for Boat').lower()

        if lake =="b":
                print("there is Storm Game Over")

        elif lake =="r":
                print("there is Tower on Lake:")
                tower = input('Which Door You want to enter "red" , "blue" or "yellow": ').lower()
                if  tower== "red":
                    print("Your Body Caught Fire Game Over")
                elif tower == "blue":
                    print("Ice spikes Damge Your whole Body Game Over")

                elif tower =="yellow":
                    print("There is Crystal Light You won")

                else:
                    print("You type the wrong thing")


else:
    print("You type the wrong thing:")





            



        


    



