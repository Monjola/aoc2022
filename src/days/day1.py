from src.utils.fileparse import file_rows_to_list, list_of_strs_to_ints

def parts_1_and_2(calories:list) -> int:
    total_calories = [0]
    j=0
    for calorie in calories:
        total_calories[j] += calorie
        if calorie==0:
            j+=1
            total_calories.append(0)
    total_calories.sort()
    return total_calories[-1], sum(total_calories[-3:])

if __name__ == "__main__":
    calories = file_rows_to_list("inputs\input1.txt")
    calories = list_of_strs_to_ints(calories)
    day1_p1_answer, day1_p2_answer = parts_1_and_2(calories)
    print("part 1 : " + str(day1_p1_answer))
    print("part 2 : " + str(day1_p2_answer))