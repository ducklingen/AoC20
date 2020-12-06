import math
import re
from helpers import AoCHelper
from helpers.AoCHelper import prints, groupLines, listToString

input = AoCHelper.readInputLines("day4/day4input1.txt")
passports = [listToString(l, ' ') for l in groupLines(input)]

requiredKeys = ['byr', 'iyr', 'eyr', 'hgt', 'ecl', 'hcl', 'pid']

validPassports = 0
passportsWithRequiredKeys = 0

def passportFieldValidator(key, value):
    if key == 'byr':
        return 1920 <= int(value) <= 2002
    elif key == 'iyr':
        return 2010 <= int(value) <= 2020
    elif key == 'eyr':
        return 2020 <= int(value) <= 2030
    elif key == 'hgt':
        return (re.search('^\d*cm$', value) and 150 <= int(value.replace('cm', '')) <= 193) \
               or (re.search('^\d*in$', value) and 59 <= int(value.replace('in', '')) <= 76)
    elif key == 'hcl':
        return bool(re.search('^#[0-9a-f]{6}', value))
    elif key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif key == 'pid':
        return bool(re.search('^\d{9}$', value))
    elif key == 'cid':
        return True
    else:
        return False


for p in passports:
    validPassport = True
    fields = p.split(' ')
    fieldKeys = []

    for f in fields:
        fieldKeys.append(f.split(':')[0])

    for k in requiredKeys:
        if k not in fieldKeys:
            validPassport = False

    if validPassport:
        passportsWithRequiredKeys += 1
        for f in fields:
            if f == '':
                continue

            a,b = f.split(':')

            if validPassport:
                validPassport = passportFieldValidator(a, b)

    if validPassport:
        validPassports += 1

print("Part 1: " + str(passportsWithRequiredKeys))
print("Part 2: " + str(validPassports))