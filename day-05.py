#!/usr/bin/python3
# pylint: disable=invalid-name
"""
    Solution for Advent of Code 2015, day 5
"""

def parse_input(filename):
    """ Parse the input file """
    strings = []
    with open(filename) as fp:
        for line in fp.readlines():
            strings.append(line.strip())
    return strings

def is_string_nice_part_1(string):
    """ Determine if string is nice (part 1) """
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
    if double_letter is False:
        return False
    if bad_substring is True:
        return False
    return True

def is_string_nice_part_2(string):
    """ Determine if string is nice (part 2) """
    pair_repeats = False
    pairs = []
    for j in range(len(string) - 1):
        pairs.append(string[j] + string[j + 1])
    for m, _ in enumerate(pairs):
        for n in range(m + 2, len(pairs)):
            if pairs[m] == pairs[n]:
                pair_repeats = True
                break
    letter_repeats_after_one_letter = False
    for a, b in zip(string, string[2:]):
        if a == b:
            letter_repeats_after_one_letter = True
            break
    return pair_repeats and letter_repeats_after_one_letter

def is_string_nice(part, string):
    """ Call appropriate function based on part """
    if part == 1:
        return is_string_nice_part_1(string)
    return is_string_nice_part_2(string)

def count_nice_strings(part, strings):
    """ High level solution """
    count = 0
    for string in strings:
        if is_string_nice(part, string):
            count += 1
    return count

####################

def test_count_nice_strings():
    """ Test solution with provided examples """
    assert count_nice_strings(1, ['ugknbfddgicrmopn']) == 1
    assert count_nice_strings(1, ['aaa']) == 1
    assert count_nice_strings(1, ['jchzalrnumimnmhp']) == 0
    assert count_nice_strings(1, ['haegwjzuvuyypxyu']) == 0
    assert count_nice_strings(1, ['dvszwmarrgswjxmb']) == 0
    assert count_nice_strings(2, ['qjhvhtzxzqqjkmpb']) == 1
    assert count_nice_strings(2, ['xxyxx']) == 1
    assert count_nice_strings(2, ['uurcxstgmygtbstg']) == 0
    assert count_nice_strings(2, ['ieodomkazucvgmuy']) == 0

####################

def main():
    """ Advent of Code 2015 day 5 """
    test_count_nice_strings()
    # Part 1
    strings = parse_input('puzzle-input-day-05.txt')
    count = count_nice_strings(1, strings)
    print("Part 1: " + str(count) + " strings are nice")
    # Part 2
    strings = parse_input('puzzle-input-day-05.txt')
    count = count_nice_strings(2, strings)
    print("Part 2: " + str(count) + " strings are nice")

if __name__ == '__main__':
    main()
