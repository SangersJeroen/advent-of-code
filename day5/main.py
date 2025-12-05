import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import read_and_sanitize
from lib.datastructures import NumberRanges


def main(puzzle_input: list[str]) -> None:
    # Input splitting
    empty_line_index: int = puzzle_input.index('')

    range_str: list[str] = puzzle_input[:empty_line_index]
    ingredients: list[str] = puzzle_input[empty_line_index+1:]

    # Part 1
    ranges: list[range] = []
    for r in range_str:
        low, high = (int(i) for i in r.split('-'))
        ranges.append(range(low, high+1))

    fresh: int = 0
    for ingredient in ingredients:
        i = int(ingredient)
        for r in ranges:
            if i in r:
                fresh += 1
                break
    print(f"Number of fresh ingredients: {fresh}")

    # Part 2
    nrange = NumberRanges(range_str[0])
    for i in range(len(range_str)-1):
        nrange + range_str[i+1]
    print(nrange.count())



if __name__ == "__main__":
    main(puzzle_input=read_and_sanitize(day=5, test=False))
