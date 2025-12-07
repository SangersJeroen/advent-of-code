import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import read_and_sanitize
from lib.datastructures import Grid


def main(puzzle_input: list[str]) -> None:
    grid = Grid(puzzle_input)
    grid.plot()
    print()
    grid.propagate()
    grid.plot()
    print(grid.splits)
    print(grid.sum_beams())


if __name__ == "__main__":
    main(puzzle_input=read_and_sanitize(day=7, test=False))
