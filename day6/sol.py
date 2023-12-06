import math


def parse():
    with open("input.txt", "r") as file:
        contents = file.readlines()
    times = [int(i) for i in contents.pop(0).split()[1:]]
    distances = [int(i) for i in contents.pop(0).split()[1:]]
    return times, distances


def solve_quadratic(t, d):
    tmins = t / 2 - 0.5 * ((t**2 - 4 * d) ** (1 / 2))
    tplus = t / 2 + 0.5 * ((t**2 - 4 * d) ** (1 / 2))
    return tplus, tmins


def int_in_range(start, stop):
    ints_in_width = math.floor(stop - 0.001) - math.ceil(start + 0.001) + 1
    return ints_in_width


if __name__ == "__main__":
    times, distances = parse()
    print("============ PART ONE ==============")
    options = 1
    for time, distance in zip(times, distances):
        tplus, tmins = solve_quadratic(time, distance)
        opts = int_in_range(tmins, tplus)
        print(f"options for {time}ms and {distance}mm: {opts}")
        options *= opts
    print(f"total options: {options}")
    print("============ PART TWO ==============")
    time, distance = "", ""
    for t, d in zip(times, distances):
        time += str(t)
        distance += str(d)
    time = int(time)
    distance = int(distance)
    tplus, tmins = solve_quadratic(time, distance)
    opts = int_in_range(tmins, tplus)
    print(f"options for {time}ms and {distance}mm: {opts}")
