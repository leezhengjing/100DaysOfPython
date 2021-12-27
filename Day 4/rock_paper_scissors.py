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

#Write your code below this line 👇
import random
player_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_move = random.randint(0, 2)
if player_move == 0:
  print(rock)
  if computer_move == 0:
    print(f"Computer chose:\n{rock}")
    print("It's a draw!")
  elif computer_move == 1:
    print(f"Computer chose:\n{paper}")
    print("You lose!")
  else:
    print(f"Computer chose:\n{scissors}")
    print("You win!")
elif player_move == 1:
  print(paper)
  if computer_move == 0:
    print(f"Computer chose:\n{rock}")
    print("You win!")
  elif computer_move == 1:
    print(f"Computer chose:\n{paper}")
    print("Its a draw!")
  else:
    print(f"Computer chose:\n{scissors}")
    print("You lose!")
else:
  print(scissors)
  if computer_move == 0:
    print(f"Computer chose:\n{rock}")
    print("You lose!")
  elif computer_move == 1:
    print(f"Computer chose:\n{paper}")
    print("You win!")
  else:
    print(f"Computer chose:\n{scissors}")
    print("Its a draw!")
