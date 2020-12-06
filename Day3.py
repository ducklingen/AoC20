import math
from helpers import AoCHelper
from helpers.AoCHelper import prints

input = AoCHelper.readInputLines("day3/day3input1.txt")

numberOfTrees = 1
forest = []

patternExpansion = math.ceil(len(input) / len(input[0]))

for i in input:
    forest.append(i*patternExpansion*10)


def treesInSlope(x,y):
    trees = 0
    for k in range(math.ceil(len(input)/x)):
        if forest[x*k][y*k] == '#':
            trees += 1
    return trees


print("Part 1: " + str(treesInSlope(1, 3)))

slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]

for slope in slopes:
    numberOfTrees *= treesInSlope(slope[0], slope[1])

print("Part 2: " + str(numberOfTrees))
