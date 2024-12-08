from typing import Any, Optional, Self
from math import sqrt


class Vec:
    def __init__(self, x: int | float, y: int | float):
        self.x: int | float = x
        self.y: int | float = y

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return f"(x;y):({self.x};{self.y})"

    def __mul__(self, mul: int):
        return Vec(self.x * mul, self.y * mul)

    def __sub__(self, other: Self | int | float) -> Self:
        match other:
            case Vec():
                sub_vec = Vec(self.x - other.x, self.y - other.y)
                return sub_vec
            case _:
                sub_vec = Vec(self.x - other, self.y - other)
                return sub_vec

    def __abs__(self) -> float:
        return sqrt(self.x**2 + self.y**2)

    def __truediv__(self, other: Self | float | int) -> Self:
        match other:
            case Vec():
                if other.x == 0:
                    left = 0
                else:
                    left = self.x / other.x
                if other.y == 0:
                    right = 0
                else:
                    right = self.y / other.y
                sub_vec = Vec(left, right)
                return sub_vec
            case _:
                sub_vec = Vec(self.x / other, self.y / other)
                return sub_vec


class Field:
    def __init__(self, content: str, field_shape_x: int, field_shape_y: int):
        self.dim0_len: int = field_shape_x
        self.dim1_len: int = field_shape_y
        self.data = [[i] for i in content]

    def __len__(self):
        return self.dim0_len

    def shape(self) -> tuple[int, int]:
        return (self.dim0_len+1, self.dim1_len+1)

    def get(self, dim0_idx: int, dim1_idx: int):
        if dim0_idx > self.dim0_len or dim1_idx > self.dim1_len:
            return "-"
        if dim0_idx < 0 or dim1_idx < 0:
            return "-"
        index: int = dim0_idx * (self.dim0_len + 1) + dim1_idx
        return self.data[index][0]

    def set_square(self, dim0_idx: int, dim1_idx: int, value) -> None:
        assert dim0_idx <= self.dim0_len, "axis 0 coord out of bound"
        assert dim1_idx <= self.dim1_len, "axis 1 coord out of bound"
        index: int = dim0_idx * (self.dim0_len + 1) + dim1_idx
        self.data[index] = [value]

    def __getitem__(self, vec: Vec):
        dim0_idx = vec.x
        dim1_idx = vec.y
        return self.get(dim0_idx, dim1_idx)

    def __str__(self) -> str:
        string: str = ""
        for jj in range(self.dim0_len + 1):
            string += (
                " ".join(
                    str(i[0])
                    for i in self.data[
                        jj * (self.dim1_len + 1) : jj * (self.dim1_len + 1)
                        + self.dim0_len
                        + 1
                    ]
                )
                + "\n"
            )
        return string


def read_file(file: str) -> list[str]:
    # Take a string ppath relative to the working directory of the
    # interpeter and return a list where every entry is a line in string
    # form with the newline characters strpped
    with open(file, "r") as text_file:
        contents: list[str] = text_file.readlines()
        parsed: list[str] = list()
        for line in contents:
            pars = line.rstrip("\n")
            parsed.append(pars)
    return parsed 


def read_to_field(file: str) -> Field:
    # Take a string ppath relative to the working directory of the
    # interpeter and return a list where every entry is a line in string
    # form with the newline characters strpped
    with open(file, "r") as text_file:
        contents: list[str] = text_file.readlines()
        for line in contents:
            line = line.rstrip("\n")

    raw_string: str = ''
    for ii, line in enumerate(contents):
        for jj, char in enumerate(line):
            raw_string += char

    return Field(raw_string, ii, jj)


def transpose_field(contents: list[list[list[Any]]]) -> list[list[Any]]:
    ax_idx0: int = len(contents)
    ax_idx1: int = len(contents[0])
    field_t: list[list[list[Any]]] = [
        [[] for j in range(ax_idx1)] for i in range(ax_idx0)
    ]

    for ii in range(ax_idx0):
        for jj in range(ax_idx1):
            field_t[ii][jj] = contents[jj][ii]

    return field_t


def print_field(field: list[list[list[Any]]]) -> None:
    for ii, line in enumerate(field):
        print(line)


def split_line(line: str, cast: Optional[callable] = None) -> tuple[Any, ...]:
    # split the line on whitespace and return a tuple of the integer
    # numbers
    if cast is not None:
        return tuple(cast(i) for i in line.split())
    return tuple(line.split())


def parse_to_lists(file: str, cast: Optional[callable] = None) -> tuple[list[Any], ...]:
    list_o_lists: list[list[Any]] = list()
    for line in read_file(file):
        for ii, obj in enumerate(split_line(line, cast = cast)):
            try:
                list_o_lists[ii].append(obj)
            except IndexError:
                list_o_lists.append(list())
                list_o_lists[ii].append(obj)
    return tuple(list_o_lists)
