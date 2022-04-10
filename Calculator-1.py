# creating a calculator using if conditions only

condition = True

while condition is True:
    userinput =int(input("\nHello, Welcome!\n \nSelect the Operation you would like to perform: \n(1)Addition \n(2)Subtraction \n(3)Multiplication \n(4)Division \n(5)Exit \nEnter the Number only - "))
    print(userinput)
    
    if userinput == 1:
        no_one = int(input("\nEnter number 1: "))
        no_two = int(input("\nEnter number 2: "))
        add = no_one + no_two
        condition = False
        print("\nThe answer is: ", add )

    elif userinput == 2:
        no_one = int(input("\nEnter number 1: "))
        no_two = int(input("\nEnter number 2: "))
        sub = no_one - no_two
        condition = False
        print("\nThe answer is: ", sub)

    elif userinput == 3:
        no_one = int(input("\nEnter number 1: "))
        no_two = int(input("\nEnter number 2: "))
        mul = no_one * no_two
        condition = False
        print("\nThe answer is: ", mul)

    elif userinput == 4:
        no_one = int(input("\nEnter number 1: "))
        no_two = int(input("\nEnter number 2: "))
        div = no_one/no_two
        condition = False
        print("\nThe answer is: ", div)

    elif userinput == 5:
        condition = False
        print("\nClosed!")

    
    elif userinput >= 6:
        print("Error! Please retry")


    if userinput != 5:
        contd = str(input("\nDo you want to continue? (y/n) "))
        
        print(contd)
        if contd == 'y':
            condition = True
            
        elif contd == 'n':
            condition = False
            print("\nExited!")

    
    


