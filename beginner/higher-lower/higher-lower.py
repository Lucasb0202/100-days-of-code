import art
import game_data
import os
import random

clear = lambda: os.system("cls")
score = 0

def get_account(data):
  return random.choice(data)

def get_answer(account_a, account_b):
  if account_a['follower_count'] > account_b['follower_count']:
    return 'A'
  else: return 'B'

account_a = get_account(game_data.data)
account_b = get_account(game_data.data)
correct_answer = get_answer(account_a, account_b)
print(art.logo)
print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
print(art.vs)
print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")
choice = input("Who has more followers? Type 'A' or 'B': ")

while True:
  if choice.upper() == correct_answer:
    clear()
    score += 1
    account_a = account_b
    account_b = get_account(game_data.data)
    print(art.logo)
    print(f"You're right! Current score: {score}.")
    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
    print(art.vs)
    print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")
    correct_answer = get_answer(account_a, account_b)
    
    choice = input("Who has more followers? Type 'A' or 'B': ")
  else:
    print(f"Sorry, that's wrong. Final score: {score}.")
    break