import re
from itertools import count
from logging import logProcesses
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

class Block:
    def __init__(self, _id, _size, _moved):
        self.identifier = _id
        self.size = _size
        self.moved = _moved

class Space:
    def __init__(self, _elements, _OG_size, _current_size):
        self.elements = _elements
        self.OG_size = _OG_size
        self.current_size = _current_size

def run2():
    disk_map = ""
    disk_list = []
    space_list = []
    identifier = 0
    with open("input.txt") as f:
        for line in f:
            disk_map = line
            for i,c in enumerate(line):
                if i %2 == 0:
                    disk_list.append(Block(identifier, int(c), False))
                    identifier = identifier + 1
                else:
                    space_list.append(Space(0,int(c),int(c)))


    for _,d in enumerate(disk_list[::-1]):
        space_position = 0
        for i, space in enumerate(space_list):
            # Stop if move pointer is above itself
            if d.identifier <= i:
                break

            # Add value into list and change status to moved for the value that have been moved, so it doesn't get counted later
            if int(space.current_size) >= d.size:
                disk_list.insert(space_position+1+space.elements, Block(d.identifier, d.size, False))
                d.moved = True
                space.elements = space.elements +1
                space.current_size = space.current_size - d.size

                break
            else: space_position = space_position +1 + space.elements


    multi = 0
    result = 0
    data_pointer = 0
    space_pointer = 0
    for k, h in enumerate(disk_map):
        if data_pointer == len(disk_list):
            break
        if k%2 == 0:
            if not disk_list[data_pointer].moved:
                for v in range(disk_list[data_pointer].size):
                    result = result + disk_list[data_pointer].identifier * multi
                    multi = multi + 1
            else:
                for q in range(disk_list[data_pointer].size):
                    multi = multi + 1
            data_pointer = data_pointer+1
        else:
            if len(space_list) == space_pointer:
                continue

            for s in range(space_list[space_pointer].elements):
                for v in range(disk_list[data_pointer].size):
                    result = result + disk_list[data_pointer].identifier * multi
                    multi = multi + 1
                data_pointer = data_pointer+1

            for s in range(int(space_list[space_pointer].current_size)):
                multi = multi + 1
            space_pointer = space_pointer + 1

    # Too Low:  5040978786433
    # Correct:  6250605700557 -- Forgot to end when pointer was above value to move (:
    # Too High: 8446022420670
    print(f'Result: {result}')

# -------------------


if __name__ == '__main__':
    run2()