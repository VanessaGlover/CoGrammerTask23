# Task 11- String Handling 

# Defined my string
string = "Welcome to the good life"
# Initialising an empty string to store the modified version
new_string = ""
print(string)

# Iterate through each character in the string and check if the index is odd
# The convert to lowercase and add to the new string. The convert to uppercase and add to the new string
for i in range(len(string)):
    if i % 2 == 1:
        new_string += string[i].lower()
    else:
        new_string += string[i].upper()
print(f"{new_string}")

# Split the modifed string into a list of words 
split_string = new_string.split()

alternative_string = ""
for i in range(len(split_string)):
    if i % 2 == 0:
        split_string[i] = split_string[i].lower()
    else:
         split_string[i] = split_string[i].upper()

alternative_string = " ".join(split_string)
print(f"{alternative_string}")

