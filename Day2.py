import math
from helpers import AoCHelper
from helpers.AoCHelper import prints

input = AoCHelper.readInputLines("day2/day2input1.txt")
validPasswords1 = 0
validPasswords2 = 0


def validPassword1(input):
    range, char, password = input.split( )
    min, max = map(int, range.split('-'))
    character = char.replace(':', '')

    return min <= password.count(character) <= max


def validPassword2(input):
    range, char, password = input.split( )
    first, second = map(int, range.split('-'))
    character = char.replace(':', '')

    return (list(password)[first-1] == character) ^ (list(password)[second-1] == character)


for i in input:
    validPasswords1 += validPassword1(i)
    validPasswords2 += validPassword2(i)

assert validPasswords1 == 538
print("Part 1: " + str(validPasswords1))
assert validPasswords2 == 489
print("Part 2: " + str(validPasswords2))
