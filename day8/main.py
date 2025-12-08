from functools import  reduce
from math import sqrt
import sys
import os
from typing import TypeAlias

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import read_and_sanitize

point: TypeAlias = tuple[int, int, int]


def distance(p0: point, p1: point) -> float:
    return sqrt((p0[0]-p1[0])**2 + (p0[1]-p1[1])**2 + (p0[2]-p1[2])**2)


def paired_by_circuit(pair: tuple[int, int], circuits: dict[int,  set[int]]) -> bool:
    ii, jj = pair
    for k, v in circuits.items():
        if ii in v and jj in v:
            return True
    return False


def compute_distances(boxes: dict[int, point]) -> dict[tuple[int, int], float]:
    distances: dict[tuple[int, int], float] = dict()
    for ii in range(len(boxes)):
        for jj in range(0, ii):
            if ii == jj:
                print('should not print')
                continue
            distance_pair = distance(boxes[ii], boxes[jj])
            distances[(ii, jj)] = distance_pair
    return distances


def main(puzzle_input: list[str]) -> None:
    boxes: dict[int, point] = dict()

    for ii, line in enumerate(puzzle_input):
        boxes[ii] = tuple(map(int, line.split(',')))

    distances = compute_distances(boxes)
    circuits: dict[int, set[int]] = {i:set([i]) for i in range(len(boxes))}
    last_connected: tuple[int, int] = ()

    iter = 0
    while len(circuits) > 1:
        iter += 1

        to_connect: tuple[int, int] = min(distances, key=distances.get)
        ii, jj = to_connect
        # print(f'considereing {ii}-{jj}')
        if paired_by_circuit(to_connect, circuits):
            # print(f'Pair paired by circuit!')
            # print()
            distances.pop(to_connect)
            last_connected = to_connect
            continue

        added_to_cicruit: bool = False
        for k, v in circuits.items():
            if ii in v and jj not in v:
                # print(f'found {ii} in circuit {k}, adding {jj}')
                for k1, v1 in circuits.items():
                    if (ii in v1 or jj in v1) and k1 != k:
                        # print(f'oops, should merge {k} & {k1}')
                        circuits[k] = v.union(v1)
                        circuits[k].add(jj)
                        added_to_cicruit = True
                        _ = circuits.pop(k1)
                        break
                    else:
                        v.add(jj)
                        added_to_cicruit = True
                break
            if jj in v and ii not in v:
                # print(f'found {jj} in circuit {k}, adding {ii}')
                for k1, v1 in circuits.items():
                    if (ii in v1 or jj in v1) and k1 != k:
                        # print(f'oops, should merge {k} & {k1}')
                        circuits[k] = v.union(v1)
                        circuits[k].add(ii)
                        added_to_cicruit = True
                        _ = circuits.pop(k1)
                        break
                    else:
                        v.add(ii)
                        added_to_cicruit = True
                break

        if not added_to_cicruit:
            # print(f'made new circuit for pair {ii}-{jj}')
            circuits[len(circuits)] = set([ii, jj])
        _ = distances.pop(to_connect)
        last_connected = to_connect
        if iter == 1000:
            circuit_sizes = sorted([len(s) for k, s in circuits.items()])
            print(f'Answer part 1: {reduce(lambda l, r: l*r, circuit_sizes[-3:])}')

    print(f'Answer part 2: {boxes[last_connected[0]][0]*boxes[last_connected[1]][0]}')


if __name__ == "__main__":
    main(puzzle_input=read_and_sanitize(day=8, test=False))
