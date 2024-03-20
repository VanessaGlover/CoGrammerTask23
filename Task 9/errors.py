
# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") #syntax error: brackets were missing for the string
print ("\n") #syntax error: unexpected indentation & brackets were missing

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" #syntax error: the variable should have been assigned a value with '=' instead of '==' which compares values 
age = int(age_Str) #synthax error: unexpected indentation
print("I'm" + str(age) + "years old.") #syntax error: unexpeced indentation

    # Variables declaring additional years and printing the total years of age
years_from_now = 3 #syntax error: unexpected indentation
total_years = age + years_from_now #syntax error: unexpected indentation

print ("The total number of years:" + str(total_years)) #syntax error: the brackets were missing for the string & the wrong variable was called

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 #syntax error: the wrong variable was called
print ("In 3 years and 6 months, I'll be " + str(total_months) + " months old") #syntax error: missing brackets

#HINT, 330 months is the correct answer