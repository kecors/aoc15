#!/usr/bin/python3

def parse_input(filename):
    strings = []
    with open(filename) as fp:
        for line in fp.readlines():
            strings.append(line.strip())
    return strings

def is_string_nice(string):
    vowels = [c for c in string if c in 'aeiou']
    if len(vowels) < 3:
        return False
    double_letter = False
    bad_substring = False
    for a, b in zip(string, string[1:]):
        if a == b:
            double_letter = True
        if (a, b) in [('a', 'b'), ('c', 'd'), ('p', 'q'), ('x', 'y')]:
            bad_substring = True
    if double_letter == False:
        return False
    if bad_substring == True:
        return False
    return True

def count_nice_strings(strings):
    count = 0
    for string in strings:
        if is_string_nice(string):
            count += 1
    return count

####################

def test_count_nice_strings():
    assert count_nice_strings(['ugknbfddgicrmopn']) == 1
    assert count_nice_strings(['aaa']) == 1
    assert count_nice_strings(['jchzalrnumimnmhp']) == 0
    assert count_nice_strings(['haegwjzuvuyypxyu']) == 0
    assert count_nice_strings(['dvszwmarrgswjxmb']) == 0

####################

# Part 1
test_count_nice_strings()
strings = parse_input('puzzle-input-day-05.txt')
count = count_nice_strings(strings)
print("Part 1: " + str(count) + " strings are nice")
