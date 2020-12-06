import math
from helpers import AoCHelper
from helpers.AoCHelper import prints

input = AoCHelper.readInputLines("day3/day3test0.txt")

numberOfTrees = 1
forest = []

patternExpansion = math.ceil(len(input) / len(input[0]))

for i in input:
    forest.append(i*patternExpansion*10)

def treesInSlope(x,y):
    treesInSlope = 0
    for k in range(math.ceil(len(input)/x)):
        if forest[x*k][y*k] == '#':
            treesInSlope+=1
    return treesInSlope

slopes = [[1,1], [1, 3], [1, 5], [1,7], [2,1]]

for slope in slopes:
    numberOfTrees*=treesInSlope(slope[0], slope[1])

prints(numberOfTrees)
