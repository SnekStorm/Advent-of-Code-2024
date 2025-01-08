import re
from operator import index
from re import findall, search, match
# Helpful tool: https://pythex.org/
from statistics import median
from typing import Dict, Any

def orientation(guard):
    if guard == '^':
        return [-1,0]
    if guard == '<':
        return [0,-1]
    if guard == '>':
        return [0,1]
    if guard == 'v':
        return [1,0]

    return [0,0]

def canMove(theMap, position, move):

    newP = [position[0]+move[0], position[1]+move[1]]
    if newP[0] < 0 or newP[1] < 0:
        return 2
    elif newP[0] > len(theMap[0])-1 or newP[1] > len(theMap)-1:
        return 2

    if theMap[newP[0]][newP[1]] == '.':
        return 1
    else:
        return 0

def turnRight(guard):
    if guard == '^':
        guard = '>'
    elif guard == '<':
        guard = '^'
    elif guard == '>':
        guard = 'v'
    elif guard == 'v':
        guard = '<'

    return guard

def run():
    theMap = []
    position = list[int, int]
    move = list[1,0]
    visited_places = set()
    with open("input.txt") as f:
        for line in f:
            theMap.append(list(line.strip('\n')))

    for y, line in enumerate(theMap):
        for x, item in enumerate(line):
            if item == '^':
                position = [y,x]
                break
    print(f'Guards\' start position: {position}')
    can_move = 0
    while can_move != 2:
        move = orientation(theMap[position[0]][position[1]])
        can_move = canMove(theMap, position, move)
        if can_move == 1:
            visited_places.add(str([position[0]]) + ',' + str([position[1]]))
            position[0] = position[0]+move[0]
            position[1] = position[1]+move[1]
            theMap[position[0]][position[1]] = theMap[position[0] - move[0] ][position[1] - move[1]]
            theMap[position[0] - move[0] ][position[1] - move[1]] = '.'
            #visited_places.add(str([position[0]]) + ',' + str([position[1]]))

        elif can_move == 0:
            theMap[position[0]][position[1]] = turnRight(theMap[position[0]][position[1]])

    print(f'The amount of unique visited places: {len(visited_places)}')  #5553


def run2():
    guardRoute = []
    found = 0
    start_position = list[int, int]
    move = list[1, 0]
    visited_places = set()
    with open("input.txt") as f:
        for line in f:
            guardRoute.append(list(line.strip('\n')))

    for y, line in enumerate(guardRoute):
        for x, item in enumerate(line):
            if item == '^':
                start_position = [y, x]
                break
    print(f'Guards\' start position: {start_position}')

    new_obstecal = [0,0]
    for iq, q in enumerate(guardRoute):
        for iw, w in enumerate(q):
            #theMap = guardRoute.copy()
            theMap = [ele[:] for ele in guardRoute]
            position = start_position.copy()
            visited_places.clear()
            new_obstecal = [iq, iw]
            storeSquare = theMap[iq][iw]
            if position[0] == iq and position[1] == iw:
                continue
            theMap[iq][iw] = '0'
            can_move = 0
            while can_move != 2:
                move = orientation(theMap[position[0]][position[1]])
                can_move = canMove(theMap, position, move)
                if can_move == 1:
                    visited_places.add(str([position[0]]) + ',' + str([position[1]]) +','+ theMap[position[0]][position[1]])
                    position[0] = position[0] + move[0]
                    position[1] = position[1] + move[1]
                    theMap[position[0]][position[1]] = theMap[position[0] - move[0]][position[1] - move[1]]
                    theMap[position[0] - move[0]][position[1] - move[1]] = '.'
                    #visited_places.add(str([position[0]]) + ',' + str([position[1]]) +','+ theMap[position[0]][position[1]])

                elif can_move == 0:
                    theMap[position[0]][position[1]] = turnRight(theMap[position[0]][position[1]])

                if str( str([position[0]])+','+str([position[1]]) +','+theMap[position[0]][position[1]]) in visited_places:
                    found = found + 1
                    can_move = 2

            print(f'The amount of unique visited places: {len(visited_places)}')
            #theMap[iq][iw] = storeSquare

    print(f'The amount of loops: {found}') #1928

if __name__ == '__main__':
    run()