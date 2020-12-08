from helpers.AoCHelper import *

inputlines = readInputLines('day8/day8input1.txt')

def alterProgram(index, program):
    newProgram = [x for x in program]
    operation = program[index]

    if operation[0:3] == 'jmp':
        newProgram[index] = operation.replace('jmp', 'nop')
    elif operation[0:3] == 'nop':
        newProgram[index] = operation.replace('nop', 'jmp')

    return newProgram

def executeOperation(index, operation, accumulator):
    if operation[0:3] == 'acc':
        accumulator += extract_numbers_from_line(operation)[0]
        index += 1
    elif operation[0:3] == 'jmp':
        index += extract_numbers_from_line(operation)[0]
    else:
        index += 1

    return accumulator, index


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
    accumulator, terminated = runprogram(alterProgram(i, readInputLines('day8/day8input1.txt')))

    if terminated:
        assert accumulator == 1174
        print("Part 2: " + str(accumulator))
        break