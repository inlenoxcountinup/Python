# creating a calculator using if conditions and functions

# creating functions

def add (a,b):
    return a + b

def sub (a,b):
    return a - b 

def mul (a,b):
    return a * b 

def div (a,b):
    return a / b

condition = True

while condition is True:
    print("\n====================================================")
    print("\nHello, Welcome!\n \nSelect the Operation you would like to perform: \n(1)Addition \n(2)Subtraction \n(3)Multiplication \n(4)Division \n(5)Exit")
    userinput = int(input("\nEnter the Number only - "))
    print(userinput)
    print("\n====================================================")

    if userinput == 1:
        a = int(input("\nEnter Number 1: "))
        b = int(input("\nEnter Number 2: "))
        print("\nThe Answer is: ", add(a,b))
        condition = False

    elif userinput == 2:
        a = int(input("\nEnter Number 1: "))
        b = int(input("\nEnter Number 2: "))
        print("\nThe Answer is: ", sub(a,b))
        condition = False

    elif userinput == 3:
        a = int(input("\nEnter Number 1: "))
        b = int(input("\nEnter Number 2: "))
        print("\nThe Answer is: ", mul(a,b))
        condition = False

    elif userinput == 4:
        a = int(input("\nEnter Number 1: "))
        b = int(input("\nEnter Number 2: "))
        print("\nThe Answer is: ", div(a,b))
        condition = False

    elif userinput == 2:
        a = int(input("\nEnter Number 1: "))
        b = int(input("\nEnter Number 2: "))
        print("\nThe Answer is: ", sub(a,b))
        condition = False

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
