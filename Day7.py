from helpers.AoCHelper import *

inputlines = readInputLines('day7/day7input1.txt')

specialbag = 'shiny gold bag'

bags = {}
bagsWithShinyGold = 0

for i in inputlines:
    i = i.replace('bags', 'bag').replace('.', '')
    container, indhold = i.split(' contain ')
    indholdsliste = []
    for j in indhold.split(', '):
        if j == 'no other bag':
            break

        list = j.split(' ')
        indholdsliste.append((list[0], listToString(list[1:], ' ').strip()))

    bags[container] = indholdsliste


def containsShinyGold(baglist, bags, parentbags):
    contains = False
    for bag in baglist:
        if bag[1] == specialbag:
            print(listToString(parentbags, ' -> ') + specialbag)
            # print(parentbags[-1:])
            contains = True
            break

    if not contains:
        for bag in baglist:
            parentage = parentbags
            parentage.append(bag[1])
            contains = containsShinyGold(bags[bag[1]], bags, parentage)
            if contains:
                break

    return contains

def containsNumberOfBags(baglist, bags):
    bagsContained = 0
    for bag in baglist:
        bagsContained += int(bag[0]) + int(bag[0])*containsNumberOfBags(bags[bag[1]], bags)

    return bagsContained

print(containsNumberOfBags(bags['shiny gold bag'], bags))

# for bag in bags:
#     if containsShinyGold(bags[bag], bags, [bag]):
#         # print(bag)
#         bagsWithShinyGold += 1

print(bagsWithShinyGold)
