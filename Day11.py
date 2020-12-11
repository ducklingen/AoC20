from itertools import combinations, combinations_with_replacement
import sys
from helpers.AoCHelper import *
from helpers.GlobalVariables import *

sys.setrecursionlimit(5000)

inputlines = readInputLines('day11/day11input1.txt')


def get_adjacent_seats(i, j, seats, immediate_neighbour):
    adjacent_seats = []

    for x, y in directions:
        if immediate_neighbour and 0 <= i + x < len(seats) and 0 <= j + y < len(seats[0]):
            adjacent_seats.append(seats[i + x][j + y])
        else:
            adjacent_seats.append(get_first_in_direction(i, j, seats, x, y))

    return adjacent_seats


def get_first_in_direction(i, j, seats, x, y):
    while 0 <= i + x < len(seats) and 0 <= j + y < len(seats[0]):
        if seats[i + x][j + y] != '.':
            return seats[i + x][j + y]
        else:
            i += x
            j += y

    return '.'


def process_seats(seats, neighbour_limit, immediate_neighbour):
    new_configuration = []

    for i in range(len(seats)):
        new_seat_row = ''
        for j in range(len(seats[0])):
            seat_status = seats[i][j]

            if seat_status == '.':
                new_seat_row += seat_status
                continue

            adjacent_people = list(filter(lambda x: x == '#', get_adjacent_seats(i, j, seats, immediate_neighbour)))

            if seat_status == 'L' and len(adjacent_people) == 0:
                new_seat_row += '#'
            elif seat_status == '#' and len(adjacent_people) >= neighbour_limit:
                new_seat_row += 'L'
            else:
                new_seat_row += seat_status

        new_configuration.append(new_seat_row)

    return new_configuration


def find_stable_configuration(initial_configuration, neighbour_limit, immediate_neighbour):
    initial_seats = initial_configuration
    updated_seats = process_seats(initial_configuration, neighbour_limit, immediate_neighbour)

    while not min([i == j for i, j in zip(initial_seats, updated_seats)]):
        initial_seats = updated_seats
        updated_seats = process_seats(initial_seats, neighbour_limit, immediate_neighbour)

    return updated_seats


# Part 1
taken_seats = sum([seat_row.count('#') for seat_row in find_stable_configuration(inputlines, 4, True)])
assert taken_seats == 2263
print("Part 1: " + str(taken_seats))

# Part 2
taken_seats = sum([seat_row.count('#') for seat_row in find_stable_configuration(inputlines, 5, False)])
assert taken_seats == 2002
print("Part 2: " + str(taken_seats))
