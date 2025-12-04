class Grid:
    def __init__(self, data: list[str]) -> None:
        self.x_size: int = len(data[0])
        self.y_size: int = len(data)
        self.data: list[list[str]] = [[i for i in j] for j in data]

    def __getitem__(self, getter: tuple[int, int]) -> str:
        i: int
        j: int
        i, j = getter
        if i < 0 or j < 0:
            return '.'
        return self.data[j][i]

    def __setitem__(self, getter: tuple[int, int], value: str) -> None:
        i: int
        j: int
        i, j = getter
        self.data[j][i] = value

    def get_neighbours(self, getter: tuple[int, int]) -> str:
        i: int
        j: int
        i, j = getter
        neighbours: str = ''
        for dj in [-1, 0, 1]: # N, ., S
            for di in [-1, 0, 1]: # W, ., E
                if not (di == 0 and dj == 0):
                    try:
                        neighbours += self[(i+di, j+dj)]
                    except IndexError:
                        neighbours += '.'
        return neighbours




