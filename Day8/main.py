import re
from operator import index
from re import findall, search, match
# Helpful tool: https://pythex.org/
from statistics import median
from typing import Dict, Any
import math
def dict_entry(dict, key, value ):
    if key not in dict:
        dict.setdefault(key, [])
    dict[key].append(value)

def run():
    antenna_map = []
    amount_of_nodes = 0

    filter_patters = r'[a-z]|[A-Z]|\d'

    node_dict: dict[Any, Any] = {}
    antinode_cord = set()

    with open("input.txt") as f:
        for line in f:
            antenna_map.append(list(line.strip('\n')))

    for y, row in enumerate(antenna_map):
        for x, column in enumerate(row):
            if re.match(filter_patters, column):
                #print(f'Node: {antenna_map[y][x]}, found in coordinates: x:{x}, y:{y}')
                dict_entry(node_dict,antenna_map[y][x], [y,x])
                amount_of_nodes = amount_of_nodes + 1
    print(f'Amount of Nodes: {amount_of_nodes}')

    for key in node_dict.keys():
        for element in range(len(node_dict[key])):
            current_element = node_dict[key][element]
            for cord in node_dict[key]:
                new_y_cord = current_element[0] + (current_element[0]-cord[0])
                new_x_cord = current_element[1] + (current_element[1]-cord[1])
                if current_element[0] == cord[0] and current_element[1] == cord[1]:
                    continue

                if 0 <= new_y_cord < len(antenna_map[0]):
                    if 0 <= new_x_cord < len(antenna_map[0]):

                        antinode_cord.add(str(new_y_cord) + ',' + str(new_x_cord))

    print(f'Amount of antinodes: {len(antinode_cord)}')
    antinode_cord.clear()

    for key in node_dict.keys():
        for element in range(len(node_dict[key])):
            current_element = node_dict[key][element]
            for cord in node_dict[key]:
                # Skip loop if same value
                if current_element[0] == cord[0] and current_element[1] == cord[1]:
                    continue
                move = True
                change_y_cord = (current_element[0]-cord[0])
                change_x_cord = (current_element[1]-cord[1])
                new_y_cord = current_element[0]
                new_x_cord = current_element[1]
                while move:

                    antinode_cord.add(str(new_y_cord) + ',' + str(new_x_cord))

                    new_y_cord = new_y_cord + change_y_cord
                    new_x_cord = new_x_cord + change_x_cord
                    if 0 > new_y_cord or new_y_cord > len(antenna_map[0])-1:
                        move = False
                    if 0 > new_x_cord or new_x_cord > len(antenna_map[0])-1:
                        move = False

                    #if re.match(filter_patters, antenna_map[new_y_cord][new_x_cord]):




    print(f'Amount of Harmonics antinodes: {len(antinode_cord)}')
    # To high: 1240
    # Correct: 1157
    # To low: 1060, 1064
if __name__ == '__main__':
    run()