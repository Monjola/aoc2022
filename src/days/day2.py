from enum import Enum

from fileparse import file_rows_to_list

class MyChoice(Enum):
    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"

class OpponentsChoice(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"

class Result(Enum):
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"

def generate_choice(opponents_choice: str, desired_outcome: str) -> str:
    possible_choices = [MyChoice.ROCK.value, MyChoice.PAPER.value, MyChoice.SCISSORS.value]
    
    match opponents_choice:
        case OpponentsChoice.ROCK.value:
            opponents_choice_index = 0
        case OpponentsChoice.PAPER.value:
            opponents_choice_index = 1
        case OpponentsChoice.SCISSORS.value:
            opponents_choice_index = 2

    match desired_outcome:
        case Result.LOSE.value:
            offset = -1
        case Result.DRAW.value:
            offset = 0
        case Result.WIN.value:
            offset = 1

    resulting_index = 0 if (opponents_choice_index + offset) == 3 else (opponents_choice_index + offset)

    return possible_choices[resulting_index]


def choice_based_score(choice: str) -> int:
    match choice:
        case MyChoice.ROCK.value:
            return 1
        case MyChoice.PAPER.value:
            return 2
        case MyChoice.SCISSORS.value:
            return 3


def result_based_score(result: str) -> int:
    match result:
        case Result.LOSE.value:
            return 0
        case Result.DRAW.value:
            return 3
        case Result.WIN.value:
            return 6


def part1(input: list) -> str:
    total_score = 0
    for row in input:
        temp_score = 0
        opponents_choice = row[0]
        my_choice = row[2]
        match opponents_choice:
            case OpponentsChoice.ROCK.value:
                match my_choice:
                    case MyChoice.ROCK.value:
                        temp_score += 4
                    case MyChoice.PAPER.value:
                        temp_score += 8
                    case MyChoice.SCISSORS.value:
                        temp_score += 3
            case OpponentsChoice.PAPER.value:
                match my_choice:
                    case MyChoice.ROCK.value:
                        temp_score += 1
                    case MyChoice.PAPER.value:
                        temp_score += 5
                    case MyChoice.SCISSORS.value:
                        temp_score += 9
            case OpponentsChoice.SCISSORS.value:
                match my_choice:
                    case MyChoice.ROCK.value:
                        temp_score += 7
                    case MyChoice.PAPER.value:
                        temp_score += 2
                    case MyChoice.SCISSORS.value:
                        temp_score += 6
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
