keep_going = 'yes'

while keep_going.lower() == 'yes' :
    num = int(input("Enter an integer: "))
    while num < 0 or num > 12:
        print("Invalid Entry!")
        print("Integer must be greater than or equal tp 0 and less than 13")
        num = int(input("Enter an integer: "))
        
    print("\n")
    if (num >= 0):
        for i in range (1,12+1):
         
            print(f'{num} * {i} = {num * i}')
        print('\n')
    else:
        print("This prpgram does not handle negative values.")
        print("\n")
    keep_going = input("Do you want to enter more numbers? Enter yes or no: ")
print('\n')
print("Exiting the program...")
