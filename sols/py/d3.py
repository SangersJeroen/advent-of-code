import re
from aoc_lib import parse_to_lists, read_file, split_line
from time import time_ns


def perform_mul_instruction(string: str) -> int:
    pattern = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
    results = re.finditer(pattern, string)

    count = 0
    for result in results:
        lint, rint = result[0].lstrip(r"mul(").rstrip(r")").split(",") # keep the left and right number
        count += int(lint) * int(rint)

    return count


def get_active_muls(string: str) -> str:
    do_matches = re.finditer(r"do\(\)", string)
    dont_matches = re.finditer(r"don't\(\)", string)

    active_after_idx: int = [0] + [match.end() for match in do_matches]
    inactive_after_idx: int = [match.end() for match in dont_matches]

    slices: list[slice] = list()
    last_stop = -1
    while len(active_after_idx) > 0: # If we can still start a sequence
        start = active_after_idx.pop(0) # Define the start of the sequence
        # print(f"opened: ({start}, ...)")
        if start > last_stop:
            while len(inactive_after_idx) > 0:
                curr_val = inactive_after_idx.pop(0)
                if (curr_val > start): # Find the index of the first stop_val greater than start
                    # print(f'closed: ({start}, {curr_val})')
                    slices.append(slice(start, curr_val)) # Add the interval
                    last_stop = curr_val
                    break
            if (start > last_stop) and len(inactive_after_idx) == 0:
                # print(f'final open ({start}, oo)')
                slices.append(slice(start, -1))
                break
        # else:
            # print('start less than last stop, REJECT')

    active_string = ''
    for act_slice in slices:
        active_string += string[act_slice]
    return active_string


if __name__ == "__main__":
    contents: list[str] = read_file(r"inputs/d3.txt")
    one_line: str = ""
    for line in contents:
        one_line += line

    start_one = time_ns()
    print(f"part one: {perform_mul_instruction(one_line)}")
    print(f"took: {(time_ns()-start_one)/1e3:.2f} ms")

    start_two = time_ns()
    print(f"part two: {perform_mul_instruction(get_active_muls(one_line))}")
    print(f"took: {(time_ns()-start_two)/1e3:.2f} ms")
