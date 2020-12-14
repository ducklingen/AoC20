import copy
import sys
import math
from itertools import combinations_with_replacement, permutations

from helpers.AoCHelper import *
from helpers.GlobalVariables import *

sys.setrecursionlimit(5000)

input_lines = read_input_lines('day14/day14input1.txt')

mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
memory = {}


def decimal_to_binary(n, expand=False):
    if expand:
        binary = bin(n).replace("0b", "")
        leading_zeros = 36-len(binary)
        return '0'*leading_zeros + binary
    else:
        return bin(n).replace("0b", "")


def update_mask(old_mask, new_mask):
    mask = ''
    for i in range(len(new_mask)):
        if new_mask[i] != '0':
            mask += new_mask[i]
        else:
            mask += old_mask[i]

    return mask


def get_all_combinations(list, size_of_tuples):
    combination_set = set()
    for i in combinations_with_replacement(list, size_of_tuples):
        for j in permutations(i):
            combination_set.add(j)

    return combination_set


def write_to_adresses(value, position, mask):
    position_as_binary = decimal_to_binary(position,True)
    masked_position = update_mask(position_as_binary, mask)

    for comb in get_all_combinations([0,1], masked_position.count('X')):
        idx = 0
        new_position = ''
        for i in range(len(mask)):
            if masked_position[i] == 'X':
                new_position += str(comb[idx])
                idx += 1
            else:
                new_position += masked_position[i]

        print("Writing " + str(value) + " to " + str(new_position))
        memory[new_position] = value


for i in input_lines:
    if i[:3] == 'mem':
        position, value = extract_numbers_from_line(i)
        value_as_binary = decimal_to_binary(value,True)
        # print(value_as_binary)
        # print(mask)
        # masked_value = update_mask(value_as_binary, mask)
        # print(masked_value)
        # print(int(masked_value, 2))

        write_to_adresses(value, position, mask)
    else:
        # print("Mask: " + mask)
        # print("Update: " + i[7:])
        mask = i[7:]
        # print("Resulting mask: " + mask)

p1 = sum(memory.values())
print(p1)