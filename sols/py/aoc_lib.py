from typing import Any, Optional


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


def read_file_as_field(file: str) -> list[list[Any]]:
    # Take a string ppath relative to the working directory of the
    # interpeter and return a list where every entry is a line in string
    # form with the newline characters strpped
    with open(file, "r") as text_file:
        contents: list[str] = text_file.readlines()
        for line in contents:
            line = line.rstrip("\n")

    field: list[list[Any]] = list()
    for ii in range(len(contents)):
        row: list[Any] = list()
        for jj in range(len(contents[0])):
            item = [contents[ii][jj]]
            if item != ['\n']:
                row.append(item)
        field.append(row)
    return field 


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


