import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

title = """
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\.
                       _/ |                
                      |__/                                                                                          
"""
print(title)

def play_blackjack():
  dealers_cards = []
  players_cards = []
  i = 0

  while i < 2:
    players_cards.append(random.choice(cards))
    dealers_cards.append(random.choice(cards))
    i += 1
  print(f"Dealers cards: [*, {dealers_cards[1]}]")
  print(f"Your cards: {players_cards} = {sum(players_cards)}")
  while True:
    choice = input("Hit or Stand?: ")
    if choice.lower() == "hit":
      card = random.choice(cards)
      players_cards.append(card)
      if card == 11 and sum(players_cards) > 21:
        players_cards.pop(len(players_cards) - 1)
        players_cards.append(1)
      if sum(players_cards) > 21:
        print(f"Your cards: {players_cards} = {sum(players_cards)}")
        print("You lost!")
        continue_playing = input("Do you want to continue playing? (y/n): ")
        if continue_playing == "y":
          play_blackjack()
        exit()
      elif sum(players_cards) == 21:
        print(f"Your cards: {players_cards} = {sum(players_cards)}")
        print("Blackjack! You won.")
        continue_playing = input("Do you want to continue playing? (y/n): ")
        if continue_playing == "y":
          play_blackjack()
        exit()
      else: 
        print(f"Your cards: {players_cards} = {sum(players_cards)}")
    elif choice.lower() == "stand":
      print(f"Your final cards: {players_cards} = {sum(players_cards)}")  
      break

  while True:
    if sum(dealers_cards) <= 17:
      card = random.choice(cards)
      dealers_cards.append(card)
      if card == 11 and sum(dealers_cards) > 21:
        dealers_cards.pop(len(dealers_cards) - 1)
        dealers_cards.append(1)
      print(f"Dealers cards: {dealers_cards} = {sum(dealers_cards)}")
    else:
      print(f"Dealers cards: {dealers_cards} = {sum(dealers_cards)}")
      if sum(dealers_cards) > 21: 
        print("Bust! You won!")
        break
      elif sum(dealers_cards) == sum(players_cards):
        print("Draw!")
        break
      elif sum(dealers_cards) > sum(players_cards):
        print("Dealer won!")
        break
      else: 
        print("You won!")
        break
  continue_playing = input("Do you want to continue playing? (y/n): ")
  if continue_playing == "y":
    play_blackjack()

play_blackjack()


# Remember DRY(Don't Repeat Yourself), if you find yourself repeating code, make it a function.

# import random

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# title = """
#  _     _            _    _            _    
# | |   | |          | |  (_)          | |   
# | |__ | | __ _  ___| | ___  __ _  ___| | __
# | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
# | |_) | | (_| | (__|   <| | (_| | (__|   < 
# |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\.
#                        _/ |                
#                       |__/                                                                                          
# """
# print(title)

# def deal_card():
#     """Returns a random card from the deck."""
#     return random.choice(cards)

# def calculate_total(hand):
#     """Calculates the total value of a hand, adjusting for Aces."""
#     total = sum(hand)
#     if 11 in hand and total > 21:
#         hand[hand.index(11)] = 1  # Change Ace (11) to 1 if total exceeds 21
#         total = sum(hand)
#     return total

# def display_cards(player, dealer, reveal_dealer=False):
#     """Displays the current cards for the player and dealer."""
#     if reveal_dealer:
#         print(f"Dealer's cards: {dealer} = {sum(dealer)}")
#     else:
#         print(f"Dealer's cards: [*, {dealer[1]}]")
#     print(f"Your cards: {player} = {sum(player)}")

# def play_blackjack():
#     dealer_cards = [deal_card(), deal_card()]
#     player_cards = [deal_card(), deal_card()]

#     # Show initial hands
#     display_cards(player_cards, dealer_cards)

#     # Player's turn
#     while True:
#         choice = input("Hit or Stand?: ").lower()
#         if choice == "hit":
#             player_cards.append(deal_card())
#             player_total = calculate_total(player_cards)
#             display_cards(player_cards, dealer_cards)

#             if player_total > 21:
#                 print("You busted! Dealer wins.")
#                 break
#             elif player_total == 21:
#                 print("Blackjack! You win!")
#                 break
#         elif choice == "stand":
#             print(f"Your final cards: {player_cards} = {sum(player_cards)}")
#             break
#         else:
#             print("Invalid choice! Please enter 'hit' or 'stand'.")

#     # Dealer's turn (if player didn't bust)
#     if calculate_total(player_cards) <= 21:
#         while calculate_total(dealer_cards) < 17:
#             dealer_cards.append(deal_card())
        
#         display_cards(player_cards, dealer_cards, reveal_dealer=True)
#         dealer_total = calculate_total(dealer_cards)
#         player_total = calculate_total(player_cards)

#         if dealer_total > 21:
#             print("Dealer busts! You win!")
#         elif dealer_total > player_total:
#             print("Dealer wins!")
#         elif dealer_total < player_total:
#             print("You win!")
#         else:
#             print("It's a draw!")

#     # Ask to play again
#     if input("Do you want to continue playing? (y/n): ").lower() == "y":
#         play_blackjack()
#     else:
#         print("Thanks for playing!")

# play_blackjack()
