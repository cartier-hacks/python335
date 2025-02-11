# Tip Calculator
print("Welcome to the tip calculator!")

# Get Inputs
total = float(input("What was the total bill?\n$"))
percentage = float(input("How much of a tip would you like to give? 15, 20, 25?\n"))
split = int(input("How many people are you splitting the bill with?\n"))

# Calculate Tip and Payment
tip = total * (percentage / 100)
total_bill = total + tip

# Calculate the payment per person
payment = round(total_bill / split ,2)

# Result
print(f"Each person should pay: ${payment:.2f}")