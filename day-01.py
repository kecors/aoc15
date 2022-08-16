#!/usr/bin/python3

def parse_input(filename):
    return open(filename).read().strip()

def follow_instruction(floor, instruction):
    if instruction == '(':
        floor += 1
    elif instruction == ')':
        floor -= 1
    else:
        print("Unknown instruction " + instruction)
    return floor

def follow_all_instructions(instructions):
    floor = 0
    for instruction in instructions:
        floor = follow_instruction(floor, instruction)
    return floor

def test_follow_all_instructions():
    assert follow_all_instructions('(())') == 0
    assert follow_all_instructions('()()') == 0
    assert follow_all_instructions('(((') == 3
    assert follow_all_instructions('(()(()(') == 3
    assert follow_all_instructions('))(((((') == 3
    assert follow_all_instructions('())') == -1
    assert follow_all_instructions('))(') == -1
    assert follow_all_instructions(')))') == -3
    assert follow_all_instructions(')())())') == -3

def find_position_at_basement_entry(instructions):
    floor = 0
    position = 1
    for instruction in instructions:
        floor = follow_instruction(floor, instruction)
        if floor == -1:
            return position
        else:
            position += 1

def test_find_position_at_basement_entry():
    assert find_position_at_basement_entry(')') == 1
    assert find_position_at_basement_entry('()())') == 5

####################

instructions = parse_input('puzzle-input.txt')

# Part 1
test_follow_all_instructions()
floor = follow_all_instructions(instructions)
print("Part 1: the instructions take Santa to floor " + str(floor))

# Part 2
test_find_position_at_basement_entry()
position = find_position_at_basement_entry(instructions)
print("Part 2: the position where Santa enters the basement is " + str(position))
