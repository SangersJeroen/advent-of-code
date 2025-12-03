from functools import reduce
import sys
import os
from itertools import chain, combinations

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import read_and_sanitize


def max_digit(string: str, leave: int) -> tuple[int, str]:
    take = slice(None, None, None)
    if leave != 0:
        take = slice(None, -leave, None)
    digits: list[int] = [int(i) for i in string[take]]
    # print(string, leave, digits)
    max_digit: int = -1
    loc_digit: int = -1
    for loc, digit in enumerate(digits):
        if digit > max_digit:
            max_digit = digit
            loc_digit = loc
    return (max_digit, string[loc_digit+1:])


def maximise_joltage(string: str, take: int = 2):
    joltage: str = ''
    d: int
    rem: str = string
    while take > 0:
        d, rem = max_digit(rem, leave=take-1)
        take -= 1
        joltage += str(d)
    return int(joltage)


def main(puzzle_input: list[str]) -> None:
    part1_sum = 0
    part2_sum = 0
    for line in puzzle_input:
        part1_sum += maximise_joltage(line)
        part2_sum += maximise_joltage(line, take=12)

    print(f'part 1 solutions is: {part1_sum}')
    print(f'part 2 solutions is: {part2_sum}')

if __name__ == "__main__":
    main(puzzle_input=read_and_sanitize(day=3, test=False))
