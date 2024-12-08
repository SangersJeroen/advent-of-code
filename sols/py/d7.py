from aoc_lib import read_file
from time import time_ns


def parse_calibration(calibration_line: str) -> tuple[int, list[int]]:
    total_str, weights_str = calibration_line.split(": ")
    weights: list[int] = [int(i) for i in weights_str.split()]
    total: int = int(total_str)
    return total, weights


def concat(left: int, right: int) -> int:
    return int(str(left) + str(right))


def inverse_concat(left: int, right: int) -> tuple[bool, int]:
    rstr: str = str(right)
    if str(left)[-len(rstr) :] == rstr and len(str(left)) > len(str(right)):
        return (True, int(str(left).removesuffix(str(right))))
    else:
        return (False, 0)


def can_reach_total(totals: list[int | float], weights: list[int]) -> bool:
    if len(totals) == 0 or (len(totals) == 1 and totals[0] <= 0):
        return False

    # Solving for the base cases:
    if len(weights) <= 2:
        if weights[0] * weights[1] in totals:
            return True
        elif weights[0] + weights[1] in totals:
            return True
        elif int(str(weights[0]) + str(weights[1])) in totals:
            return True
    else:
        new_totals_sub = [i - weights[-1] for i in totals]
        via_sub: bool = can_reach_total(new_totals_sub, weights[:-1])

        new_totals_div = [
            int(i / weights[-1]) for i in totals if (i % weights[-1]) == 0
        ]
        via_div: bool = can_reach_total(new_totals_div, weights[:-1])

        new_totals_con = [
            inverse_concat(i, weights[-1])[1]
            for i in totals
            if inverse_concat(i, weights[-1])[0]
        ]
        via_inv: bool = can_reach_total(new_totals_con, weights[:-1])

        return via_sub or via_inv or via_div
    return False


if __name__ == "__main__":
    contents = read_file(r"inputs/d7.txt")

    count = 0
    start = time_ns()
    for line in contents:
        total, weights = parse_calibration(line)
        if can_reach_total([total], weights):
            count += total
    print(f"Time taken: {(time_ns()-start)/1e6:.2f} milliseconds")
    print(count)
