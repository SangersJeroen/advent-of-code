from itertools import groupby
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import read_and_sanitize

def get_factors(length: int):
    factors: list[tuple[int, int]] = list()
    for i in range(1, length):
        num_sections = i + 1
        if length % num_sections == 0:
            section_length =  int(length / num_sections)
            factors.append((num_sections, section_length))
    return factors

def section(string: str, fractions: list[tuple[int, int]]) -> list[list[str]]:
    list_of_substring_list: list[list[str]] = []
    for frac in fractions:
        l: int = frac[1]
        substring_list: list[str] = list()
        for i in range(frac[0]):
            substring: str = string[l*i:l*(i+1)]
            substring_list.append(substring)
        list_of_substring_list.append(substring_list)
    return list_of_substring_list


def main(puzzle_input: list[str]) -> None:
    ranges: list[tuple[int, int]] = list()
    for r in puzzle_input[0].split(','):
        low, high = [int(i) for i in r.split('-')]
        ranges.append((low, high))

    sum: int = 0
    for r in ranges:
        for num in list(range(r[0], r[1]+1)):
            if (l :=len(str(num))) % 2 == 0:
                lstr = str(num)[:int(l/2)]
                rstr = str(num)[int(l/2):]
                if lstr == rstr:
                    # print(f'found {num} where {lstr}=={rstr}')
                    sum += num
    print(f'solution to part 1: {sum}')

    sum: int = 0
    for r in ranges:
        for num in list(range(r[0], r[1]+1)):
            factors: tuple[int, int] = get_factors(len(str(num)))
            sections: list[list[str]] = section(str(num), factors)
            for sec in sections:
                if all(list(map(lambda x: x == sec[0], sec))):
                    sum += num
                    # print(f'found {num} where {sec} worked')
                    break
    print(f'solution to part 2: {sum}')



if __name__ == "__main__":
    print(get_factors(10))
    main(puzzle_input=read_and_sanitize(day=2, test=False))
