from file_parse import file_rows_to_list

def get_priority(item:str) -> int:
    if item.isupper():
        return ord(item)-38
    else:
        return ord(item)-96


rucksacks = file_rows_to_list("inputs\input3.txt")
value = 0
for rucksack in rucksacks:
    center_index = int(len(rucksack)/2)
    first_half = rucksack[:center_index]
    second_half = rucksack[center_index:]

    for item in first_half:
        if item in second_half:
            value += get_priority(item)
            break
print("part 1 solution: " + str(value))



grouped_list = []
for i in range(100):
    local_list = []
    local_list.append(rucksacks.pop())
    local_list.append(rucksacks.pop())
    local_list.append(rucksacks.pop())
    grouped_list.append(local_list)

value = 0
for group in grouped_list:
    for item in group[0]:
        if (item in group[1]) and (item in group[2]):
            value += get_priority(item)
            break

print("part 2 solution: " + str(value))
