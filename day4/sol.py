def parser(card_string: str) -> tuple[int, list[int], list[int]]:
    """ """
    card_num_string, numbers_string = card_string.split(":")
    _, card_num = card_num_string.split()

    numbers, wnumbers = numbers_string.split("|")
    numbers: list[int] = list(map(int, numbers.split()))
    wnumbers: list[int] = list(map(int, wnumbers.split()))

    return (int(card_num), numbers, wnumbers)


def calc_score(pnum: list[int], wnum: list[int]) -> tuple[int, int]:
    """ """
    wnum_amnt = 0
    score = 0
    for num in pnum:
        if num in wnum:
            if wnum_amnt > 0:
                score *= 2
            else:
                score += 1
            wnum_amnt += 1
    return score, wnum_amnt


def count_scores() -> None:
    """ """
    with open("input.txt", "r") as file:
        c = file.readlines()

    rcnt = 0
    for line in c:
        line.rstrip("\n")
        _, pnum, wnum = parser(line)
        score, _ = calc_score(pnum, wnum)
        rcnt += score

    print("Sum of scores:", rcnt)


def count_cards() -> None:
    """ """
    with open("input.txt", "r") as file:
        c = file.readlines()

    card_amnt = [1] * len(c)

    for cnum, line in enumerate(c):
        line.rstrip("\n")
        _, pnum, wnum = parser(line)
        _, wnum_amnt = calc_score(pnum, wnum)
        for i in range(wnum_amnt):
            card_amnt[i + 1 + cnum] += 1 * card_amnt[cnum]
    card_count = sum(card_amnt)
    print("Sum of cards:", card_count)
