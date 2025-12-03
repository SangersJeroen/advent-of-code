from aoc_lib import Field, Vec, read_to_field
from time import sleep


DIRECTIONS: dict[str, Vec] = {
    "NN": Vec(-1, +0),
    "EE": Vec(+0, +1),
    "SS": Vec(+1, +0),
    "WW": Vec(+0, -1),
}


def hike_trails(field: Field, trail_head: Vec) -> list[set[Vec]]:
    all_trails: list[list[Vec]] = [[trail_head]]
    completed_trails: list[list[Vec]] = []
    current_num: int = 0

    iter: int = 0
    while current_num != 9 and iter < 1_000:
        # print('new_iter')
        new_trails = []
        for tt in range(len(all_trails)):
            trail = all_trails[tt]
            current_pos = trail[-1]
            current_num = int(field[current_pos])
            # print(current_pos, current_num)
            for dir in DIRECTIONS.keys():
                pos_trail = trail.copy()
                next_pos: Vec = current_pos + DIRECTIONS[dir]
                if field[next_pos] != '-':
                    next_num: int = int(field[next_pos])
                    if next_num == current_num + 1 and next_num < 9:
                        pos_trail.append(next_pos)
                        new_trails.append(pos_trail)
                        # print('appended', new_trails)
                    elif next_num == current_num + 1 and next_num == 9:
                        print('completed')
                        pos_trail.append(next_pos)
                        print(pos_trail)
                        completed_trails.append(pos_trail)
                else:
                    pass
        all_trails = new_trails
        # print(all_trails)
        iter += 1
    # print(completed_trails)
    return completed_trails


def trails_from_head(field: Field) -> int:
    xx, yy = field.shape()
    trail_heads: list[Vec] = list()
    for ii in range(xx):
        for jj in range(yy):
            v = Vec(ii, jj)
            if field[v] == '0':
                trail_heads.append(v)
            else:
                pass

    tot_score = 0
    for th in trail_heads:
        trails: list[list[Vec]] = hike_trails(field, th)
        unique_trails: list[set[Vec]] = []
        unique_nine_positions: list[Vec] = []
        for trail in trails:
            end = trail[-1]
            if end not in unique_nine_positions:
                unique_nine_positions.append(end)
            if set(trail) not in unique_trails:
                unique_trails.append(set(trail))
        score = len(unique_trails)
        print(unique_trails)
        print(score)
        tot_score += score
    return tot_score


if __name__ == '__main__':
    field: Field = read_to_field(r'inputs/d10.txt')
    print(field)
    # print(hike_trails(field, Vec(0,2)))
    print(trails_from_head(field))
    print(Vec(0,2) == Vec(0,2))
    print(Vec(0,2) != Vec(0,2))
