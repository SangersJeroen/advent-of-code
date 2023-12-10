import math


def parse(file):
    with open(file, "r") as file:
        contents = file.readlines()

    instructions = contents.pop(0).rstrip("\n")
    _ = contents.pop(0)

    map_dict = {}
    for line in contents:
        curr_node, paths = line.rstrip("\n").split(" = ")
        path0, path1 = paths.lstrip("(").rstrip(")").split(", ")
        map_dict[curr_node] = (path0, path1)

    return instructions, map_dict


def traverse_map(instructions, map_dict):
    dir_to_idx = {"R": 1, "L": 0}
    curr_node = "AAA"
    inst_idx = 0
    while curr_node != "ZZZ":
        direction = instructions[inst_idx % (len(instructions))]
        next_node = map_dict[curr_node][dir_to_idx[direction]]
        print(curr_node, "--->", next_node, map_dict[curr_node], direction)
        curr_node = next_node
        inst_idx += 1
    return inst_idx


def traverse_map_ghost(instructions, map_dict):
    dir_to_idx = {"R": 1, "L": 0}
    curr_nodes = [i for i in map_dict.keys() if i[-1] == "A"]
    start = curr_nodes
    visited_nodes = {}
    for i in start:
        visited_nodes[i] = set()
    loop_lengths = []
    inst_idx = 0
    while not all([i[-1] == "Z" for i in curr_nodes]):
        direction = instructions[inst_idx % (len(instructions))]
        next_nodes = []
        for i, node in enumerate(curr_nodes):
            next_node = map_dict[node][dir_to_idx[direction]]
            if next_node in visited_nodes[start[i]]:
                loop_lengths.append(inst_idx)
            else:
                visited_nodes[start[i]].add(next_node)
                next_nodes.append(next_node)
        print(next_nodes)
        curr_nodes = next_nodes
        inst_idx += 1
    return inst_idx, loop_lengths, visited_nodes


if __name__ == "__main__":
    file = "input.txt"
    steps, ll, vnodes = traverse_map_ghost(*parse(file))
    print(vnodes)

    print(steps, math.lcm(*ll))
