def parse(game_string: str) -> tuple[int, list[tuple[int, int, int]]]:
    """Reads a game line to return game number and a list of tuples
    describing the hands.
    num, [(r0,g0,b0) ... (rn,gn,bn)]"""

    game_num_str, draws = game_string.split(":")
    game_num: int = int(game_num_str.lstrip("Game "))

    hands: list[str] = draws.split(";")

    drawn_colours: list[tuple[int, int, int]] = []

    for hand in hands:
        red_num: int = 0
        blue_num: int = 0
        green_num: int = 0

        cubes = hand.split(",")
        for cube in cubes:
            num, colour = cube.split()

            match colour:
                case "green":
                    green_num += int(num)
                case "blue":
                    blue_num += int(num)
                case "red":
                    red_num += int(num)

        drawn_colours.append((red_num, blue_num, green_num))

    return (game_num, drawn_colours)


def test_validity(hand: tuple[int, int, int]) -> bool:
    max_col = (12, 14, 13)
    valid = all(
        [
            True if col_num <= col_max else False
            for col_num, col_max in zip(hand, max_col)
        ]
    )
    return valid


def minimum_necessary_colour(hands: list[tuple[int, int, int]]) -> tuple[int, int, int]:
    reds: list[int, ...] = []
    green: list[int, ...] = []
    blue: list[int, ...] = []

    for hand in hands:
        (r, b, g) = hand
        reds.append(r)
        green.append(g)
        blue.append(b)

    min_col_num = (max(reds), max(blue), max(green))
    return min_col_num


def colour_power(mnc: tuple[int, int, int]) -> int:
    r, b, g = mnc
    col_pow = r * b * g
    return col_pow


# Part 1:
with open("input.txt", "r") as file:
    contents = file.readlines()

sum: int = 0
for line in contents:
    line = line.rstrip("\n")
    game_num, hands = parse(line)
    if all(map(test_validity, hands)):
        sum += game_num

print(sum)

# Part 2:
with open("input.txt", "r") as file:
    contents = file.readlines()

sum_power: int = 0
for line in contents:
    line = line.rstrip("\n")
    game_num, hands = parse(line)
    mnc = minimum_necessary_colour(hands)
    sum_power += colour_power(mnc)


print(sum_power)
