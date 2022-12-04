from src.days.fileparse import file_rows_to_list


def generate_choice(opponents_choice: str, desired_outcome: str) -> str:
    possible_choices = ["X", "Y", "Z"]
    if opponents_choice == 'A':
        opponents_choice_index = 0
    elif opponents_choice == 'B':
        opponents_choice_index = 1
    elif opponents_choice == 'C':
        opponents_choice_index = 2

    if desired_outcome == 'X':
        offset = -1
    elif desired_outcome == 'Y':
        offset = 0
    if desired_outcome == 'Z':
        offset = 1

    if (opponents_choice_index + offset) == 3:
        resulting_index = 0
    else:
        resulting_index = (opponents_choice_index + offset)
    return possible_choices[resulting_index]


def choice_based_score(choice: str) -> int:
    match choice:
        case "X":
            return 1
        case "Y":
            return 2
        case "Z":
            return 3


def result_based_score(result: str) -> int:
    match result:
        case "X":
            return 0
        case "Y":
            return 3
        case "Z":
            return 6


def part1(input: list) -> str:
    total_score = 0
    for row in input:
        temp_score = 0
        if row[0] == 'A':
            if row[2] == 'X':
                temp_score += 3
                temp_score += 1
            elif row[2] == 'Y':
                temp_score += 6
                temp_score += 2
            elif row[2] == 'Z':
                temp_score += 0
                temp_score += 3
        elif row[0] == 'B':
            if row[2] == 'X':  #
                temp_score += 0
                temp_score += 1
            elif row[2] == 'Y':
                temp_score += 3
                temp_score += 2
            elif row[2] == 'Z':
                temp_score += 6
                temp_score += 3
        elif row[0] == 'C':
            if row[2] == 'X':
                temp_score += 6
                temp_score += 1
            elif row[2] == 'Y':
                temp_score += 0
                temp_score += 2
            elif row[2] == 'Z':
                temp_score += 3
                temp_score += 3
        total_score += temp_score
    return total_score


def part2(input: list) -> str:
    total_score = 0
    for row in input:
        choice = generate_choice(row[0], row[2])
        total_score += choice_based_score(choice)
        total_score += result_based_score(row[2])
    return total_score


if __name__ == "__main__":
    input = file_rows_to_list("inputs/input2.txt")
    print("part 1: " + str(part1(input)))
    print("part 2: " + str(part2(input)))
