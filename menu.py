choice = 'y'
while (choice.lower() == 'y'):
    #print menu

    print("\nMenu")
    print("1. Program 1")
    print("2. Program 2")
    print("3. Program 3")
    print("4. Exit the Program\n")
    #choice = input("Do you want to run the program again? Enter y/n: ") 
    value = int(input("Please enter your choice: "))
    #get choice
    if value == 1:
        print("You picked option")
        print()
    elif value == 2:
        print("You picked option 2")
        print()
    elif value == 3: 
       print("You picked option 4")
       print()
    elif value == 4:
        print("You picked option 4")
        print("Exiting the program")
        print("Goodbye")
        print()
        choice = 'n'
    else:
        print("Invalid choice. Please cjoose a valid option")
        input("Press any key to continue")

    #print("Exiting the program!")