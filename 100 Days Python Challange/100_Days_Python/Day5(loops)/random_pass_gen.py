import random 
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1' ,'2' ,'3' ,'4', '5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*',')','(']

print("Welcome to Python Password Genrator")

letter_number = int(input("How many letters Do You want\n"))
symbol_number = int(input("How many symbols do You want?\n"))
number_num = int(input("How many Number Do You want?\n"))
#Easy Level
password = ""
for char in range(1, letter_number+1):
    password += random.choice(letters)

for char in range(1, symbol_number+1):
    password +=random.choice(symbols)

for char in range(1, number_num+1):
    password += random.choice(numbers)

print(f"Your Password is: {password}")

