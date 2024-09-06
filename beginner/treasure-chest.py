print("Welcome to Treasure Island.\n Your mission is to find the treasure.")
decision = input("Left or right?")
if (decision.lower() == 'right'):
  print("Game Over")
  exit()
else: print("Success")

decision = input("Swim or wait?")
if (decision.lower() == 'swim'):
  print("Game Over")
  exit()
else: print("Success")

decision = input("Which door?")
if (decision.lower() != 'blue'):
  print("Game Over")
  exit()
else: print("Success")
print("You won!")


