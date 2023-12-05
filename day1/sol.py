NUM_SET: set[str] = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
MAPPING: dict[str, str] = {
    "zero": "z0ro",
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}


def find_first_num(string: str) -> str:
    for char in string:
        if char in NUM_SET:
            return char
    return ""


with open("input.txt", "r") as file:
    content = file.readlines()

numsum: int = 0
for line in content:
    clean_line = line.rstrip("\n")
    lnum: str = find_first_num(clean_line)
    rnum: str = find_first_num(clean_line[::-1])

    tot_num_str: str = lnum + rnum
    numsum += int(tot_num_str)

print(f"solution to part one: {numsum}")

numsum: int = 0
for line in content:
    clean_line = line.rstrip("\n")

    for i in MAPPING.keys():
        clean_line = clean_line.replace(i, MAPPING[i])

    lnum: str = find_first_num(clean_line)
    rnum: str = find_first_num(clean_line[::-1])

    tot_num_str: str = lnum + rnum
    numsum += int(tot_num_str)

print(f"solution to part two: {numsum}")
