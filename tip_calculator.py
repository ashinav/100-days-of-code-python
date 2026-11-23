
print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
no_people_split = int(input("How many people to split the bill? "))

tip_amount = total_bill * tip / 100
total_amount = total_bill + tip_amount
each_person = total_amount / no_people_split

print(f"Each person should pay: {each_person:.2f}")
