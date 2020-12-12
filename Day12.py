import copy
import sys
import math
from helpers.AoCHelper import *
from helpers.GlobalVariables import *

sys.setrecursionlimit(5000)

input_lines = read_input_lines('day12/day12input1.txt')

position = (0, 0)
waypoint = (10, 1)
direction = (1, 0)


def turn(direction, degrees):
    for i in range(math.ceil(degrees/90)):
        direction = (direction[1], -direction[0])

    return direction


for i in input_lines:
    operation = i[0:1]
    value = int(i[1:])

    if operation == 'N':
        position = (position[0], position[1] + value)
    if operation == 'S':
        position = (position[0], position[1] - value)
    if operation == 'E':
        position = (position[0] + value, position[1])
    if operation == 'W':
        position = (position[0] - value, position[1])
    if operation == 'F':
        position = (position[0] + value * direction[0], position[1] + value * direction[1])
    if operation == 'R':
        direction = turn(direction, value)
    if operation == 'L':
        direction = turn(direction, 360-value)


manhattan_distance = abs(position[0]) + abs(position[1])
assert manhattan_distance == 1148
print("Part 1: " + str(manhattan_distance))

for i in input_lines:
    operation = i[0:1]
    value = int(i[1:])

    if operation == 'N':
        waypoint = (waypoint[0], waypoint[1] + value)
    if operation == 'S':
        waypoint = (waypoint[0], waypoint[1] - value)
    if operation == 'E':
        waypoint = (waypoint[0] + value, waypoint[1])
    if operation == 'W':
        waypoint = (waypoint[0] - value, waypoint[1])
    if operation == 'F':
        position = (position[0] + value * waypoint[0], position[1] + value * waypoint[1])
    if operation == 'R':
        waypoint = turn(waypoint, value)
    if operation == 'L':
        waypoint = turn(waypoint, 360-value)


manhattan_distance = abs(position[0]) + abs(position[1])
assert manhattan_distance == 51419
print("Part 2: " + str(manhattan_distance))