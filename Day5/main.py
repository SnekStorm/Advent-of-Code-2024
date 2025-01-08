import re
from operator import index
from re import findall, search, match
# Helpful tool: https://pythex.org/
from statistics import median
from typing import Dict, Any

def inDixt(list, my_dict, index):
    if list[len(list) -index - 1] in my_dict:
        if set(list[:len(list)-index - 1]).intersection(my_dict[list[len(list) -index - 1]]):
            return False
    return True

def checkNext(list, my_dict):
    for l in range(len(list)):
        if not inDixt(list, my_dict, l):
            return False
        #if list[len(list)-l-1] in my_dict:
           # if set(list[:len(list)-l-1]).intersection(my_dict[list[len(list)-l-1]]):
            #    return False
    return True

def fixPage(list, my_dict):
    while not checkNext(list[:], my_dict):
        for l in range(len(list)):
            x = set(list[:len(list)-l - 1]).intersection(my_dict[list[len(list) -l - 1]])
            removeItem = 0
            for item in x:
                tempSufixList = list[len(list)-l-removeItem:].copy()
                tempPrefixList = list[:len(list)-l-removeItem].copy()
                itemIndex = list.index(item)

                tempPrefixList.pop(itemIndex)
                tempSufixList.append(list[itemIndex])
                list = tempPrefixList + tempSufixList
                removeItem = removeItem + 1
            l = l + len(x)-1
    return list

def run():
    pageUpdate = []
    rules = []
    found = 0
    summa = 0
    summa2 = 0
    correctPages = []
    incorrectPages = []
    my_dict: dict[Any, Any] = {}
    with open("input.txt") as f:
        for line in f:
            rules.extend(findall(r'(\d+)\|(\d+)', line))
            if match(r'(\d+,)',line):
                pageUpdate.append(line.strip('\n').split(","))

    # Create dict for the rules
    for rule in rules:
        my_dict.setdefault(rule[0], [])
        my_dict[rule[0]].append(rule[1])


    for update in pageUpdate:
        temp_update = update[:]
        if checkNext(temp_update,my_dict):
            found += 1
            correctPages.append(update)
        else:
            incorrectPages.append(update)

    for p in correctPages:
        summa += int( p[round(((len(p)+1) / 2)-1)])


    print(f'{found}')
    print(f'{summa}')
    # Correct 5391

    #Part 2
    pageIndex = 0
    for update in incorrectPages:
        temp_copy = update[:]
        incorrectPages[pageIndex] = fixPage(update,my_dict)
        pageIndex = pageIndex + 1


    for p in incorrectPages:
        summa2 += int( p[round(((len(p)+1) / 2)-1)])

    print(summa2)
if __name__ == '__main__':
    run()