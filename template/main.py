import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import read_and_sanitize


def main(puzzle_input: list[str]) -> None:
    pass

if __name__ == "__main__":
    main(puzzle_input=read_and_sanitize(day=1, test=False))
