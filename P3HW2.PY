# Marlym Munoz
# March 18 2025
# P3HW1
# Pay

name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter employee's pay rate: "))

if hours > 40: 
    reg_pay = 40 * rate
    ovt_hrs = hours - 40
    ovt_pay = ovt_hrs * rate * 1.5
    gross_pay = ovt_pay + reg_pay 
else: 
    reg_pay = hours * rate
    ovt_hrs = 0
    ovt_pay = 0
    gross_pay = ovt_pay + reg_pay 

print("\n--------------------------------")
print(f"Employee name: {name}")
print()
print(f"Hours Worked   Pay Rate    OverTime      Overtime Pay      RegHour Pay")
print("\n----------------------------------------------------------------------")
print(f"{hours:<15.1f}{rate:<15.1f}{ovt_hrs:<10.1f}{ovt_pay:<15.2f}${reg_pay:<12.2f}${gross_pay:<12.2f}")
