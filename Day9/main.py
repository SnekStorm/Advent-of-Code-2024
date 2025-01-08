import re
from operator import index
from re import findall, search, match
# Helpful tool: https://pythex.org/
from statistics import median
from typing import Dict, Any
import math

def run():
    disk_map = ""
    disk_list = []
    data_index = 0


    with open("input.txt") as f:
        for line in f:
            disk_map = line.strip('\n')

    total_index = int((len(disk_map)-1)/2)

    for i, data in enumerate(disk_map):
        # All data is handled when both indexes meet
        if data_index > total_index:
            break

        if i % 2 == 0:
            # Add data space
            for amount in range(int(disk_map[i])):
                disk_list.append(str(data_index))
            data_index = data_index + 1
        else:
            # Fill empty space with data from back
            for amount in range(int(disk_map[i])):
                disk_list.append(str(total_index))
                # Remove one unit from last value
                disk_map = disk_map[:-1] + str( int(disk_map[-1]) - 1)
                # If last value is 0 remove it from list and the free space
                if int(disk_map[len(disk_map)-1]) < 1:
                    total_index = total_index -1
                    disk_map = disk_map[:-2]

    result = 0
    for i, id_number in enumerate(disk_list):
        result = result + (i * int(id_number))

    print(f'Checksum: {result}')

def move_data(location, data):
    x = ''
    rest = ''
    y = list(data)

    for i,u in enumerate(y):
        x.join(u)

    for q in range(len(x)-len(data)):
        rest = rest + '.'

    return x, rest

def run2():
    disk_map = ""
    disk_list = []
    data_index = 0


    with open("dummy.txt") as f:
        for line in f:
            for i, digit in enumerate(line):
                x = ''
                if i % 2 == 0:
                    for amount in range(int(digit)):
                        x = x +(str(data_index))
                    disk_list.append(x)
                    data_index = data_index + 1
                else:
                    for amount in range(int(digit)):
                        x = x + '.'
                    disk_list.append(x)


    print(f'List: {disk_list}')

    move_index = len(disk_list)


    for space_index,i in enumerate(disk_list):
        if i[0] == '.':
            for n, j in enumerate(disk_list[:move_index].reverse()):
                if j[0] != '.':
                    if len(j) <= len(i):
                        disk_list = disk_list[:space_index] + move_data(i,j) + disk_list[:space_index+1]



    '''
    empty_space = int(disk_map[i])
            for d in disk_map[:move_index+1]:
                if move_index <= 0:
                    break
                if empty_space >= int(disk_map[move_index]):
                    for amount in range(int(disk_map[move_index])):
                        disk_list.append(str(total_index))
                    disk_map = disk_map[:move_index] + '0' + disk_map[move_index+1:]

                    move_index = move_index - 2
                    total_index = total_index -1
                    break
                else:
                    move_index = move_index - 2
                    total_index = total_index -1
    '''



if __name__ == '__main__':
    run2()