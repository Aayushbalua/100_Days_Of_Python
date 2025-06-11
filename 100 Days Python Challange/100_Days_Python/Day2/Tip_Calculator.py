'''In this session I am Going to build Tip Calculator Let's Go baby
'''
print("Welcome To the Tip calculator")
bill = float(input("What was Your Bill?"))
tip = float(input("How much tip Would You Like to give? 10,12 , or 15?"))

split =int(input("How many people among You split the Bill="))
c = bill+tip
final_Bill = c/split
print(round(final_Bill , 2 ))


