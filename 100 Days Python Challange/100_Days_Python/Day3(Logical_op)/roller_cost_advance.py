'''Welcome to The Roller coster'''
height = float(input("Please Enter Your Height:-"))
# age = int(input("Please Enter Your Age"))
bill = 0
if height>=120:
    print("You Can ride the rollercoaster")
    age = int(input("Please Enter Your Age:-"))
    if age<=12:
        bill = 5
        print("Your Ticket Fare is 5$")

    elif age<=18:
        bill =7
        print("Your ticket fare is 7$")

    elif age >=45 and age <=55:
        print("P")

    else:
        bill=12
        print("Your Fare is 12$")

    photo = str(input("Do You Want Photo? Press Y for Yes and N for No"))
    if photo=="Y":
        bill = bill+3

        print(f"Your Final Bill is {bill}")


else:
    print("You Can't ride the rollerCoatser")