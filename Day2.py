import math
from helpers import AoCHelper

validPasswords = 0
input = AoCHelper.readInputLines("day2/day2input1.txt")

def validPassword(input):
    parts = input.split( )
    minOccurence = int(parts[0].split('-')[0])
    maxOccurence = int(parts[0].split('-')[1])

    character = parts[1].replace(':','')

    return (list(parts[2])[minOccurence-1] == character) ^ (list(parts[2])[maxOccurence-1] == character)

for i in input:
    if validPassword(i):
        validPasswords = validPasswords + 1

print(str(validPasswords))
