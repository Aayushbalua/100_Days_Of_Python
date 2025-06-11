'''In this Session I am Going to create the Fizz Buzz Like if Number is divisible by 3 It will print Fizz if Number is Divisible by 5 it will print Buzz If Number is divisible by Both then It'llprint Fizz Buzz else Number '''

for number in range(1,101):
    if number % 3 ==0 and number %5 == 0:
        print("Fizz Buzz")
    elif number % 3==0:
        print("Fizz")
    elif number%5 ==0:
        print("Buzz")

    else:
        print(number)