import math
try:
    def simple_interest(amount,interest,numYears):
        total_amount = amount*(1+(interest/100)*numYears)
        return total_amount
    def compound_interest(amount,interest,numYears):
        total_amount = amount*math.pow((1+(interest/100)),numYears)
        return total_amount
    def Investment():
        amount = float(input("Enter amount to deposit: "))
        rate = float(input("Enter interest rate: "))
        numYears = int(input("Enter number of year: "))
        check = True
        while check:
            interest = input("Do you want simple or compound interest?: ").lower()
            if interest == "simple":
                amount = simple_interest(amount,rate,numYears)
                print("=====================================================")
                print(f"Estimated amount :R{amount}\nType: {interest} interest\nNumber of Years: {numYears}\nRate :{rate}%")
                print("=====================================================")
                check = False
            elif interest == "compound":
                amount = compound_interest(amount,rate,numYears)
                print("=====================================================")
                print(f"Estimated amount :R{amount}\nType: {interest} interest\nNumber of Years: {numYears}\nRate :{rate}%")
                print("=====================================================")
                check = False
    def Bond():
        amount = float(input("Enter the present value of the house: "))
        rate = float(input("Enter interest rate: "))
        numMonths = int(input("Enter number of months to repay the bond: "))
        repayment = ((rate/100)*amount)/(1-math.pow(1+(rate/100),(-numMonths)))
        print("=====================================================")
        print(f"Estimated Montly payment :R{repayment}\nHouse Value :R{amount}\nNumber of months :R{numMonths}\nInterest Rate :{rate}%")
        print("=====================================================")
        
    while True:
        print("\nChoose either 'ínvestment' or 'bond' from the menu below to proceed:\n\n"
              "Investment    -to calculate the amount of interest you'll earn on interst\n"
              "Bond          -to calculate the amount you'll have to pay on a home loan")
        type = input("Enter: ").lower()
        if type == "investment":
            Investment()
        elif type == "bond":
            Bond()
        else:
            print("Please select only Investment or Bond")

        myInput  = input("Do you want to continue? yes/no :").lower()
        if myInput == "no":
            break
    print("=========================Good Bye!!!============================")
except:
    print("=====================================================")
    print("Something went wrong, please restart the program.(^_^)")
    print("=========================Good Bye!!!============================")
