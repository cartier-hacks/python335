MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


units = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
}

# Function to check if there is enough ingredients left in the machine

def enough_inventory(resource, amount):
    return resources[resource] >= amount

# Function to make the order

def can_make_order(order):
    ingredients = MENU[order]["ingredients"]
    for resource in ingredients:
        if not enough_inventory(resource, ingredients[resource]):
            return False
    return True

# Making the coffee and reducing coffee made from the resources

def make_coffee(drink_name):
    order_ingredients = MENU[drink_name]["ingredients"]
    for ingredients in order_ingredients:
        resources[ingredients] -= order_ingredients[ingredients]
    print(f"Here is your {drink_name}!")


# Function for coin processor and total

def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

# Function to take the order and use payment

def take_order(choice):
    change = 0.0
    global profit
    if can_make_order(choice):
        price = MENU[choice]["cost"]
        print(f"We're going to charge you {price}")
        payment = process_coins()
        if payment >= price:
            profit += price
            change = round(payment - price, 2)
            parts = str(change).split(".") 
            print(f"Here is your change of {parts[0]} dollars and {parts[1]} cents")
            make_coffee(choice)
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False
    else:
        print("Machine doesn't have enough ingredients.")

# Ask user what they would like from the menu

while True:
    choice = input("What would you like? espresso/latte/cappuccino?: ").lower()
    match choice:
        case "off":
            exit()
        case "report":
            for resource in resources:
                print(f"{resource.title()}: {resources[resource]}{units[resource]}")
            print(f"Money: ${profit}")
        case _:
            take_order(choice)