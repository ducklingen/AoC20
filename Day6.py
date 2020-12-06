import math
import re
from string import ascii_lowercase
from helpers import AoCHelper
from helpers.AoCHelper import prints, prod, listToString, groupLines

input = AoCHelper.readInputLines("day6/day6input1.txt")
groups = groupLines(input)

numberOfYeses = sum([len(set(listToString(g))) for g in groups])

assert numberOfYeses == 6625
print("Part 1: " + str(numberOfYeses))
numberOfYeses = 0

for c in ascii_lowercase:
    for g in groups:
        allYes = True
        for i in g:
            if c not in i:
                allYes = False
                break

        numberOfYeses += allYes

assert numberOfYeses == 3360
prints("Part 2: " + str(numberOfYeses))

