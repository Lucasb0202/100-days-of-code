import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty.lower() == "easy":
  attempts = 10
elif difficulty.lower() == "hard":
  attempts = 5
else: print("Choose an available difficulty option") 

number = random.randint(1, 100)
i = attempts
while i > 0:
  print(f"You have {i} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if guess > number:
    print("Too high.")
  elif guess < number:
    print("Too low.")
  else: 
    print("You guessed the number!") 
    break
  i -= 1

if i == 0:
  print("You ran out of attempts!")
  print(f"The correct number was {number}")



