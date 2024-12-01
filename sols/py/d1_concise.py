from aoc_lib import *


if __name__ == "__main__":
    file = r"inputs/d1_p1.txt"

    # Part 1
    list_left, list_right = parse_to_lists(file, cast=int)

    # Sort the lists in place
    list_left.sort()
    list_right.sort()

    # Compute the absolute difference between numbers in the left and 
    # right list and take the sum
    dist = sum([abs(l-r) for l, r in zip(list_left, list_right)])
    print(dist)

    # Part 2
    list_left, list_right = parse_to_lists(file, cast=int)
    # Take the sum of the similarity score per entry in the left list
    # which is the number of occurences in the right list times the 
    # the value in the left list
    similarity = sum([sum([1 if ll == rr else 0 for rr in list_right])*ll for ll in list_left])
    print(similarity)
