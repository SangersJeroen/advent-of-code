def almanac():
    with open("input.txt", "r") as file:
        content = file.readlines()

    seedline = content.pop(0)
    _ = content.pop(0)

    _, seeds = seedline.split(":")
    seeds = [int(x) for x in seeds.lstrip(" ").rstrip("\n").split(" ")]

    parsed_maps = {}
    buffer = []
    for line in content:
        line = line.rstrip("\n")
        if len(line.split()) == 2:
            mapping = line.split()[0]
        else:
            if line == "":
                parsed_maps[mapping] = buffer
                buffer = []
            else:
                buffer.append(line)

    for key, values in zip(parsed_maps, parsed_maps.values()):
        nval = []
        for value in values:
            value = [int(i) for i in value.split(" ")]
            nval.append(value)
        parsed_maps[key] = nval

    return (seeds, parsed_maps)


def part1():
    seeds, mappings = almanac()
    vals = seeds
    for map_name in mappings:
        for i in range(len(vals)):
            for imap in mappings[map_name]:
                oval = vals[i]
                nstart, start, length = imap
                off = start - nstart
                if vals[i] in range(start, start + length):
                    vals[i] -= off
                    break


def calc_overlap(irange, imap):
    _, start, length = imap
    map_min, map_max = start, start + length
    range_min, range_max = irange

    if map_max <= range_max and map_min >= range_min:
        new_ranges = [
            [map_min, map_max],
            [range_min, map_min - 1],
            [map_max + 1, range_max],
        ]

        return True, new_ranges
    if map_max >= range_max and map_min <= range_min:
        new_ranges = [[range_min, range_max]]

        return True, new_ranges
    if map_min >= range_min and map_max >= range_max and map_min <= range_max:
        new_ranges = [[map_min, range_max], [range_min, map_min - 1]]

        return True, new_ranges
    if map_max <= range_max and map_min <= range_min and map_max >= range_min:
        new_ranges = [[range_min, map_max], [map_max + 1, range_max]]

        return True, new_ranges
    return False, []


def part2():
    seeds, mappings = almanac()
    ranges = []

    for rng_start, rng_length in zip(seeds[::2], seeds[1::2]):
        ranges.append([rng_start, rng_start + rng_length])

    #
    #
    for map_name in mappings:
        next_ranges = []
        print(map_name, len(ranges))
        for irange in ranges:
            for imap in mappings[map_name]:
                has_overlap, new_ranges = calc_overlap(irange, imap)
                if has_overlap:
                    nstart, start, length = imap
                    off = start - nstart
                    mod_range = [i - off for i in new_ranges.pop(0)]

                    try:
                        next_ranges.pop(next_ranges.index(irange))
                    except:
                        pass

                    next_ranges.append(mod_range)

                    if len(new_ranges) > 0:
                        for j in new_ranges:
                            next_ranges.append(j)
                    break
                else:
                    next_ranges.append(irange)
        ranges = next_ranges
    flattened = []
    for i in ranges:
        flattened.extend(i)


part2()
