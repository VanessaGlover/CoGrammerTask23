# Get the user input and save the variable
str_manip = input ("Enter a sentence ")

# Calculate and display the length of str_manip
length_of_str = len(str_manip)
print(f"The length of the entered sentence is: {length_of_str}")

# Find the last letter in str_manip
last_letter = str_manip[-1]
# Replace every occurrence of the last letter with '@'
str_manip_modified = str_manip.replace(last_letter, '@')

# Print the new sentence string
print(f"Original sentence: {str_manip}")
print(f"New sentence: {str_manip_modified}")

# Find the last 3 characters of the sentence
last_three_characters = str_manip[-3:][::-1]
# Print the last 3 characters of the sentence backwards
print(f"Last 3 characters in reverse order: {last_three_characters}")

five_letter_word = str_manip[:3] + str_manip[-2:]
print(f"Five-letter word: {five_letter_word}")