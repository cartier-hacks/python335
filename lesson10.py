# This is a calculator program using functions and dictionaries

# Adding import so console can clear after user starts a new calculation

import os

# Calculator ASCII art

art = """
 _____________________
|  _________________  |
| | CH           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
 """

# Define operator functions

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
   return n1 - n2

def multiply(n1, n2):
   return n1 * n2

def divide(n1, n2):
   return n1 / n2

# Dictionary for operations and console clearing

operations = {
   "+": add,
   "-": subtract,
   "*": multiply,
   "/": divide
}

clear_commands = {
    "nt": "cls",
    "posix": "clear"
}

# While loop to continue or not
def calculator():
    print(art)
    continue_calc = True
    n1 = float(input("What is the first number?: "))

    while continue_calc:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Choose an operation: ")
        n2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")

        choice = input(f"Type y to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

        if choice == "y":
            n1 = answer
    
        else:
            continue_calc = False
            os.system(clear_commands[os.name])
            calculator()
   
calculator()
