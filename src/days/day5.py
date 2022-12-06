import re

from fileparse import file_rows_to_list

stacks = [  ["R","G","J","B","T","V","Z"],
            ["J","R","V","L"],
            ["S","Q","F"],
            ["Z","H","N","L","F","V","Q","G"],
            ["R","Q","T","J","C","S","M","W"],
            ["S","W","T","C","H","F"],
            ["D","Z","C","V","F","N","J"],
            ["L","G","Z","D","W","R","F","Q"],
            ["J","B","W","V","P"]]


def move_several(nr_of_crates:int, source_stack:int, goal_stack:int):
    crates_in_crane = stacks[source_stack-1][-1*nr_of_crates:]
    del stacks[source_stack-1][-1*nr_of_crates:]
    stacks[goal_stack-1] += crates_in_crane


def move(nr_of_crates:int, source_stack:int, goal_stack:int):
    for i in range(nr_of_crates):
        crate_in_crane = stacks[source_stack-1].pop()
        stacks[goal_stack-1].append(crate_in_crane)

def get_answer():
    answer = ''
    for stack in stacks:
        if len(stack) != 0:
            answer += stack.pop()
    print(answer)


def parse(input: str):
    pattern = re.compile(r'\[\d\]')
    match = pattern.search(input)
    print(match)
    


def part1_parse(input:list) -> str:
    for row in input:
        parse(row)
def part1(input:list) -> str:
    for row in input:
        decoded_move = row.split(' ')
        nr_of_crates=int(decoded_move[1])
        source_stack=int(decoded_move[3])
        goal_stack=int(decoded_move[5])
        move(nr_of_crates,source_stack,goal_stack)
        
def part2(input:list) -> str:
    for row in input:
        decoded_move = row.split(' ')
        nr_of_crates=int(decoded_move[1])
        source_stack=int(decoded_move[3])
        goal_stack=int(decoded_move[5])
        move_several(nr_of_crates,source_stack,goal_stack)

if __name__ == '__main__':
    #input = file_rows_to_list("inputs\input5instructionsonly.txt")
    input = file_rows_to_list("inputs\input5stacksonly.txt")
    part1_parse(input)
    #part1(input)
    #part2(input)
    #get_answer()