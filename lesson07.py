import random

stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
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
  |   |
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
      |
      |
      |
      |
=========''']

word_list = ["giraffe", "coffee", "computer", "camel", "table", "puree", "water", "medicine", "microphone",]
lives = 6

# Choose a random word for the list

chosen_word = random.choice(word_list)

# Setting word with underscores

placeholder = ""
correct_letters = []

for position in range(len(chosen_word)):
    placeholder += "_ "
print(placeholder)

# Ask for a guess in lowercase

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already guessed {guess}, try a different letter!")



    display = ""

# Check if guess is in the word and replace "_" with letter

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_ "

    print(display)

    
    # Reduce lives if wrong letter is chosen

    if guess not in chosen_word:
        lives -= 1
        if guess not in correct_letters:
            print(f"You guessed {guess}, thats not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"Game over! The correct word was '{chosen_word}'")

    if "_" not in display:
        game_over = True
        print("You Win!")
    
    # Update the art

    print(stages[lives])