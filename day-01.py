#!/usr/bin/python3

def parse_input(filename):
    return open(filename).read().strip()

def follow_all_instructions(instructions):
    floor = 0
    for instruction in instructions:
        if instruction == '(':
            floor += 1
        elif instruction == ')':
            floor -= 1
        else:
            print("Unknown instruction " + instruction)
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

####################

instructions = parse_input('puzzle-input.txt')

# Part 1
test_follow_all_instructions()
floor = follow_all_instructions(instructions)
print("Part 1: the instructions take Santa to floor " + str(floor))
