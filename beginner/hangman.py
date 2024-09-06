import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

random_word = random.choice(word_list)
random_word_list = [char for char in random_word]
  
lives = 6
letters_guessed = ["_"] * len(random_word_list)

hangman_index = 0

while lives > 0:
  word = ""
  word = ''.join(letters_guessed)

  if letters_guessed == random_word_list:
    print("You won! The word was " + word + ".")
    break

  print(HANGMANPICS[hangman_index])
  print("Word to guess: " + word)

  letter = input("Guess a letter: ")
  if letter in random_word:
    print("\nCorrect!")
    print (f"LIVES REMAINING: {lives} / 6\n")
  else: 
    print("\nWrong. You lost a life.")
    lives -= 1
    hangman_index += 1
    print (f"LIVES REMAINING: {lives} / 6\n")

  for i in range(len(random_word)): 
    if letter == random_word_list[i]:
      letters_guessed[i] = letter
if lives <= 0:
  print(HANGMANPICS[hangman_index])
  print("You lost! The word was " + random_word)
  





