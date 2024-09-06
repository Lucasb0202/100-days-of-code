#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

easy_password = ""
for i in range(0, nr_letters):
  easy_password += random.choice(letters)
for i in range(0, nr_symbols):
  easy_password += random.choice(symbols)
for i in range(0, nr_numbers):
  easy_password += random.choice(numbers)
print(easy_password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
characters = [letters, numbers, symbols]

letter_count = 0
number_count = 0
symbol_count = 0

hard_password = ""

i = 0
while i < nr_letters + nr_numbers + nr_symbols:
  character = random.choice(random.choice(characters))
  if character in letters:
    if letter_count < nr_letters:
      hard_password += character
      letter_count += 1
      i += 1
    else: continue
  elif character in symbols:
    if symbol_count < nr_symbols:
      hard_password += character
      symbol_count += 1
      i += 1
    else: continue
  else:
    if number_count < nr_numbers:
      hard_password += character
      number_count += 1
      i += 1
    else: continue
print(hard_password)