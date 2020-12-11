from itertools import combinations
import sys
from helpers.AoCHelper import *

sys.setrecursionlimit(5000)

inputlines = readInputLines('day11/day11input1.txt')


for i in inputlines:
    print(i)

def get_adjacent_seats(i, j, seats):
    adjacent_seats = []

    height = len(seats)
    width = len(seats[0])

    if i > 0:
        adjacent_seats.append(seats[i-1][j])
        if j > 0:
            adjacent_seats.append(seats[i-1][j-1])
        if j < width - 1:
            adjacent_seats.append(seats[i-1][j+1])
    if j > 0:
        adjacent_seats.append(seats[i][j-1])
    if j < width - 1:
        adjacent_seats.append(seats[i][j+1])
    if i < height - 1:
        adjacent_seats.append(seats[i+1][j])
        if j > 0:
            adjacent_seats.append(seats[i+1][j-1])
        if j < width - 1:
            adjacent_seats.append(seats[i+1][j+1])

    return adjacent_seats

def get_first_in_direction(i, j, seats, x, y):
    first = '.'
    height = len(seats)
    width = len(seats[0])

    while 0 <= i + x < height and 0 <= j + y < width:
        if seats[i + x][j + y] != '.':
            return seats[i + x][j + y]
        else:
            i += x
            j += y

    return first


def get_adjacent_seats2(i, j, seats):
    adjacent_seats = []

    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x != 0 or y != 0:
                adjacent_seats.append(get_first_in_direction(i, j, seats, x, y))

    return adjacent_seats

def process_seats(seats):
    new_situation = []
    height = len(seats)
    width = len(seats[0])

    for i in range(height):
        new_seat_row = ''
        for j in range(width):
            seat_status = seats[i][j]

            adjacent_people = list(filter(lambda x: x == '#', get_adjacent_seats2(i, j, seats)))

            if seat_status == 'L' and len(adjacent_people) == 0:
                new_seat_row += '#'
            elif seat_status == '#' and len(adjacent_people) >= 5:
                new_seat_row += 'L'
            else:
                new_seat_row += seat_status

        new_situation.append(new_seat_row)

    print()
    print('Processed seats')
    print()
    for seat_row in new_situation:
        print(seat_row)

    return new_situation

def unchanged_seats(old_seats, new_seats):
    unchanged = True
    for i in range(len(old_seats)):
        if old_seats[i] != new_seats[i]:
            unchanged = False
            break

    return unchanged

updatedSeats = process_seats(inputlines)
initial_seats = inputlines

while not unchanged_seats(initial_seats, updatedSeats):
    initial_seats = updatedSeats
    updatedSeats = process_seats(initial_seats)

taken_seats = sum([seat_row.count('#') for seat_row in updatedSeats])

print(taken_seats)
