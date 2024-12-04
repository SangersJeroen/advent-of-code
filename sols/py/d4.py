from aoc_lib import read_file, parse_to_lists
from typing import Any, Iterable, Self
import re


class Vec:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def __add__(self, other: Self) -> Self:
        return Vec(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return f"(x;y):({self.x};{self.y})"

    def __mul__(self, mul: int) -> Self:
        return Vec(self.x * mul, self.y * mul)


class Field:
    def __init__(self, content: Iterable, shape: tuple[int, int]):
        self.dim0_len: int = shape[0]
        self.dim1_len: int = shape[1]
        self.data: Any = content

    def __len__(self):
        return self.dim0_len

    def shape(self) -> tuple[int, int]:
        return (self.dim0_len, self.dim1_len)

    def get(self, dim0_idx: int, dim1_idx: int) -> Any:
        if dim0_idx >= self.dim0_len or dim1_idx >= self.dim1_len:
            return "-"
        if dim0_idx < 0 or dim1_idx < 0:
            return "-"
        index: int = dim0_idx * (self.dim0_len) + dim1_idx
        return self.data[index]

    def __getitem__(self, vec: Vec) -> Any:
        dim0_idx = vec.x
        dim1_idx = vec.y
        return self.get(dim0_idx, dim1_idx)


DIRECTIONS: dict[str, Vec] = {
    "NN": Vec(-1, +0),
    "EE": Vec(+0, +1),
    "SS": Vec(+1, +0),
    "WW": Vec(+0, -1),
    "NE": Vec(-1, +1),
    "SE": Vec(+1, +1),
    "SW": Vec(+1, -1),
    "NW": Vec(-1, -1),
}


def test_directions(field: Field, pos: tuple[int, int]) -> tuple[bool, list[str]]:
    ii, jj = pos
    char: str = field.get(ii, jj)
    curr_pos: Vec = Vec(ii, jj)

    debug = False
    if (ii == 0) and (jj == 47):
        debug = True

    found_dirs: list[str] = []
    if char == "X":
        for direction in DIRECTIONS.keys():
            characters_in_direction: str = "X"
            for dd in range(3):
                off: Vec = DIRECTIONS[direction] * (dd + 1)
                new_char = field[curr_pos + off]
                if new_char != ["M", "A", "S"][dd]:
                    break
                else:
                    characters_in_direction += new_char
            if debug:
                print(curr_pos + off, direction, characters_in_direction)
            if characters_in_direction == "XMAS":
                found_dirs.append(direction)

    if len(found_dirs) > 0:
        return (True, found_dirs)
    return (False, [])


def find_xmas_in_field(field: Field) -> int:
    (yy, xx) = field.shape()

    count: int = 0
    for ii in range(yy):
        for jj in range(xx):
            res = test_directions(field, (ii, jj))
            if res[0]:
                # print((ii,jj), res[1])
                assert (ii, jj) in KNOWN_GOOD, f"({ii},{jj}) not in KNOWN_GOOD"
                count += len(res[1])
    return count


def find_diag_mas_in_field(field: Field) -> int:
    (yy, xx) = field.shape()

    count: int = 0
    for ii in range(yy):
        for jj in range(xx):
            pos = Vec(ii, jj)
            if field[pos] == "A" and (
                (
                    (
                        (
                            field[pos + DIRECTIONS["NE"]] == "S"
                            and field[pos + DIRECTIONS["SW"]] == "M"
                        )
                        or (
                            field[pos + DIRECTIONS["SW"]] == "S"
                            and field[pos + DIRECTIONS["NE"]] == "M"
                        )
                    )
                    and (
                        (
                            field[pos + DIRECTIONS["NW"]] == "S"
                            and field[pos + DIRECTIONS["SE"]] == "M"
                        )
                        or (
                            field[pos + DIRECTIONS["NW"]] == "M"
                            and field[pos + DIRECTIONS["SE"]] == "S"
                        )
                    )
                )
                or (
                    (
                        (
                            field[pos + DIRECTIONS["NN"]] == "S"
                            and field[pos + DIRECTIONS["SS"]] == "M"
                        )
                        or (
                            field[pos + DIRECTIONS["NN"]] == "M"
                            and field[pos + DIRECTIONS["SS"]] == "S"
                        )
                    )
                    and (
                        (
                            field[pos + DIRECTIONS["WW"]] == "S"
                            and field[pos + DIRECTIONS["EE"]] == "M"
                        )
                        or (
                            field[pos + DIRECTIONS["WW"]] == "M"
                            and field[pos + DIRECTIONS["EE"]] == "S"
                        )
                    )
                )
            ):
                count += 1
    return count


if __name__ == "__main__":
    contents = read_file(r"inputs/d4test.txt")
    contents = read_file(r"inputs/d4.txt")
    ax0 = len(contents)
    ax1 = len(contents[0])
    # print('   '+' '.join([str(ii) for ii in range(ax0)]))
    # for ii, line in enumerate(contents):
    #     print(str(ii)+" ", " ".join(line))

    KNOWN_GOOD = parse_to_lists(r"debug/d4_known_pos.txt", cast=int)
    KNOWN_GOOD = set([(ii, jj) for ii, jj in zip(KNOWN_GOOD[0], KNOWN_GOOD[1])])
    # print(KNOWN_GOOD)

    flat_string = "".join(contents)
    field = Field(content=flat_string, shape=(ax0, ax1))
    print(find_xmas_in_field(field))
    print(find_diag_mas_in_field(field))
