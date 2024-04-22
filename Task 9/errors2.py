# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" #syntax error: missing quotation marks to assign the word 'lion' as a string
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth" #syntax error: missing f string format

print(full_spec) #syntax error: brackets were missing 