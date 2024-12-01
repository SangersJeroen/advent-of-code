from typing import Any, Optional


def read_file(file: str) -> list[str]:
    # Take a string ppath relative to the working directory of the
    # interpeter and return a list where every entry is a line in string
    # form with the newline characters strpped
    with open(file, "r") as text_file:
        contents: list[str] = text_file.readlines()
        for line in contents:
            line.rstrip("\n")
    return contents


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


