import re
from helpers.GlobalVariables import *


def readInputLines(filename, linebreaks=False):
    if linebreaks:
        return [line for line in open("Inputs/" + filename)]
    else:
        return [line.rstrip('\n') for line in open("Inputs/" + filename)]


def readInputCommaLine(filename):
    lines = readInputLines(filename)
    return lines[0].split(',')


def readInputCommaLines(filename):
    lines = readInputLines(filename)

    lists = []

    for i in lines:
        lists.append(i.split(','))

    return lists


def prints(i):
    print(str(i))


def prod(ints):
    p = 1
    for i in ints:
        p *= int(i)
    return p


def listToString(listofstrings, separator=''):
    string = ''
    for l in listofstrings:
        string += (str(l) + separator)
    return string


def groupLines(inputlines):
    groups = []
    group = []

    for i in inputlines:
        if i == '':
            groups.append(group)
            group = []
        else:
            group.append(i)

    groups.append(group)

    return groups


def extract_numbers_from_line(line):
    pattern = r'((?<!\d)[+-]?)(\d+)'
    return [int(match.group()) for match in re.finditer(pattern, line)]


def extract_numbers(lines):
    return [extract_numbers_from_line(line) for line in lines]


def get_neighbours(i, j, grid, immediate_neighbour, characters_to_skip):
    neighbours = []

    for x, y in directions:
        if immediate_neighbour and 0 <= i + x < len(grid) and 0 <= j + y < len(grid[0]):
            neighbours.append(grid[i + x][j + y])
        else:
            neighbours.append(get_first_in_direction(i, j, grid, x, y, characters_to_skip))

    return neighbours


def get_first_in_direction(i, j, seats, i_increment, j_increment, characters_to_skip):
    while 0 <= i + i_increment < len(seats) and 0 <= j + j_increment < len(seats[0]):
        if seats[i + i_increment][j + j_increment] not in characters_to_skip:
            return seats[i + i_increment][j + j_increment]
        else:
            i += i_increment
            j += j_increment

    return '.'
