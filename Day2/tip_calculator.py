#create a Tip calculator depending on the Bill Amount
print("Welcome to the Tip Calculator")

bill = float(input("What was the total bill? $"))

tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip_multiplier = float("1."+ tip)

bill_with_tip = bill * tip_multiplier

no_people = int(input("How many people to split the bill? "))

final_split = "{:.2f}".format(bill_with_tip/no_people)

print(f"Each person should pay: ${final_split}")