from helpers.AoCHelper import *

inputlines = readInputLines('day8/day8input1.txt')

def alterProgram(i, program):
    newProgram = [x for x in program]
    operation = program[i]

    if operation[0:3] == 'jmp':
        newProgram[i] = operation.replace('jmp', 'nop')
    elif operation[0:3] == 'nop':
        newProgram[i] = operation.replace('nop', 'jmp')

    return newProgram

def executeOperation(i, operation, accumulator):
    if operation[0:3] == 'acc':
        accumulator += extract_numbers_from_line(operation)[0]
        i += 1
    elif operation[0:3] == 'jmp':
        i += extract_numbers_from_line(operation)[0]
    else:
        i += 1

    return accumulator, i


def runprogram(program):
    current_line, accumulator, visited_lines, terminated = [0, 0, [], False]

    while current_line not in visited_lines and current_line < len(program):
        visited_lines.append(current_line)
        accumulator, current_line = executeOperation(current_line, program[current_line], accumulator)

    if current_line >= len(program):
        terminated = True

    return accumulator, terminated

# Part 1
assert runprogram(inputlines)[0] == 1744
print("Part 1: " + str(runprogram(inputlines)[0]))

# Part 2
for i in range(len(inputlines)):
    a, terminated = runprogram(alterProgram(i, readInputLines('day8/day8input1.txt')))

    if terminated:
        assert a == 1174
        print("Part 2: " + str(a))
        break