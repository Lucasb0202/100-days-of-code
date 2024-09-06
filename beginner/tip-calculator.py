print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

total_with_tip = tip / 100 * bill + bill
payment_for_each_person = total_with_tip / num_people

print(f"Each person should pay: ${round(payment_for_each_person, 2)}")