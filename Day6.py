import math
import re
from string import ascii_lowercase
from helpers import AoCHelper
from helpers.AoCHelper import prints, prod, listToString, groupLines

input = AoCHelper.readInputLines("day6/day6input1.txt")
groups = groupLines(input)

numberOfYeses = 0

for g in groups:
    numberOfYeses += len(set(listToString(g)))

assert numberOfYeses == 6625
print("Part 1: " + str(numberOfYeses))
numberOfYeses = 0

for c in ascii_lowercase:
    for g in groups:
        allYes = True
        for i in g:
            if c not in i:
                allYes = False

        if allYes:
            numberOfYeses += 1

assert numberOfYeses == 3360
prints("Part 2: " + str(numberOfYeses))

