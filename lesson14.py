import random
import os
from data_higher_lower import data

art = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

# Clear Commands

clear_commands = {
    "nt": "cls",
    "posix": "clear"
}


# Function to format data and return in a printable format

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_description}, from {account_country}")

# Function to check the answer and tally up the score if they got it right

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
       return user_guess == "b"


score = 0
game_should_continue = True

## if user gets it right, make the correct guess move to the A position

account_b = random.choice(data)

# While loop to continue the game if correct

while game_should_continue:
    print(art)

    # Choosing random data and ensuring they are not the same
    ## if user gets it right, make the correct guess move to the A position

    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")

    print(vs)

    print(f"Against B: {format_data(account_b)}")



    # Ask user for guess

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #Clearing screen
    
    os.system(clear_commands[os.name])

    ## Get follower count

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]    
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give feedback to user
    # Replay game if the user gets it right

    if is_correct:
        score += 1
        print(f"You're Right! Current score: {score}")
    else:
        print(f"Sorry that's wrong. Final score: {score}")
        game_should_continue = False

    



