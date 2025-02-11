# This is a silent auction program using dictionaries
import os

# Function to find the highest bidder option 1

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    print(f"The winner is {winner} with a bid of ${highest_bid}!")

# Find the highest bidder option 2

def find_highest_bidder2(bidding_dictionary):
    winner = max(bidding_dictionary, key = bidding_dictionary.get)
    highest_bid = bidding_dictionary[winner]
    print(f"The winner is {winner} with a bid of ${highest_bid}!")

# Set other_bidders to true to initiate while loop

bids = {}
clear_commands = {
    "nt": "cls",
    "posix": "clear"
}

other_bidders = True

while other_bidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bidders == "no":
        other_bidders = False
        find_highest_bidder2(bids)
    elif other_bidders == "yes":
        os.system(clear_commands[os.name])