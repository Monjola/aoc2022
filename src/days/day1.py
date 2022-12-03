from src.days.file_parse import file_rows_to_list, list_of_strs_to_ints

calories = file_rows_to_list("src\days\input1.txt")

calories = list_of_strs_to_ints(calories)
total_calories = [0]
j=0
for i,calorie in enumerate(calories):
    total_calories[j] = total_calories[j] + calorie
    if calorie==0:
        j+=1
        total_calories.append(0)
total_calories.sort()
top3_calorie_sum = total_calories[len(total_calories)-1] + total_calories[len(total_calories)-2] + total_calories[len(total_calories)-3]
day1_p1_answer = max(total_calories)
day1_p2_answer = top3_calorie_sum
print("Day 1 Part 1 Answer: " + str(day1_p1_answer))
print("Day 1 Part 2 Answer: " + str(day1_p2_answer))