from aoc_lib import read_file, read_to_field, Field, Vec
from math import sqrt


def distance_between_all(pos: Vec, antennae_coords: list[Vec]) -> list[float]:
    """
    For any position in the field should compute the distance to all antennae and return these in a list
    """

    return [abs(ant - pos) for ant in antennae_coords]


def colinear(vec_one: Vec, vec_two: Vec) -> bool:
    # if (vec_one.x == 0 and vec_one.y == 0) or (vec_two.x == 0 and vec_two.y == 0):
    #     return True
    # if vec_two.x == 0 or vec_two.y == 0:
    #     return False
    # elif vec_one.x == 0:
    #     return vec_two.y == 0
    res = vec_one / vec_two
    return res.x == res.y


def compute_if_antinode_part1(pos: Vec, antennae: dict[str, list[Vec]]) -> bool:
    """
    Should return True if only two antennas overlap
    """

    for ant_type in antennae.keys():
        antennae_coords = antennae[ant_type]
        distances = distance_between_all(pos, antennae_coords)
        for dist_0, ant_0 in zip(distances, antennae_coords):
            for dist_1, ant_1 in zip(distances, antennae_coords):
                if dist_1 == 2 * dist_0 and colinear(ant_0 - pos, ant_1 - pos):
                    return True
    return False


def intersect_two_ant(pos: Vec, antennae_coords: list[Vec]) -> bool:
    for ii, ant_0 in enumerate(antennae_coords):
        for jj, ant_1 in enumerate(antennae_coords):
            if ii != jj:
                ray = ant_0 - ant_1
                if colinear(ant_0 - pos, ray):
                    return True
    return False


def compute_if_antinode_part2(pos: Vec, antennae: dict[str, list[Vec]]) -> bool:
    """
    Should return True if only two antennas overlap
    """

    for ant_type in antennae.keys():
        antennae_coords = antennae[ant_type]
        if len(antennae_coords) <= 1:
            return False
        if intersect_two_ant(pos, antennae_coords):
            return True
    return False


if __name__ == "__main__":
    contents = read_file(r"inputs/d8.txt")

    antennae: dict[str, list[Vec]] = dict()
    for ii, line in enumerate(contents):
        for jj, char in enumerate(line):
            if char != ".":
                try:
                    antennae[char].append(Vec(ii, jj))
                except KeyError:
                    antennae[char] = list()
                    antennae[char].append(Vec(ii, jj))

    # Computation and visualisation part 1
    field: Field = read_to_field(r"inputs/d8.txt")
    field_dims = field.shape()

    count = 0
    for xx in range(field_dims[0]):
        for yy in range(field_dims[1]):
            pos = Vec(xx, yy)
            if compute_if_antinode_part1(pos, antennae):
                field.set_square(xx, yy, "#")
                count += 1

    print(field)
    print(count)

    # Computation and visualisation part 2
    field: Field = read_to_field(r"inputs/d8.txt")
    field_dims = field.shape()

    count = 0
    for xx in range(field_dims[0]):
        for yy in range(field_dims[1]):
            pos = Vec(xx, yy)
            if compute_if_antinode_part2(pos, antennae):
                field.set_square(xx, yy, "#")
                count += 1

    print(field)
    print(count)
