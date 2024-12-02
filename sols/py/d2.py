from aoc_lib import parse_to_lists, read_file, split_line
from time import time_ns


def compute_gradient(entries: list[int]) -> list[int]:
    grad: list[int] = list()
    entr_len: int = len(entries)
    for ii in range(entr_len - 1):
        diff = entries[ii + 1] - entries[ii]
        grad.append(diff)
    return grad


def test_safe(gradient: list[int]) -> bool:
    # Test for decreasing entries
    all_neg: bool = all([grad < 0 for grad in gradient])
    # Test for increasing entries
    all_pos: bool = all([grad > 0 for grad in gradient])
    # Test for slope between equal 1 and 3
    good_slope: bool = all([abs(grad) < 4 and abs(grad) >= 1 for grad in gradient])

    if (all_neg and good_slope) or (all_pos and good_slope):
        return True
    else:
        return False


def test_safe_with_dampener(entries: list[int], call_depth=0) -> bool:
    gradient: list[int] = compute_gradient(entries)
    if test_safe(gradient):
        return True

    # Test all variations of the list with one level removed
    # This would get slow if we didnt have so many already save entries
    for rej_idx in range(len(entries)):
        entries_mod = entries.copy()
        _ = entries_mod.pop(rej_idx)
        if test_safe(compute_gradient(entries_mod)):
            return True

    return False


if __name__ == "__main__":
    rows: list[list[int]] = read_file(r"inputs/d2.txt")
    time_start = time_ns()
    count_safe: int = 0
    for line in rows:
        entries: list[int] = list(split_line(line, cast=int))
        if test_safe_with_dampener(entries):
            count_safe += 1
    print(count_safe)
    time_end = time_ns()
    print(f'Part Two calculation took: {(time_end-time_start)*1e-6:.2f} milliseconds')
