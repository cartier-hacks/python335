import random
import os

# Art for terminal

art = """
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                                  
"""

# List for possibilites on the deal

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(art)

# Function for clearing console to play again

clear_commands = {
    "nt": "cls",
    "posix": "clear"
}

# Function to deal cards

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Function to calculate cards dealt

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# Function to compare winner/loser/push

def compare(user_score, dealer_score):
    if dealer_score == user_score:
        return "Player Push!"
    elif dealer_score == 0:
        return "Dealer has Blackjack, You lose!"
    elif user_score == 0:
        return "Player BlackJack, You win!"
    elif user_score > 21:
        return "Player bust! You lose!"
    elif dealer_score > 21:
        return "Dealer Bust! Player wins!"
    elif user_score > dealer_score:
        return "Player wins!"
    else:
        return "Dealer wins!"

def play_game():
    print(art)
    user_cards = []
    dealer_cards = []
    is_game_over = False

    # For loop to add cards

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    # Adding variables for score of dealer and player using calculation function and use while loop

    while not is_game_over:

        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

    # Printing current cards

        print(f"Player cards: {user_cards}, current score: {user_score}")
        print(f"Dealer shows: {dealer_cards[0]}")


        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            hit_or_stay = input("Type 'y' to hit for another card, type 'n' to stay: ")
            if hit_or_stay == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    # While loop for dealer to hit or not

    while dealer_score !=0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
    
    # Printing scores and comparing scores

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(user_score, dealer_score))

# Asking user if they want to play again and clearing console

while input("Do you want to play BlackJack? Type 'y' or 'n': ").lower() == "y":
    os.system(clear_commands[os.name])
    play_game()
else:
    print("Thank you for playing!")