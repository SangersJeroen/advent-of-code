from aoc_lib import Field, Vec, read_file, parse_to_field


DIR: dict[str, Vec] = {
    "^": Vec(-1, +0),
    ">": Vec(+0, +1),
    "v": Vec(+1, +0),
    "<": Vec(+0, -1),
}


TESTFILE = r"./inputs/d15test.txt"
TRUEFILE = r"./inputs/d15.txt"


def parse_field(contents: list[str]) -> tuple[Field, str]:
    split_line: int = contents.index("")
    field_lines = contents[:split_line]
    moves_lines = contents[split_line + 1 :]
    field = parse_to_field(field_lines)
    moves_string = ""
    for line in moves_lines:
        for char in line:
            if char != "\n":
                moves_string += char

    return field, moves_string


def find_robot(field: Field) -> Vec:
    xx, yy = field.shape()
    for ii in range(xx):
        for jj in range(yy):
            fc = field[Vec(ii, jj)]
            if fc == "@":
                return Vec(ii, jj)
    return Vec(0, 0)


def move_robot(field: Field, position: Vec, move: str) -> Vec:
    xx, yy = field.shape()
    rxx, ryy = position.x, position.y
    if field[position + DIR[move]] == "#":
        print("wall")
        return position
    elif field[position + DIR[move]] == ".":
        field.set_square(rxx, ryy, ".")
        npos = position + DIR[move]
        field.set_square(npos.x, npos.y, "@")
        return position + DIR[move]
    else:
        move_indices: list[Vec] = []
        match move:
            case "^":
                for ii in range(1, ryy - 1):
                    if (
                        field[position + DIR[move] * ii] == "O"
                        and field[position + DIR[move] * (ii + 1)] in [".", "O"]
                    ):
                        move_indices.append(position + DIR[move] * ii)
                print(f"moving up {len(move_indices)} boxes")
                for idx in move_indices:
                    field.set_square(idx.x, idx.y, ".")
                    field.set_square(idx.x - 1, idx.y, "O")
            case ">":
                for ii in range(1, xx - rxx):
                    if (
                        field[position + DIR[move] * ii] == "O"
                        and field[position + DIR[move] * (ii + 1)] in [".", "O"]
                    ):
                        move_indices.append(position + DIR[move] * ii)
                print(f"moving right {len(move_indices)} boxes")
                for idx in move_indices:
                    field.set_square(idx.x, idx.y, ".")
                    field.set_square(idx.x, idx.y + 1, "O")
            case "v":
                for ii in range(1, yy - ryy):
                    if (
                        field[position + DIR[move] * ii] == "O"
                        and field[position + DIR[move] * (ii + 1)] in [".", "O"]
                    ):
                        move_indices.append(position + DIR[move] * ii)
                print(f"moving down {len(move_indices)} boxes")
                for idx in move_indices:
                    field.set_square(idx.x, idx.y, ".")
                    field.set_square(idx.x + 1, idx.y, "O")
            case "<":
                for ii in range(1, rxx - 1):
                    if (
                        field[position + DIR[move] * ii] == "O"
                        and field[position + DIR[move] * (ii + 1)] in [".", "O"]
                    ):
                        move_indices.append(position + DIR[move] * ii)
                print(f"moving left {len(move_indices)} boxes")
                for idx in move_indices:
                    field.set_square(idx.x, idx.y, ".")
                    field.set_square(idx.x, idx.y - 1, "O")
        field.set_square(position.x, position.y, ".")
        npos = position + DIR[move]
        field.set_square(npos.x, npos.y, "@")
        print('updates pos')
        return npos


def main():
    contents = read_file(TESTFILE)
    field, moves = parse_field(contents)
    pos = find_robot(field)
    print(field, pos)

    iter = 0
    for move in moves:
        if iter > 30:
            break
        pos = move_robot(field, pos, move)
        print(field, pos)
        iter += 1


if __name__ == "__main__":
    main()
