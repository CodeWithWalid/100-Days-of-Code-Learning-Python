#Tip Calculator
print("Welcome to the tip calculator.\n")
bill = input("Enter your bill\n")
tip = input("How much percentage are you willing to tip??\n")
split = input("How many people are you going to split the bill with?\n")

bill = float(bill)
tip = float(bill) / 100
split = int(split)

final_bill = (bill + tip) / split

print(f"\n\nEach person should pay {final_bill}")
