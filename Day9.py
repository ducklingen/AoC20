from itertools import combinations

from helpers.AoCHelper import *

inputlines = readInputLines('day9/day9input1.txt')

preambleLength = 25

for i in range(len(inputlines)):
    if i < preambleLength:
        continue

    n = int(inputlines[int(i)])

    valid = False

    for j, k in combinations(inputlines[int(i)-preambleLength: int(i)], 2):
        if int(j) + int(k) == n:
            valid = True
            break

    if not valid:
        print("Part 1: ", str(n))
        break

specialnumber = 10884537

for i in range(len(inputlines)):
    j = i+1
    ix = int(inputlines[i])

    while ix < specialnumber:
        # print(ix)
        ix += int(inputlines[j])
        j += 1

        if ix == specialnumber:
            # print(ix)
            print("Range: (" + str(i) + ", " + str(j) + ")")
            break

print("Part 2: " + str(max(map(int, inputlines[386: 403])) + min(map(int, inputlines[386: 403]))))
