import re
from operator import index
from re import findall, search, match
# Helpful tool: https://pythex.org/
from statistics import median
from typing import Dict, Any
import math

def addList(post, pre, mul):
    result = 0
    numbers = post + pre
    numbers.append(mul)
    for l in numbers:
        result = result + l
    return result

def multList(numbers, singleNumber = 0) -> int:
    if len(numbers) == 0:
        return 0
    if len(numbers) == 1:
        return int(numbers[0])
    if numbers == 0:
        result = numbers[0]
    else:
        result = singleNumber
    for l in numbers[1:]:
        result = result * l
    return int(result)

def run():
    equations = []
    result = 0
    with open("input.txt") as f:
        for line in f:
            equations.append(line.strip('\n'))

    for equation in equations:
        found = False
        ttestReturn = 0
        answer = findall(r'(\d+):', equation)
        answer = int(answer[0])
        numbers = findall(r' (\d+)', equation)
        for i, n in enumerate(numbers):
            numbers[i] = int(n)


        for mu in range(len(numbers)):
            for j in range(len(numbers) - mu):
                ttestReturn = test(numbers[:], answer, mu, j)
                if ttestReturn == answer:
                    found = True

        if found:
            result = result + answer

    # to low: 4280115027739
            # 4280115047143
            # 4330577810019

    print(f'The total calibration amount: {result}')

def test(numbers, answer, mu, j):
    x = [sum(numbers[:j+1])]
    x.extend(numbers[j+1:])
    if x[0] == 0:
        x.pop(0)
    y = x[0]
    for m in range(mu):
        y = y * x[m+1]
    z = y + sum(x[mu+1:])
    return z


def runRecursion():
    equations = []
    number_of_found_q1 = 0
    total_calibration_result_q1 = 0
    number_of_found_q2 = 0
    total_calibration_result_q2 = 0
    with open("input.txt") as f:
        for line in f:
            equations.append(line.strip('\n'))

    for equation in equations:
        answer = findall(r'(\d+):', equation)
        answer = int(answer[0])
        numbers = findall(r' (\d+)', equation)


        if alg(0,numbers,answer, quest2= False):
            number_of_found_q1 = number_of_found_q1 +1
            number_of_found_q2 = number_of_found_q2 +1
            total_calibration_result_q1 = total_calibration_result_q1 + answer
            total_calibration_result_q2 = total_calibration_result_q2 + answer
        elif alg(0,numbers,answer, quest2= True):
            number_of_found_q2 = number_of_found_q2 +1
            total_calibration_result_q2 = total_calibration_result_q2 + answer

    print(f'Quest 1: From {number_of_found_q1} correct calibrations gives the Calibration result: {total_calibration_result_q1}.')
    print(f'Quest 2: From {number_of_found_q2} correct calibrations gives the Calibration result: {total_calibration_result_q2}.')
    # Quest 1: 5837374519342 from 356
    # Quest 2: 492383931650959 from 541

def alg(current:int, rest, answer:int, quest2, found = False):
    if len(rest) == 0:
        if current == answer:
            return True
        else:
            return False

    # Early return if value will be too high
    if current > answer:
        return False
    if len(rest) > 0:
        if int(rest[0]) > answer:
            return False

    if quest2:
        # Try || combining
        if len(rest) > 0:
            if current != 0:
                compact = str(current) + rest[0]
            else:
                compact = rest[0]
            if alg(int(compact), rest[1:], answer, quest2, found):
                return True


    # Try Add
    addition = current + int(rest[0])
    if alg(addition, rest[1:], answer, quest2):
        return True

    # Try multi
    if current == 0:
        multiplication = 1 * int(rest[0])
    else:
        multiplication = current * int(rest[0])
    if alg(multiplication, rest[1:], answer, quest2):
        return True


    return False

if __name__ == '__main__':
    runRecursion()