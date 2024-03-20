import math
# Task 5 - Capstone.
# Getting the user's input on which choice they wish to proceed with
choice = input("""Choose either 'investment' or 'bond' from the menu below to proceed:

            investment      - to calculate the amount of interest you'll earn on interest
            bond            - to calculate the amount you'll have to pay on a home loan
               
            Enter here: """)

# This will ensure that the input by the user (e.g. Investment or investment etc.) are accepted into the conditional statement.
choice = choice.lower()

# Getting input from user on amount, rate, years and interest type to enter into investment calculator.
if choice == "investment":

    deposit = float(input("Please enter the amount of money you wish to deposit: \n"))           
    interest_rate = float(input("Please enter your interest rate as a number: \n"))
    years = int(input("Please enter the number of years you plan on investing for: \n"))
    interest_type = input("Please enter your investment choice type: (simple or compound) \n")
    

    # Creating indented conditional statement to display the results based on user's choice of interest type.
    # Entering formulas for simple and compound interest depending on user choice.
    simple_interest = deposit * (1 + (interest_rate/100) * years)
    simple_interest = round(simple_interest, 2)
    print()

    compound_interest = deposit * math.pow((1 + (interest_rate/100)), years)
    compound_interest = round (compound_interest, 2)
    print()

    if interest_type == "simple":
        print(f"Your interest after {years} years of investing will be £ {simple_interest}")
    elif interest_type == "compound":
        print(f"Your compound interest after {years} years of investing will be £ {compound_interest}")

# Second part of conditional statement for bond option
# Getting input from user on house value, interest rate and number of months taken to pay bond
elif choice == "bond":
    house_value = float(input("Please enter the present value of the house: \n"))
    bond_interest_rate = float(input("Please enter your interest rate as a number: \n"))
    months = int(input("Please enter the number of months you plan to take to repay the bond: \n"))

    bond_interest = bond_interest_rate / 100 / 12
# Entering Formula for bond calculator.
    monthly_payment = (bond_interest * house_value) / (1 - (1+ bond_interest) **  (- months))
# Displaying monthly payment results.
    print(f"Your monthly repayment amount for the home loan will be £ {monthly_payment}")
else:
    print("Invalid input. Please enter 'investment' or 'bond'")