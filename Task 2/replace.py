single_string = "The!quick!brown!fox!jumps!over!the!lazy!dog."

<<<<<<< HEAD
=======
# Replace "!" with " " and convert to uppercase in a single line
>>>>>>> a4a6083a685d58df4db3d368a52b0484c8318697
new_single_string = single_string.replace("!" , " ")
print(new_single_string)

upper_case_string = new_single_string.upper()
print(upper_case_string)

reverse_string = new_single_string [:: -1]
print(reverse_string)
