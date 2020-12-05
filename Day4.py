import math
import re
from helpers import AoCHelper

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
        return re.search('^\d{4}$', value) and value.isdigit() and 1920 <= int(value) <= 2002
    elif key == 'iyr':
        return re.search('^\d{4}$', value) and value.isdigit() and 2010 <= int(value) <= 2020
    elif key == 'eyr':
        return re.search('^\d{4}$', value) and value.isdigit() and 2020 <= int(value) <= 2030
    elif key == 'hgt':
        return (re.search('^\d*cm$', value) and value.replace('cm', '').isdigit() and 150 <= int(value.replace('cm', '')) <= 193) \
               or (re.search('^\d*in$', value) and value.replace('in', '').isdigit() and 59 <= int(value.replace('in', '')) <= 76)
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
    # else:
    #     print("Invalid: " + p)

# print('True: ' + str(passportValidator('byr', '2002')))
# print('False: ' + str(passportValidator('byr', '2003')))
# print('True: ' + str(passportValidator('hgt', '60in')))
# print('True: ' + str(passportValidator('hgt', '190cm')))
# print('False: ' + str(passportValidator('hgt', '190in')))
# print('False: ' + str(passportValidator('hgt', '190')))
# print('True: ' + str(passportValidator('hcl', '#123abc')))
# print('False: ' + str(passportValidator('hcl', '#123abz')))
# print('False: ' + str(passportValidator('hcl', '123abc')))
# print('True: ' + str(passportValidator('ecl', 'brn')))
# print('False: ' + str(passportValidator('ecl', 'wat')))
# print('True: ' + str(passportValidator('pid', '000000001')))
# print('False: ' + str(passportValidator('pid', '0123456789')))






print(str(validPassports))