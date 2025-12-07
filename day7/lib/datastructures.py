from collections import defaultdict



class Grid:
    def __init__(self, data: list[str]) -> None:
        self.x_size: int = len(data[0])
        self.y_size: int = len(data)
        self.data: list[list[str]] = [[i for i in j] for j in data]
        self.weights: list[list[int]] = [[0 for i in j] for j in data]
        self.splits: int = 0

    def __getitem__(self, getter: tuple[int, int]) -> str:
        i: int
        j: int
        i, j = getter
        if i < 0 or j < 0:
            return '0'
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

    def plot(self) -> None:
        for line, weights in zip(self.data, self.weights):
            print(''.join(line), ''.join(map(str, weights)))

    def propagate(self) -> None:
        for jj, line in enumerate(self.data[:]):
            field, weights = [], []
            for ii, ch in enumerate(line):
                if jj == self.y_size-1:
                    ch = '.'
                if ch == 'S': # Create beam below
                    self[(ii,jj+1)] = '|'
                    self.weights[jj+1][ii] += 1
                elif ch == '|': # Propagate beam downward
                    if self[(ii, jj+1)] != '^':
                        self[(ii, jj+1)] = '|'
                        self.weights[jj+1][ii] += self.weights[jj][ii]
                elif ch == '^': # Split beams if char above is a beam
                    if self[(ii, jj-1)] == '|':
                        self.splits += 1
                        self[(ii-1, jj+1)] = '|'
                        self[(ii+1, jj+1)] = '|'
                        self.weights[jj+1][ii-1] += self.weights[jj-1][ii]
                        self.weights[jj+1][ii+1] += self.weights[jj-1][ii]
                field.append(ch)
                weights.append(self.weights[jj][ii])
            print(''.join(field), ''.join(map(str, weights)))



    def sum_beams(self) -> None:
        depth = len(self.data)
        beams = 0
        for ww in self.weights[self.y_size-1]:
            beams += ww
        return beams


