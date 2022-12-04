from enum import Enum, unique

from src.utils.fileparse import file_rows_to_list


@unique
class MyChoice(Enum):
    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"


@unique
class OpponentsChoice(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"


@unique
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


def outcome(opponents_choice:str,my_choice:str) -> str:
    match opponents_choice:
        case OpponentsChoice.ROCK.value:
            match my_choice:
                case MyChoice.ROCK.value:
                    return Result.DRAW.value
                case MyChoice.PAPER.value:
                    return Result.WIN.value
                case MyChoice.SCISSORS.value:
                    return Result.LOSE.value

        case OpponentsChoice.PAPER.value:
            match my_choice:
                case MyChoice.ROCK.value:
                    return Result.LOSE.value
                case MyChoice.PAPER.value:
                    return Result.DRAW.value
                case MyChoice.SCISSORS.value:
                    return Result.WIN.value

        case OpponentsChoice.SCISSORS.value:
            match my_choice:
                case MyChoice.ROCK.value:
                    return Result.WIN.value
                case MyChoice.PAPER.value:
                    return Result.LOSE.value
                case MyChoice.SCISSORS.value:
                    return Result.DRAW.value


def part1(strategy_guide: list) -> str:
    total_score = 0
    for instruction in strategy_guide:
        opponents_choice = instruction[0]
        my_choice = instruction[2]
        temp_score = choice_based_score(my_choice)
        result = outcome(opponents_choice, my_choice)
        temp_score += result_based_score(result)
        total_score += temp_score
    return total_score


def part2(strategy_guide: list) -> str:
    total_score = 0
    for instruction in strategy_guide:
        opponents_choice = instruction[0]
        outcome = instruction[2]
        choice = generate_choice(opponents_choice, outcome)
        total_score += choice_based_score(choice)
        total_score += result_based_score(outcome)
    return total_score


if __name__ == "__main__":
    input = file_rows_to_list("inputs/input2.txt")
    print("part 1: " + str(part1(input)))
    print("part 2: " + str(part2(input)))
