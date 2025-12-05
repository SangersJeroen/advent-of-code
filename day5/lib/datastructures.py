from decimal import ROUND_05UP


class NumberRanges:
    def __init__(self, range_spec: str) -> None:
        self.ranges: list[tuple[int, int]] = list()
        self.ranges.append(self._parse(range_spec))

    def _parse(self, range_spec: str) -> tuple[int, int]:
        low_, high_ = range_spec.split('-')
        low, high = int(low_), int(high_)
        return (low, high)

    def __add__(self, other: str) -> None:
        l, h = self._parse(other)

        for i, r in enumerate(self.ranges):
            rl, rh = r

            if l < rl and h > rh: # Known range fully enclosed
                self.ranges[i] = (l, h)
                # print(i, (l,h), (rl, rh), 'enclosed')
                # print(f'added {l}-{h} instead of {rl}-{rh}')
                break
            elif l < rl and h > rl: # Left overlap
                self.ranges[i] = (l, rh)
                # print(i, (l,h), (rl, rh), 'left overlap')
                # print(f'added {l}-{rh} instead of {rl}-{rh}')
                break
            elif l < rh and h > rh: # Right overlap
                self.ranges[i] = (rl, h)
                # print(i, (l,h), (rl, rh), 'right overlap')
                # print(f'added {rl}-{h} instead of {rl}-{rh}')
                break
            else: # No overlap with range
                # print(i, (l,h), (rl, rh), 'no overlap')
                pass

        self.ranges.append((l, h))
        bridges = True
        while bridges:
            bridges = self._check_bridging()


    def _check_bridging(self) -> bool:
        new_ranges: list[tuple[int, int]] = list()
        excluded: list[int] = list()
        # print('checking ================')
        for i, R in enumerate(self.ranges):
            if i in excluded:
                continue
            for j, r in enumerate(self.ranges):
                if i == j:
                    continue
                # print(r, R, bridges(r, R), f'added {join(r,R)}'*bridges(r,R))
                if bridges(r, R):
                    new_ranges.append(join(r, R))
                    excluded.append(i)
                    excluded.append(j)
                    break
            if i not in excluded:
                new_ranges.append(R)
        self.ranges = new_ranges
        # print('end checking ============')
        if len(excluded) > 0:
            return True 
        return False

    def count(self) -> int:
        sum: int = 0
        for r in self.ranges:
            l, h = r
            sum += h - l + 1
        return sum

    def __repr__(self) -> str:
        string: str = ''
        for r in self.ranges:
            string += f'{r[0]}-{r[1]} '
        return string

def bridges(r0, r1):
    l0, h0 = r0
    l1, h1 = r1

    if l1 <= l0 <= h1 or l1 <= h0 <= h1:
        return True
    if l0 <= l1 <= h0 or l0 <= h1 <= h0:
        return True
    if (l0 <= l1 and h0 >= h1) or (l1 <= l0 and h1 >= h0):
        return True
    return False

def join(r0, r1):
    l0, h0 = r0
    l1, h1 = r1

    return (min(l0, l1), max(h0,h1))

if __name__ == '__main__':
    print(bridges((10,18), (16,20)))

