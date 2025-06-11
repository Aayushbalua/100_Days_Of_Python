print("Welcome to the Aayush Park")

height = float(input("Please Enter Your Height: "))
age = int(input("Please Enter Your Age please: "))
if height>=120:
    print("You Can Ride the Roller Coaster")
    if age<12:
        print("Your Fare is $5")
    elif age>=18:
        print("Your Fare is $7")

    else:
        print("Your fare is 12$")

else:
    print("You Can't Ride")