#Prompt the user to enter their Name
#Store the user's input in a vaiable called "name"
#Prompt the user to enter their Age
#Store the user's input in a vaiable called "age"
#Prompt the user to enter their House number
#Store the user's input in a vaiable called "house number"
#Prompt the user to enter their Street name
#Store the user's input in a vaiable called "street name"
#Then on a new line the output will print out a single sentence containing all the details of the user

name = input ("Please enter your name: ")
age = input("Please enter your age: ")
house_number = input("Please enter your house number: ")
street_name = input("Plesse enter your street name: ")
print("{} is {} years old and lives at {} {}".format(name, age, house_number, street_name))