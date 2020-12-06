import re


def readInputLines(filename, linebreaks=False):
    if linebreaks:
        return [line for line in open("Inputs/" + filename)]
    else:
        return [line.rstrip('\n') for line in open("Inputs/" + filename)]


def readInputCommaLine(filename):
    lines = readInputLines(filename)
    return lines[0].split(',')


def readInputCommaLines(filename):
    lines = readInputLines(filename)

    lists = []

    for i in lines:
        lists.append(i.split(','))

    return lists


def prints(i):
    print(str(i))


def prod(ints):
    p = 1
    for i in ints:
        p *= int(i)
    return p


def listToString(listofstrings, separator=''):
    string = ''
    for l in listofstrings:
        string += (str(l) + separator)
    return string


def groupLines(inputlines):
    groups = []
    group = []

    for i in inputlines:
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
