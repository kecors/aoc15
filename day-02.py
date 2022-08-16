#!/usr/bin/python3

def parse_input(filename):
    presents = []
    with open(filename) as fp:
        for line in fp.readlines():
            present = []
            for dimension in line.strip().split('x'):
                present.append(int(dimension))
            present.sort()
            presents.append(present)
    return presents

def compute_present_footage(present):
    footage = (3 * present[0] * present[1]) + (2 * present[0] * present[2]) + (2 * present[1] * present[2])
    return footage

def compute_total_footage(presents):
    total = 0
    for present in presents:
        total += compute_present_footage(present)
    return total

def test_compute_total_footage():
    assert compute_total_footage([[2,3,4]]) == 58
    assert compute_total_footage([[1,1,10]]) == 43

####################

presents = parse_input('puzzle-input-day-02.txt')

# Part 1
test_compute_total_footage()
total = compute_total_footage(presents)
print("They should order " + str(total) + " square feet of wrapping paper")
