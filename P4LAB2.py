keep_going = 'yes'
total = 0
while keep_going.lower() == 'yes' :
    num = int(input("Enter a number: "))
    total += num
    #total = total + mum
    keep_going = input("Do you want to enter more numbers? Enter yes or no: ")
print(total)