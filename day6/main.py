from functools import reduce
import sys
import os
from typing import Any, Callable

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import read_and_sanitize

mapping: dict[str, Callable] = {
    '*': lambda x: reduce(lambda a, b: a * b, x),
    '+': lambda x: reduce(lambda a, b: a + b, x),
}


def delete_ws(row):
    non_ws_row: list[int] = list()
    for i in row:
        if i == ' ' or i == '':
            continue
        else:
            non_ws_row.append(i)
    return non_ws_row

def list_split(input: list[Any], split_on = '') -> list[list[Any]]:
    output = []
    buffer = []
    for val in input:
        if val != split_on:
            buffer.append(val)
        else:
            output.append(buffer)
            buffer = list()
    output.append(buffer)
    return output


# def main(puzzle_input: list[str]) -> None: # part 1
#     operations: list[str] = []
#     numbers: list[list[int]] = []
#     operations = delete_ws(puzzle_input.pop(-1))
#
#     for row in puzzle_input:
#         row_num = delete_ws(row.split(' '))
#         for ii, num in enumerate(row_num):
#             try:
#                 numbers[ii].append(int(num))
#             except IndexError:
#                 numbers.append(list())
#                 numbers[ii].append(int(num))
#
#     sum = 0
#     for ii, exc in enumerate(operations):
#         sum += mapping[exc](numbers[ii])
#     print(f"Solution for part 1: {sum}")

def main(puzzle_input: list[str]) -> None: # part 2
    row_length = len(puzzle_input[0])
    operations = []
    numbers = []
    for ii in range(0, row_length, 1):
        ii = row_length - ii - 1
        column = [row[ii] for row in puzzle_input]
        number_str = ''.join(delete_ws(column[:-1]))
        if number_str == "":
            numbers.append('')
        else:
            number = int(number_str)
            numbers.append(number)
            if column[-1] in ['*', '+']:
                operations.append(column[-1])

    split_numbers = list_split(numbers)
    print(split_numbers, operations)
    sum = 0
    for operation, operand in zip(operations, split_numbers):
        sum += mapping[operation](operand)
    print(sum)


if __name__ == "__main__":
    main(puzzle_input=read_and_sanitize(day=6, test=False))
