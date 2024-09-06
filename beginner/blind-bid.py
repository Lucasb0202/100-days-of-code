bidders = {}

while (True):
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))

  bidders.update({name: bid})

  decision = input("Are there any other bidders? (y/n): ")

  if decision == 'n':
    break
  else: print("\n" * 100)
print(f"The winner is {max(bidders, key = bidders.get)} with a bid of ${max(bidders.values())}")
