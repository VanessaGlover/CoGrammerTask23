# T03- Practical Task 

# Using the if, elif and else functions to print out the correct statement for each age bracket

try:
    age = int(input("Please enter your age: \n"))

    if age > 100:
        print("Sorry, you're dead.")
    elif age >= 65:
        print("Enjoy your retirement! \n")
    elif age >= 40:
        print("You're over the hill \n")
    elif age < 13:
        print("You qualify for the kiddie discount! \n")
    elif age == 21:
        print("Congrats on your 21st! \n")
    else:
        print("Age is but a number. \n")

except ValueError:
    print("Error: Please enter a valid number.")
