# Marlym Munoz
# Mar 4 2025
# P2HW2
# Grade test

mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))
gradeList = [] # empty list
gradeList = [mod1,mod2,mod3,mod4,mod5,mod6] # add variables to the list
print(gradeList)

# figure out the lowest, highest, sum and the length

lowest = min(gradeList)
highest = max(gradeList)
total = sum(gradeList)
average = total / len(gradeList)

# Print the results
print("\n ----------Results----------")
print(f'{"Lowest Grade: ":<20}{lowest}')
print(f'{"Highest Grade: ":<20}{highest}')
print(f'{"Sum of Grades: ":<20}{total}')
print(f'{"Average: ":<20}{average:.2f}')
print('-'*30)