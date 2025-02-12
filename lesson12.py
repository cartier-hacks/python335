# Number Guessing Game
from random import randint
art = """
▗▖ ▗▖▗▖ ▗▖ ▗▄▖▗▄▄▄▖▗▄▄▖    ▗▄▄▄▖▗▖ ▗▖▗▄▄▄▖    ▗▖  ▗▖▗▖ ▗▖▗▖  ▗▖▗▄▄▖ ▗▄▄▄▖▗▄▄▖ 
▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌ █ ▐▌         █  ▐▌ ▐▌▐▌       ▐▛▚▖▐▌▐▌ ▐▌▐▛▚▞▜▌▐▌ ▐▌▐▌   ▐▌ ▐▌
▐▌ ▐▌▐▛▀▜▌▐▛▀▜▌ █  ▝▀▚▖      █  ▐▛▀▜▌▐▛▀▀▘    ▐▌ ▝▜▌▐▌ ▐▌▐▌  ▐▌▐▛▀▚▖▐▛▀▀▘▐▛▀▚▖
▐▙█▟▌▐▌ ▐▌▐▌ ▐▌ █ ▗▄▄▞▘      █  ▐▌ ▐▌▐▙▄▄▖    ▐▌  ▐▌▝▚▄▞▘▐▌  ▐▌▐▙▄▞▘▐▙▄▄▖▐▌ ▐▌
                                                                                                                                                            
"""
print(art)

# Global variables

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user guess

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high. Guess again.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low. Guess again.")
        return turns -1
    else:
        print(f"You correctly guessed: {actual_answer}, YOU WIN!")

# Function to set difficulty for attempts

def set_difficulty():
     level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
     if level == "easy":
          return EASY_LEVEL_TURNS
     else:
          return HARD_LEVEL_TURNS
         
def game():
    # Choosing random number between 1 and 100

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)  
    print(answer)

    # Choosing difficulty

    turns = set_difficulty()

    # Guess from user
    game_over = False

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            game_over = True
            print(f"You have ran out of attempts. YOU LOSE! The number was {answer}!")
            return

game()