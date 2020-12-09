from itertools import combinations

from helpers.AoCHelper import *

inputlines = readInputLines('day9/day9input1.txt')
preambleLength = 25


def find_invalid_number(lines):
    for i in range(len(lines)):
        if i < preambleLength:
            continue

        valid = False

        for j, k in combinations(lines[int(i) - preambleLength: int(i)], 2):
            if int(j) + int(k) == int(lines[int(i)]):
                valid = True
                break

        if not valid:
            return int(lines[int(i)])


special_number = find_invalid_number(inputlines)
assert special_number == 10884537
print("Part 1:", str(special_number))


def find_contiguous_set(lines, target_number):
    for i in range(len(lines)):
        j = i + 1
        i_as_int = int(lines[i])

        while i_as_int < target_number:
            i_as_int += int(lines[j])
            j += 1

            if i_as_int == target_number:
                return i, j


range_start, range_end = find_contiguous_set(inputlines, special_number)
p2 = max(map(int, inputlines[range_start: range_end])) + min(map(int, inputlines[range_start: range_end]))

assert p2 == 1261309
print("Part 2: " + str(p2))
