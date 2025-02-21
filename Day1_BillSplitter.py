print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? Rs")
total_tip = input("How much tip would you like to give? 10, 12, 15?")
total_people = input("How many people to split the bill?")

payment_per_person = (total_bill + total_tip)/total_people
print(f"Each person should pay: Rs{payment_per_person}")

