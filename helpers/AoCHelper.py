def readInputLines(fileName):
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
