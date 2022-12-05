from src.days.fileparse import file_rows_to_list

def _get_priority(item:str) -> int:
    if item.isupper():
        return ord(item)-38
    else:
        return ord(item)-96

def part1(rucksacks:list) -> int:
    value = 0
    for rucksack in rucksacks:
        center_index = int(len(rucksack)/2)
        first_half = rucksack[:center_index]
        second_half = rucksack[center_index:]

        for item in first_half:
            if item in second_half:
                value += _get_priority(item)
                break
    return value

def part2(rucksacks:list) -> int:
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
                value += _get_priority(item)
                break
    return value

if __name__ == "__main__":
    rucksacks = file_rows_to_list("inputs\input3.txt")
    print("part 1: " + str(part1(rucksacks)))
    print("part 2: " + str(part2(rucksacks)))
