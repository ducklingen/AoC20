import math
import sys
import unittest
from itertools import combinations

from helpers import AoCHelper
from helpers.AoCHelper import prints, prod

input = AoCHelper.readInputLines("day1/day1input1.txt")


for i, j in combinations(map(int, input), 2):
    if i + j == 2020:
        assert prod([i, j]) == 539851
        print("Part 1: " + str(prod([i, j])))
        break

for i, j, k in combinations(map(int, input), 3):
    if i + j + k == 2020:
        assert prod([i, j, k]) == 212481360
        print("Part 2: " + str(prod([i, j, k])))
        break


