import numpy as np
from numpy._typing import NDArray

field: list[list[str, ...], ...] = []

with open("input.txt", "r") as file:
    contents = file.readlines()

for line in contents:
    char_list_line: list[str, ...] = []
    line = line.rstrip("\n")

    for char in line:
        char_list_line.append(char)

    field.append(char_list_line)

NUMBERS = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
NOT_SPECIAL = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."}

field: NDArray[str] = np.asarray(field, dtype="U")
y, x = field.shape


def get_adjacent_indices(idxs: tuple[int, int]) -> list[tuple[int, int], ...]:
    indices: list[tuple[int, int], ...] = []
    for i in [i - 1 for i in range(3)]:
        for j in [i - 1 for i in range(3)]:
            if 0 <= (idxs[0] + j) < y and 0 <= (idxs[1] + i) < x:
                indices.append((idxs[0] + j, idxs[1] + i))
    return indices


indices_to_check = []
for j in range(y):
    for i in range(x):
        if field[j][i] not in NOT_SPECIAL:
            extra_indices = get_adjacent_indices((j, i))
            for idx in extra_indices:
                if field[idx] in NUMBERS:
                    indices_to_check.append(idx)

number_indices = []
for idx in indices_to_check:
    j, i = idx
    while (0 <= i - 1 < x) and (field[j, i - 1] in NUMBERS):
        i -= 1
    if (j, i) not in number_indices:
        number_indices.append((j, i))

part_sum = []
for idx in number_indices:
    j, i = idx
    num_str: str = field[j, i]
    while (0 <= i + 1 < x) and field[j, i + 1] in NUMBERS:
        num_str += field[j, i + 1]
        i += 1
        print(j, i, num_str)
    part_sum.append(int(num_str))

print(sum(part_sum))

matches = {}
for j in range(y):
    for i in range(x):
        if field[j][i] == "*":
            extra_indices = get_adjacent_indices((j, i))
            indices_to_check = []
            for idx in extra_indices:
                if field[idx] in NUMBERS:
                    indices_to_check.append(idx)
            matches[str((j, i))] = indices_to_check

number_indices = {}
for key, value in zip(matches, matches.values()):
    print(key, value)
    new_values = []
    for idx in value:
        j, i = idx
        print(j, i)
        while (0 <= i - 1 < x) and (field[j, i - 1] in NUMBERS):
            i -= 1
        if (j, i) not in new_values:
            new_values.append((j, i))
    number_indices[key] = new_values

ratios = {}
for key, value in zip(number_indices, number_indices.values()):
    temp = []
    for idx in value:
        j, i = idx
        num_str: str = field[j, i]
        while (0 <= i + 1 < x) and field[j, i + 1] in NUMBERS:
            num_str += field[j, i + 1]
            i += 1
        temp.append(int(num_str))
    ratios[key] = temp

ratio_sum = 0
for key, value in zip(ratios, ratios.values()):
    print(len(value), value)
    if len(value) == 2:
        val0, val1 = value
        print(val0, val1, val0 * val1)
        ratio = val0 * val1
        ratio_sum += ratio

print("ratio sum", ratio_sum)
