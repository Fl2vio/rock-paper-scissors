import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock,paper,scissors]
player = int(input("choose 0 for rock 1 for paper 2 for scissors: "))
#player choice
print(choices[player])

#computer choice
print("computer choice:")
computer_choice = random.randint(0,2)
print(choices[computer_choice])

if player == computer_choice:
    print("its a draw")
elif player == 0 and computer_choice == 2:
    print("you win!")
elif player == 1 and computer_choice == 0:
    print("you win!")
elif player == 2 and computer_choice == 1:
    print("you win")
else:
    print("you lose")
