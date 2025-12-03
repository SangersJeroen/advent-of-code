from aoc_lib import read_file
from time import time_ns
from functools import lru_cache, cache
# from numba import njit, jit
# from numba.types import int64, List

# @jit(List(int64)(int64))
@cache
def blink(stone: int) -> list[int]:

    if stone == 0:
        return [1]

    elif len(str(stone)) % 2 == 0:
        sv = str(stone)
        mid_idx = len(sv)//2
        left = sv[:mid_idx]
        right = sv[mid_idx:]
        return [int(left), int(right)]

    return [stone*2024]


def blink_stone_n_times(stone: int, n: int) -> list[int]:
    row: list[int] = [stone]
    iter: int = 0
    while iter < n:
        new_row: list[int] = []
        while len(row) > 0:
            stone = row.pop(0)
            new_stones: list[int] = blink(stone)
            for new_stone in new_stones:
                new_row.append(new_stone)
        row = new_row
        iter += 1
    return row


# @jit(int64(int64, int64))
@cache
def blink_stone_n_times_optimised(stone: int, n: int) -> int:

    if n == 0:
        return 1

    num_stones: int = 0
    new_stones: list[int] = blink(stone)
    for stone in new_stones:
        num_stones += blink_stone_n_times_optimised(stone, n-1)

    return num_stones


if __name__ == '__main__':
    rows: list[str] = [i.rstrip('\n') for i in open(r'inputs/d11.txt', 'r').readlines()]
    row: list[int] = [int(stone) for row in rows for stone in row.split()]
    N: int = 75

    start = time_ns()
    score: int = 0
    for ii in range(len(row)):
        stone = row[ii]
        # out_stone = blink_stone_n_times(stone, N)
        # score += len(out_stone)
        score += blink_stone_n_times_optimised(stone, N)
        print(f"finished {ii+1}/{len(row)}")
    print(f'computation took: {(time_ns() - start)/1e9:.2f} seconds')

    print(score)
