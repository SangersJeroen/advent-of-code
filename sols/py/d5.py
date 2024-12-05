from aoc_lib import read_file
from time import time_ns


def build_order_lists(order_specifier_lines: list[str]) -> tuple[list[str],list[str]]:
    """
    Create two list that store the rules based on their index.
    The number in `lefts` at index 0 should be before the number
    in `rights` at index 0
    """
    lefts: list[str] = list()
    rights: list[str]  = list()

    for line in order_specifier_lines:
        left, right = line.split('|')
        lefts.append(left)
        rights.append(right)

    return lefts, rights


def check_line_order(page_numbers: list[str], left_list: list[str], right_list: list[str]) -> bool:
    """
    Brute force check whether all rules are obeyed
    """
    # Looping over the page number order
    for pnum_idx, pnum in enumerate(page_numbers):
        # Find all applicable rules in the pre-made lists
        indices_in_left: list[int] = [i for i, val in enumerate(left_list) if val == pnum]
        # Find all page numbers that should be after the current page number
        nums_not_before_current: set[str] = set([right_list[i] for i in indices_in_left])
        # If there is an intersection in the sets of numbers that should be after the current
        # and the set of numbers before the current we have an invalid order
        if nums_not_before_current & set(page_numbers[:pnum_idx]):
            return False
    return True


def fix_order(page_numbers: list[str], left_list: list[str], right_list: list[str]) -> list[str]:
    """
    Fixes the order of the current `page_numbers` to match the rules in `left_list` and `right_list`
    """
    new_order: list[str] = list()
    # Loop over the numbers we need to correct
    for pnum in page_numbers:
        # Find all page numbers that should be after the current page number
        indices_in_left: list[int] = [i for i, val in enumerate(left_list) if val == pnum]
        nums_after_current: list[str] = [right_list[i] for i in indices_in_left]
        indices: list[int] = list()

        # Find all numbers in `new_order` that should be after the
        # currently being inserted number and record their indices
        for num in nums_after_current:
            if num in new_order:
                indices.append(new_order.index(num))

        # If there are no numbers which the current number should preced
        # it will be appended to the end
        if len(indices) == 0:
            new_order.append(pnum)
        # Find the minimum smallest index of all numbers we should preceed
        # and insert the number in that position
        else:
            min_idx = min(indices)
            new_order = new_order[:min_idx] + [pnum] + new_order[min_idx:]

    return new_order


def part_two(update: list[str], order_specifier_lines: list[str]) -> None:
    lefts, rights = build_order_lists(order_specifier_lines)
    count = 0
    for line in update_lines:
        page_numbers: list[str] = line.split(',')
        if not check_line_order(page_numbers, lefts, rights):
            new_order = fix_order(page_numbers, lefts, rights)
            middle_idx = len(page_numbers) // 2
            add_num = new_order[middle_idx]
            # print(line, add_num)
            count += int(add_num)
    print(count)


def part_one(update: list[str], order_specifier_lines: list[str]) -> None:
    lefts, rights = build_order_lists(order_specifier_lines)
    count = 0
    for line in update_lines:
        page_numbers: list[str] = line.split(',')
        if check_line_order(page_numbers, lefts, rights):
            middle_idx = len(page_numbers) // 2
            add_num = page_numbers[middle_idx]
            # print(line, add_num)
            count += int(add_num)
    print(count)


if __name__ == '__main__':
    contents = read_file(r'inputs/d5.txt')

    empty_line_idx: int = contents.index('')
    order_specifier_lines: list[str] = contents[:empty_line_idx]
    update_lines: list[str] = contents[empty_line_idx+1:]

    start_time = time_ns()
    part_one(update_lines, order_specifier_lines)
    print(f'Solving part one took {(time_ns() - start_time)/1e6:.2f} milliseconds')
    start_time = time_ns()
    part_two(update_lines, order_specifier_lines)
    print(f'Solving part two took {(time_ns() - start_time)/1e6:.2f} milliseconds')
