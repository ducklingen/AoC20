import math
import sys
from itertools import combinations

from helpers import AoCHelper
from helpers.AoCHelper import prints, prod

input = AoCHelper.readInputLines("day1/day1input1.txt")

for i,j,k in combinations(map(int, input), 3):
    if i + j + k == 2020:
        prints(prod([i,j,k]))
        break

