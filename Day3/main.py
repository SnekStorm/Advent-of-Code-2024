import re
from re import findall
# Helpful tool: https://pythex.org/

def run():
    matches = []
    condition_matches = []
    sumOfMux = 0
    con_sumOfMux = 0
    writeBool = True
    with open("input.txt") as f:
        for line in f:
            matches.extend( findall(r"mul\((\d{1,3}),(\d{1,3})\)", line))
            condition_matches.extend( findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", line))

    for mul in matches:
        sumOfMux += int( mul[0] ) * int( mul[1])

    for con_mul in condition_matches:
        if con_mul[3] == "don't()":
            writeBool = False
        elif con_mul[2] == "do()":
            writeBool = True
        elif writeBool:
            con_sumOfMux += int(con_mul[0]) * int(con_mul[1])


    print( f'Sum of all Mul operators: {sumOfMux}')
    print( f'Sum of conditional Mul: {con_sumOfMux}')

if __name__ == '__main__':
    run()