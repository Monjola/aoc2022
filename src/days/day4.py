from src.utils.fileparse import file_rows_to_list


class Assignment:
    def __init__(self, start_id, end_id):
        self.start_id = start_id
        self.end_id = end_id


def _fully_contains(assignment1: Assignment, assignment2: Assignment) -> bool:
    if (assignment1.start_id <= assignment2.start_id) and (assignment1.end_id >= assignment2.end_id):
        return True
    elif (assignment2.start_id <= assignment1.start_id) and (assignment2.end_id >= assignment1.end_id):
        return True
    else:
        return False


def _overlaps(assignment1: Assignment, assignment2: Assignment) -> bool:
    if (assignment1.start_id <= assignment2.start_id) and (assignment1.end_id >= assignment2.start_id):
        return True
    elif (assignment2.start_id < assignment1.start_id) and (assignment2.end_id >= assignment1.start_id):
        return True
    else:
        return False


def _split_assignments(assignment_pair: str) -> tuple[Assignment, Assignment]:
    a,b = assignment_pair.split(",")
    x0,y0 = map(int, a.split("-"))
    x1,y1 = map(int, b.split("-"))
    assignment1 = Assignment(x0, y0)
    assignment2 = Assignment(x1, y1)
    return assignment1, assignment2


def part1(input_file: list) -> int:
    count = 0
    for line in input_file:
        assignment1, assignment2 = _split_assignments(line)
        if _fully_contains(assignment1, assignment2):
            count += 1
    return count


def part2(input_file: list) -> int:
    count = 0
    for line in input_file:
        assignment1, assignment2 = _split_assignments(line)
        if _overlaps(assignment1, assignment2):
            count += 1
    return count


if __name__ == "__main__":
    file = file_rows_to_list("inputs/input4.txt")
    print("part1: " + str(part1(file)))
    print("part2: " + str(part2(file)))
