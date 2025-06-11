print("Welcome to the BMI Calculator")

weight = round(float(input("Enter Your Weight in kg: ")) , 2)
height = round(float(input("Please Enter Your Height:")) , 2)
bmi = weight/(height**2)
print(bmi)
'''
if bmi>=25:
    print("You are Over Weight")

elif bmi>=18.5:
    print("Normal Weight")

else:
    print("You are Underweight")
    '''