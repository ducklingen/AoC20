import math
from helpers import AoCHelper
from helpers.AoCHelper import prints

input = AoCHelper.readInputLines("day2/day2input1.txt")
validPasswords = 0

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
    if validPassword1(i):
        validPasswords = validPasswords + 1

print("Part 1: " + str(validPasswords))
validPasswords = 0

for i in input:
    if validPassword2(i):
        validPasswords = validPasswords + 1

print("Part 2: " + str(validPasswords))
