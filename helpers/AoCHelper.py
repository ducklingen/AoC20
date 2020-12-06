import re

def readInputLines(fileName, linebreaks = False):
    if linebreaks:
        return [line for line in open("Inputs/" + fileName)]
    else:
        return [line.rstrip('\n') for line in open("Inputs/" + fileName)]


def readInputCommaLine(fileName):
    lines = readInputLines(fileName)
    return lines[0].split(',')


def readInputCommaLines(fileName):

    lines = readInputLines(fileName)

    lists = []

    for i in lines:
        lists.append(i.split(','))

    return lists


def prints(i):
    print(str(i))


def prod(ints):
    p = 1
    for i in ints:
        p*=int(i)
    return p


def listToString(list, separator = ''):
    string = ''
    for l in list:
        string += (str(l) + separator)
    return string


def groupLines(input):
    groups = []
    group = []

    for i in input:
        if i == '':
            groups.append(group)
            group = []
        else:
            group.append(i)

    groups.append(group)

    return groups


def extract_numbers_from_line(line):
    pattern = r'((?<!\d)[+-]?)(\d+)'
    return [int(match.group()) for match in re.finditer(pattern, line)]


def extract_numbers(lines):
    return [extract_numbers_from_line(line) for line in lines]