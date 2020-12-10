from itertools import combinations
import sys
from helpers.AoCHelper import *

sys.setrecursionlimit(5000)

## Part 1
inputlines = list(map(int, readInputLines('day10/day10input1.txt')))
inputlines.sort()

output_joltage = 0
one_jolt_differences = 0
three_jolt_differences = 0

while True:
    initial_output_joltage = output_joltage
    for i in inputlines:
        if i == output_joltage + 1:
            output_joltage = i
            one_jolt_differences += 1
        elif i == output_joltage + 2:
            output_joltage = i
        elif i == output_joltage + 3:
            output_joltage = i
            three_jolt_differences += 1

    if initial_output_joltage == output_joltage:
        break

assert one_jolt_differences * (three_jolt_differences + 1) == 1690
print(one_jolt_differences * (three_jolt_differences + 1))

## Part 2
input_lines_reversed = list(map(int, readInputLines('day10/day10input1.txt')))
input_lines_reversed.sort(reverse=True)
continuations = {}
branch_numbers = {}

for i in input_lines_reversed:
    continuations[i] = list(filter(lambda x: i < x <= i+3, inputlines))


for i in input_lines_reversed:
    if not continuations[i]:
        branch_numbers[i] = 1
    elif len(continuations[i]) > 0:
        branch_numbers[i] = sum([branch_numbers[j] for j in continuations[i]])

assert sum([branch_numbers[x] for x in set(input_lines_reversed).intersection((1, 2, 3))]) == 5289227976704
print(sum([branch_numbers[x] for x in set(input_lines_reversed).intersection((1, 2, 3))]))
