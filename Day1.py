import math
from helpers import AoCHelper
from helpers.AoCHelper import prints, prod

input = AoCHelper.readInputLines("day1/day1input1.txt")

for i in input:
    for j in input:
        for k in input:
            if int(i) + int(j) + int(k) == 2020:
                prints(prod([i,j,k]))

