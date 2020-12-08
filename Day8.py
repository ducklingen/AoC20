from helpers.AoCHelper import *


def alterProgram(i, program):
    newProgram = [x for x in program]
    operation = program[i]

    if operation[0:3] == 'jmp':
        print("Changed position " + str(i))
        newProgram[i] = operation.replace('jmp', 'nop')
    elif operation[0:3] == 'nop':
        print("Changed position " + str(i))
        newProgram[i] = operation.replace('nop', 'jmp')

    return newProgram

def executeOperation(i, program, accumulator):
    if i >= len(program):
        print("Out of index")
        return accumulator, i

    operation = program[i]
    # print(operation)

    if operation[0:3] == 'acc':
        value = extract_numbers_from_line(operation)
        accumulator += value[0]
        i += 1
    elif operation[0:3] == 'jmp':
        value = extract_numbers_from_line(operation)
        i += value[0]
    else:
        i += 1

    if i == len(program) and operation[0:3] in ['acc', 'nop']:
        print('Program terminates')
        i -= 1

    return accumulator, i

def runprogram(currentLine, visitedLines, accumulator, program):
    while currentLine not in visitedLines:
        visitedLines.append(currentLine)
        accumulator, currentLine = executeOperation(currentLine, program, accumulator)

    return accumulator


inputlines = readInputLines('day8/day8input1.txt')

for i in range(len(inputlines)):
    a = 0
    c = 0
    v = []
    inputlines = readInputLines('day8/day8input1.txt')
    alteredProgram = alterProgram(i, inputlines)
    print(runprogram(c, v, a, alteredProgram))
