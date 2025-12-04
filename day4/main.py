import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import read_and_sanitize
from lib.datastructures import Grid

def remove_rolls(grid: Grid, remove=False) -> tuple[int, Grid]:
    removable_rolls: int = 0
    # print('  WNEWEWSE')
    # print('  NNNWESSW')
    for i in range(grid.x_size):
        for j in range(grid.y_size):
            neighbours = grid.get_neighbours((i,j))
            number_rolls: int = neighbours.count('@')
            # print(grid[(i,j)], neighbours, number_rolls, number_rolls < 4, i, j)
            if grid[(i,j)] == '@' and number_rolls < 4:
                removable_rolls += 1
                if remove:
                    grid[(i,j)] = '.'
    return removable_rolls, grid


def main(puzzle_input: list[str]) -> None:
    grid = Grid(puzzle_input)
    # count removable
    removable_rolls, _ = remove_rolls(grid)
    print(f'Part 1: {removable_rolls} rolls removable')

    total_removed_rolls = 0
    while True:
        removed_rolls, grid = remove_rolls(grid, remove=True)
        total_removed_rolls += removed_rolls
        if removed_rolls == 0:
            break
    print(f'Part 2: {total_removed_rolls} rolls were removed')

if __name__ == "__main__":
    main(puzzle_input=read_and_sanitize(day=4, test=False))
