import random
rock = '''
 _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) '''

paper ='''
  _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________) '''

scissor = '''
 _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

game = [rock , paper , scissor]

user_choice = int(input("Type 0 for Rock 1 for Paper or 2 for Scissor"))
print(game[user_choice])

computer_choice = random.randint(0,2)
print(game[computer_choice])

if user_choice==0 and computer_choice==1:
    print("You Loose Baby")

elif user_choice==0 and computer_choice==2:
    print("You Win")

elif user_choice==computer_choice:
    print("Match Draw")

elif user_choice==1 and computer_choice==0:
    print("You Win")
elif user_choice==1 and computer_choice==2:
    print("You Loose")

elif user_choice==2 and computer_choice==0:
    print("You Loose")
elif user_choice==2 and computer_choice==1:
    print("You Win")
else:
    print("You Type the Invalid number")