def read_and_sanitize(day: int, test: bool = True) -> list[str]:
    path = rf"/home/jeroensangers/Repos/advent_of_code/day{day}/inputs/"

    if test:
        path += "test.txt"
    else:
        path += "real.txt"

    contents: list[str] = list()
    try:
        with open(path, "r") as file:
            for line in file.readlines():
                contents.append(line.rstrip("\n"))
    except FileNotFoundError:
        print(f'!! File at {path} does not exist !!')
    except Exception as e:
        print(e)


    return contents
