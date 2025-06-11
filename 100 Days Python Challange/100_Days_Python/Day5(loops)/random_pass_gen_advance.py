#Welcome In this Session We are Going to genrate the Random password not in sequence but different
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1' ,'2' ,'3' ,'4', '5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*',')','(']

print("Welcome to Python Password Genrator")

number_in = int(input("How many Numbers Do You Want in Your Password?\n"))
letter_in = int(input("How many Letters Do You want in your password\n"))
symbol_in = int(input("How many Symbols Do You want in your password\n"))

pass_list = []

for char in range(0, number_in):
    pass_list.append(random.choice(numbers))

for char in range(0,letter_in):
    pass_list.append(random.choice(letters))

for char in range(0 , symbol_in):
    pass_list.append(random.choice(symbols))

print(pass_list)

random.shuffle(pass_list)

print(pass_list)

password = ""
for char in pass_list:
    password+=char
print(f"Your Password is:- {password}")