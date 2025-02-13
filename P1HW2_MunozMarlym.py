# Marlym Munoz
# 02/13/25
# P1HW2
# A program that does some basic math on numbers that are entered.

print("This program calculates and displays travel expenses\n")
budget = int(input("Enter Budget: "))
print()
location = str(input("Enter your travel destination: "))
print()
gas = int(input("How much do you think you will spend on gas? "))
print()
lodging = int(input("Approximately, how much do you think you will need for accomodation/hotel? "))
print ()
food = int(input("Last, how much do you need for food? "))
print ()

print("-"*12,"Travel Expenses","-"*12)
print("Location: ",location)
print("Initial Budget: ",budget)

print("Fuel: ",gas)
print("Accomadation: ",lodging)
print("Food: ",food)

# calculation
balance = budget - gas - lodging - food
print("Remaining Balance: ",balance)

##Ask user to enter their budget
##Ask user to enter travel destination
##Ask user for amount they will spend on gas
##Ask user for amount they will spend on accommodation
##Ask user for amount they will spend on food
##Add expenses
##Subtract expenses from budget
##Display results
