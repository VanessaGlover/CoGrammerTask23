# Task 7- Control Structures - While loop

# Setting values to the variables 
total = 0
count = 0

# While this is true the user will continually be asked to enter a number
# If the user enters -1 then the user will stop receving the request to enter a number
while True:
    user_input = float(input("Enter a number: "))
    if user_input == -1:
        break

# Add the numbers inputted by the user and increment count
    total += user_input
    count += 1
# Any number greater than 0 that was entered will be used to calculate the average
if count > 0:
    average = total / count
    print(f"The average of the entered numbers is: {average}")