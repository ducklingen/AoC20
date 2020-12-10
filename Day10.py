from itertools import combinations
import sys
from helpers.AoCHelper import *

sys.setrecursionlimit(5000)

inputlines = list(map(int, readInputLines('day10/day10input1.txt')))
inputlinesreversed = list(map(int, readInputLines('day10/day10input1.txt')))
inputlines.sort()
inputlinesreversed.sort(reverse=True)

adapters_used = set()

output_joltage = 0

# one_jolt_differences = 0
# three_jolt_differences = 0
#
# while True:
#     initial_output_joltage = output_joltage
#     for i in inputlines:
#         if i == output_joltage + 1:
#             output_joltage = i
#             one_jolt_differences += 1
#             adapters_used.add(i)
#         elif i == output_joltage + 2:
#             output_joltage = i
#             adapters_used.add(i)
#         elif i == output_joltage + 3:
#             output_joltage = i
#             three_jolt_differences += 1
#             adapters_used.add(i)
#
#     if initial_output_joltage == output_joltage:
#         print("No new adapters found")
#         break

# print(len(inputlines))
# print(len(adapters_used))
# print(output_joltage+3)
# print(one_jolt_differences)
# print(three_jolt_differences)
# print(one_jolt_differences * (three_jolt_differences+1))

def valid_single_continuations(o, adapters):
    single_continuations = []

    for a in adapters:
        if o < a <= o+3:
            single_continuations.append(a)

    return single_continuations


continuations = {}

branch_numbers = {}

for i in inputlines:
    continuations[i] = valid_single_continuations(i, inputlines)


for i in inputlinesreversed:
    if continuations[i] == []:
        branch_numbers[i] = 1
    elif len(continuations[i]) > 0:
        branch_numbers[i] = sum([branch_numbers[j] for j in continuations[i]])

print(sum([branch_numbers[x] for x in inputlines[0:3]]))


def valid_continuations(o, adapters):
    continuations = 0

    if len(adapters) == 1:
        return 1

    for idx, a in enumerate(adapters):
        if o < a <= o+3:
            continuations += valid_continuations(a, adapters[idx+1:])
        elif a > o+3:
            break

    return continuations


# print(valid_continuations(0, inputlines))

# for i in inputlines:
#     print(str(i) + ": " + str(valid_single_continuations(i, inputlines)))
#
# print(3*prod([valid_single_continuations(i, inputlines) for i in inputlines[:-1]]))