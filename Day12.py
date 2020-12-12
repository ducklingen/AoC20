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
    new_direction = direction
    for i in range(math.ceil(degrees/90)):
        new_direction = (new_direction[1], -new_direction[0])

    return new_direction


for i in input_lines:
    print(i)
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

    print("New waypoint: " + str(waypoint))
    print("New position: " + str(position))

manhattan_distance = abs(position[0]) + abs(position[1])

print("Part 1: " + str(manhattan_distance))