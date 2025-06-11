'''Welcome to the Little program of Bill Claculator'''
print("Welcome to the Tip Calculator")
bill = float(input("What was Your Bill= $"))
tip = float(input("What percentage of Tip You want to give ? 10,15 or 20? = "))
people = int(input("How many people with You want to split the Bill?"))

bill_am = tip/100*bill+bill
c = bill_am/people
c1 = round(c ,2)
print(f"Your Bill after spliying with people is {c1}")
