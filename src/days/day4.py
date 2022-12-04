from src.utils.fileparse import file_rows_to_list


class Assignment:
    def __init__(self, start_id, end_id):
        self.start_id = start_id
        self.end_id = end_id


def fully_contains(assignment1:Assignment,assignment2:Assignment) -> bool:
    if (assignment1.start_id <= assignment2.start_id) and (assignment1.end_id >= assignment2.end_id):    
        return True
    elif (assignment2.start_id <= assignment1.start_id) and (assignment2.end_id >= assignment1.end_id):
        return True
    else: 
        return False


def overlaps(assignment1:Assignment,assignment2:Assignment) -> bool:
    if (assignment1.start_id <= assignment2.start_id) and (assignment1.end_id >= assignment2.start_id):
        return True
    elif (assignment2.start_id < assignment1.start_id) and (assignment2.end_id >= assignment1.start_id):
        return True
    else: return False

def split_assignments(assignment_pair:str) -> Assignment:
    split_pairs = assignment_pair.split(",")
    split_numbers =[]
    split_numbers.append(split_pairs[0].split("-"))
    split_numbers.append(split_pairs[1].split("-"))
    assignment1 = Assignment(int(split_numbers[0][0]),int(split_numbers[0][1]))
    assignment2 = Assignment(int(split_numbers[1][0]),int(split_numbers[1][1]))
    return assignment1, assignment2


def part1(input_file:list) -> int:
    count=0
    for line in input_file:
        assignment1, assignment2 = split_assignments(line)
        if fully_contains(assignment1, assignment2):
            count+=1
    return count


def part2(input_file:list) -> int:
    count=0
    for line in input_file:
        assignment1, assignment2 = split_assignments(line)
        if overlaps(assignment1, assignment2):
            count+=1
    return count


if __name__ == "__main__":
    input_file = file_rows_to_list("inputs/input4.txt")
    print("part1: " + str(part1(input_file)))
    print("part2: " + str(part2(input_file)))
    