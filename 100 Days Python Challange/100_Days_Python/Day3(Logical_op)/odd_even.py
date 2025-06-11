'''
In this Program I am going to create a program that can check either the number is odd or even'''

a = int(input("Enter the number to check it is odd or even="))
b= a%2
if b==0:
    print(f"{b}  is Even")

else:
    print(f"{b} is odd")
