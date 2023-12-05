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
                print(oval, vals[i], imap, map_name)
    print(min(vals))


def part2():
    seeds, mappings = almanac()

    all_seeds = []
    for range_start, range_length in zip(seeds[::2], seeds[1::2]):
        all_seeds.append(list(range(range_start, range_start + range_length)))
    vals = all_seeds
    for map_name in mappings:
        print(mappings)
        for i in range(len(vals)):
            for imap in mappings[map_name]:
                oval = vals[i]
                nstart, start, length = imap
                off = start - nstart
                if vals[i] in range(start, start + length):
                    vals[i] -= off
                    break
    print(min(vals))


part2()
