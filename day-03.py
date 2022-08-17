#!/usr/bin/python3

def parse_input(filename):
    return open(filename).read().strip()

def compute_house_count(moves):
    x = 0
    y = 0
    houses = {(x, y)}
    for move in moves:
        if move == '^':
            y += 1
        elif move == '>':
            x += 1
        elif move == 'v':
            y -= 1
        elif move == '<':
            x -= 1
        else:
            print("Unknown move " + move)
        houses.add((x, y))
    return len(houses)

####################

def test_compute_house_count():
    assert compute_house_count('>') == 2
    assert compute_house_count('^>v<') == 4
    assert compute_house_count('^v^v^v^v^v') == 2

####################

# Part 1
test_compute_house_count()
moves = parse_input('puzzle-input-day-03.txt')
count = compute_house_count(moves)
print("Part 1: " + str(count) + " houses receive at least one present")
