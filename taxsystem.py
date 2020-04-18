import sys
import tkinter
import math


Allowance = int(132000)
mpf = int()
tax = int()
income = int()
x = int()
count = int()

def isInt(income_input):
    try:
        int(income_input)
        return True
    except ValueError:
        return False


def cal_mpf(income_input):
    if (income_input >= 30000*12):
        mpf = 18000
    elif (income_input < 7100*12):
        mpf = 0
    else:
        mpf = int(income_input *0.05)
    print("mpf is", mpf)
    return mpf

def net_income(income_input):
    income = income_input - Allowance - cal_mpf(income_input)
    if income <= 0:
        income = 0
    return income

def cal_tax(income):
    global tax
    count = 0
    print("net income is", income)
    while (income >= 50000) and (count < 4):
        income -= 50000
        count += 1
    if count == 0:
        tax = (0.02*income)
    if count == 1:
        tax = 1000 + (0.06*income)
    if count == 2:
        tax = 1000 + 3000 + (0.1*income)
    if count == 3:
        tax = 1000 + 3000 + 5000 + (0.14*income)
    if count == 4:
        tax = 1000 + 3000 + 5000 + 7000 + (0.17*income)
    return int(tax)

def taxSingle(income_input):    #tax calculation for single
    income = net_income(income_input)
    x = cal_tax(income)
    if income != 0:
        print("Annual Income:", income_input)
        print("Net chargable Income:", income)
        print("Tax payable by you:", x)
    else:
        low_input()

def taxMarried(input1, input2): #tax calculation for married
    income1 = net_income(input1)
    income2 = net_income(input2)
    if income1 != 0 or income2 != 0:
        tax1 = cal_tax(income1)
        tax2 = cal_tax(income2)
        joint_payment = cal_tax(income1 + income2)
        separate_payment = tax1 + tax2
        print("Separate Payment:", separate_payment)
        print("Joint Payment:", joint_payment)
        if separate_payment < joint_payment:
            print("You should pay tax by separate Payment")
        else:
            print("You should pay tax by joint Payment")
    else:
        low_input()

def Standard_tax(income_input):
    tax = int(income_input*0.15)
    print("Net Income:", income_input)
    print("Standard Tax payable by you:", tax)

def low_input():
    print("Your income is too low")
    print("You do not have to pay tax")

def quit():
    print ("You quit the Tax System")

def main():
    instructions = """Please select your marital status:
       1 to select Single Tax calculation
       2 to select Married Tax calculation
       3 to end \n"""

    while True:
        print (instructions)
        choice = input( "Enter your choice:" )

        if choice == "1":
            while True:
                income_input = input("Enter your income:")
                if isInt(income_input) == True:
                    income_input = int(income_input)
                    break
                else:
                    print("It is a invalid input")
                    print("Please try again")
            if(income_input > 2040023):
                print("mpf: 18000")
                print("Annual Income:", income_input)
                Standard_tax(income_input - 18000)
            else:
                taxSingle(income_input)
        elif choice == "2":
            while True:
                input1 = input("Enter self income:")
                input2 = input("Enter spouse income:")
                if isInt(input1) == True and isInt(input2) == True:
                    input1 = int(input1)
                    input2 = int(input2)
                    break
                else:
                    print("It is a invalid input")
                    print("Please try again")
            if(input1 + input2 > 3180024):
                input1 = input1 - cal_mpf(input1)
                input2 = input2 - cal_mpf(input2)
                print("Net self Income:", input1 - Allowance)
                print("Net spouse income:", input2 - Allowance)
                Standard_tax(input1 + input2)
            else:
                taxMarried(input1, input2)
        elif choice == "3":
            print("End Tax computation system")
            exit()

        else:
            sys.stderr.write("\nWrong input, please try again\n")



if __name__ == "__main__":
    main()
