import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import read_and_sanitize
from lib.datastructures import Dial


def main(puzzle_input: list[str]) -> None:
    dial = Dial()
    for line in puzzle_input:
        direction, clicks = line[0], int(line[1:])
        if direction == 'L':
            dial.left(clicks)
        elif direction == 'R':
            dial.right(clicks)
        else:
            raise RuntimeError('Should be unreachable')

    password = dial.history.count(0)
    print(f'Password is {password}')
    password_2 = dial.exact_history.count(0)
    print(f'password is {password_2}')

if __name__ == "__main__":
    main(puzzle_input=read_and_sanitize(day=1, test=False))
