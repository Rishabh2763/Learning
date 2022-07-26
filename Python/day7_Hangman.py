import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word=random.choice(word_list)
word_length = len(chosen_word)
lives=6
print(f"the choose word is {chosen_word}")
display=[]


for i in range(word_length):
  display.append("_")
print(display)
end_of_game=False


while not end_of_game:
  
  guess=input("Guess a letter").lower()


  for position in range(word_length):
    # print(f"Current position: {position}\n Current letter: {chosen_word[position]}\n Guessed Letter: {guess}")
    if chosen_word[position]==guess:
      display[position]=guess 
  print(display)  
  if guess not in chosen_word:
    lives=lives-1
    if lives==0:
      end_of_game=True
      print("You lose")
  if "_" not in display:
    end_of_game=True
    print("You win")

  

  print(stages[lives])
