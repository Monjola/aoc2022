from file_parse import file_rows_to_list, list_of_strs_to_ints

calories = file_rows_to_list("src\days\shortinput1.txt")

calories = list_of_strs_to_ints(calories)
for calorie in calories:
    
print(calories)