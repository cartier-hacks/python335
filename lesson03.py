# Treasure Island
print("Welcome to Treasure Island.")

print("Your mission is to find the treasure!")

# First decision
print("You're at a cross road. Where do you want to go?")
direction = input("      Type 'left' or right' ")
wait_or_swim = 0
red_yellow_blue = 0

if direction == "left":
    print("You have come to a lake. There is an island in the middle of the lake.")
    wait_or_swim = input("Type 'wait' to wait for a boat. Type 'swim' to swim across. ")

    if wait_or_swim == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        red_yellow_blue = input("One red, one yellow, one blue. Which color do you choose? ")
    
        if red_yellow_blue == "yellow":
            print("YOU WIN!")
        else:
            print("Game over!")
    else:
        print("Game over!")
else:
    print("Game over!")
