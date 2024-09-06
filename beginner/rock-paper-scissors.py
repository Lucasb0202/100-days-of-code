import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

moves = [rock, paper, scissors]

user_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_move = moves.index(random.choice(moves))

if (user_move == computer_move):
  print("Your move:")
  print(moves[user_move])
  print("Computer move:")
  print(moves[computer_move])
  print("Draw.") 
elif (computer_move == 0 and user_move == 2):
  print("Your move:")
  print(moves[user_move])
  print("Computer move:")
  print(moves[computer_move])
  print("You lost.") 
elif (user_move == 0 and computer_move == 2):
  print("Your move:")
  print(moves[user_move])
  print("Computer move:")
  print(moves[computer_move])
  print("You win!") 
elif (computer_move > user_move):
  print("Your move:")
  print(moves[user_move])
  print("Computer move:")
  print(moves[computer_move])
  print("You lost.") 
elif (user_move > computer_move):
  print("Your move:")
  print(moves[user_move])
  print("Computer move:")
  print(moves[computer_move])
  print("You win!") 