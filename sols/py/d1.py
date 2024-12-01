from aoc_lib import *

if __name__ == "__main__":
    file = r"inputs/d1_p1.txt"

    # Part 1
    list_left, list_right = parse_to_list(file)

    # Sort the lists in place
    list_left.sort()
    list_right.sort()

    # Compute the absolute difference between numbers in the left and
    # right list and take the sum
    dist = sum([abs_diff(l, r) for l, r in zip(list_left, list_right)])
    print(dist)

    # Part 2
    list_left, list_right = parse_to_list(file)
    counts: list[int] = list()

    # Iterating over entries in the left list
    # O(n**2)
    for ll in list_left:
        count: int = 0
        # Check whether the right entry is the same as the current left
        # entry for every entry in the right list, if so add one to the
        # count
        for rr in list_right:
            if ll == rr:
                count += 1
        counts.append(count)

    # Take the sum of the similarity score per entry in the left list
    # which is the number of occurences in the right list times the
    # the value in the left list
    print(sum([ll * cc for ll, cc in zip(list_left, counts)]))
