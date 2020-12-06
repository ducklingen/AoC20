import math
import re
from helpers import AoCHelper
from helpers.AoCHelper import prints

input = AoCHelper.readInputLines("day4/day4input1.txt")

requiredKeys = ['byr', 'iyr', 'eyr', 'hgt', 'ecl', 'hcl', 'pid']

validPassports = 0
passports = []
passport = ""

for i in input:
    if i == '':
        passports.append(passport)
        passport = ''
    else:
        passport += (i + ' ')

passports.append(passport)

def passportValidator(key, value):
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
        for f in fields:
            if f == '':
                continue

            a,b = f.split(':')

            if validPassport:
                validPassport = passportValidator(a, b)

    if validPassport:
        print(p)
        validPassports += 1

prints(validPassports)