import random
# Rock, Paper, Scissors vs Computer


# Get inputs

human_choice = int(input("Type 0 for 'Rock', 1 for 'Paper', or 2 for 'Scissors'\n"))

computer_choice = random.randint (0, 2)
print(f"Computer chose {computer_choice}")

# Winner / Loser

if human_choice >= 3 or human_choice < 0:
    print("You typed an invalid number. You lose!")
elif human_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and human_choice == 2:
    print("You lose!")
elif computer_choice > human_choice:
    print("You lose!")
elif human_choice > computer_choice:
    print("You win!")
elif computer_choice == human_choice:
    print("Draw!")
elif human_choice >= 3 or human_choice < 0:
    print("You typed an invalid number. You lose!")