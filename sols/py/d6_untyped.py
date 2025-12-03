from aoc_lib import read_file
from time import time_ns
from time import sleep


class Vec:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    # def __repr__(self) -> str:
    #     return f"(x;y):({self.x};{self.y})"

    def __mul__(self, mul: int):
        return Vec(self.x * mul, self.y * mul)


class Field:
    def __init__(self, content: str, field_shape_x: int, field_shape_y: int ):
        self.dim0_len: int = field_shape_x
        self.dim1_len: int = field_shape_y
        self.data = [[i] for i in content]

    def __len__(self):
        return self.dim0_len

    def shape(self) -> tuple[int, int]:
        return (self.dim0_len, self.dim1_len)

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


DIRECTIONS: dict[str, Vec] = {
    "NN": Vec(-1, +0),
    "EE": Vec(+0, +1),
    "SS": Vec(+1, +0),
    "WW": Vec(+0, -1),
}

TURN: dict[str, str] = {"NN": "EE", "EE": "SS", "SS": "WW", "WW": "NN"}


def march_guard(field, guard_pos: Vec, guard_dir: str):
    next_gpos: Vec = guard_pos + DIRECTIONS[guard_dir]
    next_char: str = field[next_gpos]
    # print(next_char)
    # print(next_gpos)
    if next_char == "#" or next_char == "O":
        # print(f'turn: {guard_dir} -> {TURN[guard_dir]}')
        return True, guard_pos, TURN[guard_dir]
    elif next_char == "-":
        return False, None, None
    else:
        field.set_square(next_gpos.x, next_gpos.y, "X")
        return True, next_gpos, guard_dir
    # print("ran out of logic")


def run_sim(field: Field, direction: str, guard_pos: Vec) -> bool | list:
    field.set_square(guard_pos.x, guard_pos.y, "X")
    result: tuple[bool, Vec, str] = (True, Vec(0,0), 'NN')
    visited_wd: set[tuple[int, int, str]] = set()
    while result[0]:
        if (curr_state := (guard_pos.x, guard_pos.y, direction)) in visited_wd:
            # We have looped
            return True
        else:
            visited_wd.add(curr_state)
        result = march_guard(field, guard_pos, direction)
        guard_pos = result[1]
        direction = result[2]
    visited = list(set([(xx, yy) for (xx, yy, dd) in visited_wd]))
    return visited


def find_loops(raw_string, shape, direction: str, guard_pos: Vec) -> int:
    field = Field(raw_string, *shape)
    path: bool | list = run_sim(field, direction, guard_pos)

    count = 0
    while len(path) > 0:
        field = Field(raw_string, *shape)
        obstacle_pos_dir: tuple[int, int] = path.pop()
        xx, yy = obstacle_pos_dir
        if (xx, yy) != (guard_pos.x, guard_pos.y):
            field.set_square(xx, yy, "O")
            if run_sim(field, direction, guard_pos) == True:
                # print(f'{xx}, {yy}')
                print(field)
                sleep(0.05)
                count += 1
    return count


if __name__ == "__main__":
    contents = read_file(r"inputs/d6.txt")
    raw_string: str = ""
    guard = ""
    guard_pos = None
    for ii, line in enumerate(contents):
        for jj, char in enumerate(line):
            if char not in ["^", ">", "v", "<"]:
                raw_string += char
            else:
                guard_pos = (ii, jj)
                guard = char
                raw_string += "."

    # Part 1
    field: Field = Field(raw_string, ii, jj)
    run_sim(field, direction="NN", guard_pos=Vec(*guard_pos))
    print(sum([1 for i in field.data if i[0] == "X"]))

    # Part 2

    start = time_ns()
    cnt = find_loops(raw_string, shape=(ii,jj), direction='NN', guard_pos=Vec(*guard_pos))
    print(f'Calculating part 2 took: {(time_ns()-start)/1e6} milliseconds')
    print(cnt)
