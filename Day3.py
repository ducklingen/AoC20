import math
from helpers import AoCHelper
from helpers.AoCHelper import prints, prod

input = AoCHelper.readInputLines("day3/day3input1.txt")

patternExpansion = math.ceil(len(input) / len(input[0]))
forest = [i*patternExpansion*10 for i in input]


def treesInSlope(x,y):
    trees = 0
    for k in range(math.ceil(len(input)/x)):
        trees += (forest[x*k][y*k] == '#')
    return trees


assert treesInSlope(1, 3) == 181
print("Part 1: " + str(treesInSlope(1, 3)))

slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
numberOfTrees = prod([treesInSlope(slope[0], slope[1]) for slope in slopes])

assert numberOfTrees == 1260601650
print("Part 2: " + str(numberOfTrees))
