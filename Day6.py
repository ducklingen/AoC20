import math
import re
from string import ascii_lowercase

from helpers import AoCHelper
from helpers.AoCHelper import prints, prod

input = AoCHelper.readInputLines("day6/day6input1.txt")

numberOfYeses = 0

groups = []
group = ''

for i in input:
    if i == '':
        groups.append(group)
        group = ''
    else:
        group += (i)

groups.append(group)

# for g in groups:
#     numberOfYeses += len(set(g))

for c in ascii_lowercase:
    allYes = True

    for i in input:
        if i == '':
            if allYes:
                numberOfYeses += 1
            allYes = True

        if i != '' and c not in i:
            allYes = False

    if allYes:
        numberOfYeses += 1

prints(numberOfYeses)

