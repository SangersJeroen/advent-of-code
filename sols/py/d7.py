from aoc_lib import read_file


def parse_calibration(calibration_line: str) -> tuple[int, list[int]]:
    total_str, weights_str = calibration_line.split(": ")
    weights: list[int] = [int(i) for i in weights_str.split()]
    total: int = int(total_str)
    return total, weights


def concat(left: int, right: int) -> int:
    return int(str(left) + str(right))


def inverse_concat(left: int, right: int) -> tuple[bool,int]:
    rstr: str =  str(right)
    if str(left)[-len(rstr):] == rstr and len(str(left)) > len(str(right)):
        return (True, int(str(left).removesuffix(str(right))))
    else:
        return (False, 0)


def can_reach_total(totals: list[int | float], weights: list[int]) -> bool:
    assert all([i > 0 for i in weights]), "Negative values encountered"
    if len(totals) == 0:
        return False
    if len(totals) == 1 and totals[0] <= 0:
        return False
    # print(f"Can i reach {totals} with {weights} ?")
    if len(weights) <= 2:
        if weights[0] * weights[1] in totals:
            print(f"{weights[0]}*{weights[1]} = {weights[0]*weights[1]} == {totals}")
            print('*')
            return True
        elif weights[0] + weights[1] in totals:
            print(f"{weights[0]}+{weights[1]} = {weights[0]+weights[1]} == {totals}")
            print('+')
            return True
        elif int(str(weights[0]) + str(weights[1])) in totals:
            print(f"{weights[0]}||{weights[1]} = {concat(*weights)} == {totals}")
            print('||')
            return True
    else:
        new_totals_one = [i - weights[-1] for i in totals]
        via_sub: bool = can_reach_total(new_totals_one, weights[:-1])
        if via_sub:
            print("total sub last")
            print(new_totals_one)
            print('+', weights[-1])

        new_totals_two = [
            int(i / weights[-1]) for i in totals if (i % weights[-1]) == 0
        ]
        via_div: bool = can_reach_total(new_totals_two, weights[:-1])
        if via_div:
            print("total div last")
            print(new_totals_two)
            print('*', weights[-1])

        new_totals_thr = [inverse_concat(i, weights[-1])[1] for i in totals if inverse_concat(i, weights[-1])[0]]
        via_inv: bool = can_reach_total(new_totals_thr, weights[:-1])
        if via_inv:
            print("total inv conc last")
            print(new_totals_thr)
            print('||', weights[-1])

        return via_sub or via_inv or via_div
    return False


if __name__ == "__main__":
    contents = read_file(r"inputs/d7.txt")
    known_good = read_file(r'ref_good.txt')
    count = 0
    # print(can_reach_total([16931], [568,2,9,16,529,1,8,1,3,8]))
    for line in contents:
        total, weights = parse_calibration(line)
        if (can_reach_total([total], weights)):
            count += total
            assert str(total) in known_good, f'oopsie {total} shouldnt work!'
        print('\n')
    print(count)
