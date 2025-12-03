from aoc_lib import read_file, Vec


def button_line_to_vector(line: str) -> Vec:
    _, _, l, r = line.split()
    l = l.rstrip(",")
    cl, numl = l.split("+")
    cr, numr = r.split("+")
    vec = Vec(int(numl), int(numr))
    return vec


def prize_line_to_vector(line: str, off: int) -> Vec:
    _, xc, yc = line.split()
    xc = xc.rstrip(",").lstrip("X=")
    yc = yc.lstrip("Y=")
    return Vec(int(xc) + off, int(yc) + off)


def solve_system(matrix: list[Vec], target_vec: Vec) -> Vec:
    a, b, c, d = matrix[0].x, matrix[1].x, matrix[0].y, matrix[1].y
    det_inv = 1 / (a * d - b * c)
    press_a = det_inv * (target_vec.x * d - target_vec.y * b)
    press_b = det_inv * (target_vec.y * a - target_vec.x * c)
    return Vec(press_a, press_b)


def isint(num: float) -> bool:
    if num % 1 < 0.01 or num % 1 > 0.99:
        return True
    return False


if __name__ == "__main__":
    lines = read_file(r"inputs/d13.txt")
    tickets = 0
    for ii, (but_a, but_b, prize) in enumerate(
        zip(lines[::4], lines[1::4], lines[2::4])
    ):
        vec_A = button_line_to_vector(but_a)
        vec_B = button_line_to_vector(but_b)
        vec_P = prize_line_to_vector(prize, 10000000000000)
        solution = solve_system([vec_A, vec_B], vec_P)
        if (
            isint(solution.x)
            and isint(solution.y)
            and (solution.x > 0)
            and (solution.y > 0)
        ):
            tickets += solution * Vec(3, 1)
    print(tickets)
