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

def compute_paper(present):
    paper = (3 * present[0] * present[1]) 
    paper += (2 * present[0] * present[2])
    paper += (2 * present[1] * present[2])
    return paper

def compute_total_paper(presents):
    total = 0
    for present in presents:
        total += compute_paper(present)
    return total

def compute_ribbon(present):
    ribbon = (2 * present[0] + 2 * present[1])
    ribbon += (present[0] * present[1] * present[2])
    return ribbon

def compute_total_ribbon(presents):
    total = 0
    for present in presents:
        total += compute_ribbon(present)
    return total

####################

def test_compute_total_paper():
    assert compute_total_paper([[2,3,4]]) == 58
    assert compute_total_paper([[1,1,10]]) == 43

def test_compute_total_ribbon():
    assert compute_total_ribbon([[2,3,4]]) == 34
    assert compute_total_ribbon([[1,1,10]]) == 14

####################

presents = parse_input('puzzle-input-day-02.txt')

# Part 1
test_compute_total_paper()
total_paper = compute_total_paper(presents)
print("Part 1: they should order " + str(total_paper) + " square feet of wrapping paper")

# Part 2
test_compute_total_ribbon()
total_ribbon = compute_total_ribbon(presents)
print("Part 2: they should order " + str(total_ribbon) + " feet of ribbon")
