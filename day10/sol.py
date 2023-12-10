def parse(input_file):
    field = []
    with open(input_file, "r") as file:
        file_content = file.readlines()
    for line in file_content:
        field.append([char for char in line.rstrip("\n")])
    return field


def find_start(field):
    for i, line in enumerate(field):
        for j, char in enumerate(line):
            if char == "S":
                start = (i, j)
            else:
                pass
    return start


accepts_from = {
    "-": ["e", "w"],
    "|": ["n", "s"],
    "L": ["n", "e"],
    "J": ["n", "w"],
    "7": ["s", "w"],
    "F": ["s", "e"],
    "S": ["n", "s", "w", "e"],
    ".": [],
}


def reverse_dir(direction):
    reverse_dir = {"s": "n", "n": "s", "w": "e", "e": "w"}
    return reverse_dir[direction]


dir_to_off = {"s": (-1, 0), "w": (0, 1), "n": (1, 0), "e": (0, -1)}


def connects(token_one, token_two, direction):
    # print(token_one, token_two, direction)
    if token_one == "S" and direction in accepts_from[token_two]:
        return True
    elif token_one == "." or token_two == ".":
        return False
    elif direction in accepts_from[token_two]:
        return True
    return False


def find_loop(field):
    start = find_start(field)
    loop_coords = [start]
    loop_closed = False

    i, j = start
    while not loop_closed:
        for dirc in map(reverse_dir, accepts_from[field[i][j]]):
            dy, dx = dir_to_off[dirc]
            y, x = i + dy, j + dx
            if field[y][x] == "S" and (y, x) == start and len(loop_coords) > 2:
                # print("S found")
                loop_closed = True
                break
            elif connects(field[i][j], field[y][x], dirc) and (y, x) not in loop_coords:
                # print(
                #     f"Connects: {i,j}->{y,x}  direction: {dirc} by {field[i][j]} -> {field[y][x]}"
                # )
                loop_coords.append((y, x))
                i, j = y, x
                break
    loop_coords.append(start)
    return loop_coords


def calculate_distances(loop):
    dist_cw = [i for i in range(len(loop))]
    dist_ccw = dist_cw[::-1]
    min_dist_from_start = [min(i, j) for i, j in zip(dist_cw, dist_ccw)]
    return min_dist_from_start


def area_enclosed(field, loop):
    area = 0
    for i in range(1, len(field)):
        in_loop = False
        for j in range(0, len(field[0])):
            if on_loop := ((i, j) in loop) and (char := field[i][j]) not in {
                "-",
                "L",
                "J",
                "F",
                "7",
            }:
                in_loop = not in_loop
            elif on_loop and char in {"L", "J", "7", "F"}:
                in_loop = True
            if in_loop and not on_loop:
                area += 1
                field[i][j] = "X"
    print("Area: ", area)
    for line in field:
        print(line)


if __name__ == "__main__":
    file = "test.txt"
    field = parse(file)
    # print("X   0    1    2    3    4")
    # for i, line in enumerate(field):
    #     print(i, line)
    loop = find_loop(field)
    distance_from_start = calculate_distances(loop)
    print(f"maximum distance from the start: {max(calculate_distances(loop))}")
    area_enclosed(field, loop)
