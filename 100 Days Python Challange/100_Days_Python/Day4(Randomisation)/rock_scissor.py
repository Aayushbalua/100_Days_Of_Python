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
game = [rock , scissor , paper]
# print(rock,paper,scissor)

user = int(input('Type "0" for Rock "1" for scissor and "2" for paper\n'))
if user>=0 and user<=2:
    print(game[user])

computer_choice = random.randint(0,2)
print("Computer choose:")
print(game[computer_choice])


if user==0 and computer_choice==2:
    print("Computer Wins")

elif user==0 and computer_choice==1:
    print("User Wins")
elif user==computer_choice:
    print("Match Draw")

elif user==1 and computer_choice==2:
    print("You Win")

elif user==1 and computer_choice==0:
    print("You Loose Computer Wins")

elif user==2 and computer_choice==0:
    print("You win")
elif user==2 and computer_choice==1:
    print("Computer Wins You Loose")

else:
    print("You type the wrong thing")