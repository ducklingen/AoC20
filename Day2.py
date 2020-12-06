import math
from helpers import AoCHelper
from helpers.AoCHelper import prints

validPasswords = 0
input = AoCHelper.readInputLines("day2/day2input1.txt")

def validPassword(input):
    range,char,password = input.split( )
    min, max = map(int, range.split('-'))

    character = char.replace(':','')

    return (list(password)[min-1] == character) ^ (list(password)[max-1] == character)

for i in input:
    if validPassword(i):
        validPasswords = validPasswords + 1

prints(validPasswords)
