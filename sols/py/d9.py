from aoc_lib import read_file
from dataclasses import dataclass
from time import sleep


def build_partition(disk_desc: str) -> list[list[str | int]]:
    raw_part: list[list[int | str]] = list()
    file_num: int = 0
    for pos, label in enumerate(disk_desc):
        if pos % 2 == 0:
            for i in range(int(label)):
                raw_part.append([file_num])
            file_num += 1
        else:
            for i in range(int(label)):
                raw_part.append(["."])
    return raw_part


def compact_free_space(partition: list[list[int | str]]) -> list[list[int | str]]:
    for ii, spot in enumerate(partition):
        if spot == ["."]:
            last_val = partition.pop(-1)
            while last_val == ["."]:
                last_val = partition.pop(-1)
            partition[ii] = last_val
    return partition


def check_sum(partition: list[list[int | str]]) -> int:
    checksum: int = sum([ii * int(val[0]) for ii, val in enumerate(partition)])
    return checksum


@dataclass
class Space:
    length: int

    def __str__(self):
        return '.'*self.length


@dataclass
class File:
    length: int
    fileid: int

    def __str__(self):
        return str(self.fileid)*self.length


def build_file_list(disk_desc: str) -> list[File | Space]:
    file_list: list[File | Space] = list()
    file_num: int = 0
    for pos, label in enumerate(disk_desc):
        if pos % 2 == 0:
            file = File(length=int(label), fileid=file_num)
            file_num += 1
            file_list.append(file)
        else:
            file_list.append(Space(int(label)))
    return file_list


def defrag_disk(disk: list[Space | File]) -> list[Space | File]:
    target_disk = list()

    is_sorted = False
    while not is_sorted:
        for ii, item in enumerate(disk):
            if isinstance(item, File):
                target_disk.append(item)
            elif isinstance(item, Space):
                max_id_index = -1
                prev_high = -1
                for jj, chunk in enumerate(disk[ii:]):
                    if isinstance(chunk, File) and chunk.fileid > prev_high and chunk.length <= item.length:
                        prev_high = chunk.fileid
                        max_id_index = ii+jj
                target_disk.append(disk[max_id_index])
                if disk[max_id_index].length < item.length:
                    target_disk.append(Space(item.length - disk[max_id_index].length))
                disk.pop(max_id_index)

            print('td'+''.join([str(i) for i in target_disk]))
            print('dd'+''.join([str(i) for i in disk]))
            print('\n')

        # connect sppac
        for ii, item in enumerate(target_disk):
            if isinstance(item, Space):
                for jj, item in enumerate(target_disk):
                    if not isinstance(Space):
                        target_disk[]
    return target_disk



if __name__ == "__main__":
    line: str = read_file(r"inputs/d9test.txt")[0]

    # part = build_partition(line)
    # print(f"partitition: {part}")
    # compacted = compact_free_space(part)
    # print(f"compacted partition: {compacted}")
    # checksum = check_sum(compacted)
    # print(f"checksum of compacted: {checksum}")

    for i in defrag_disk(build_file_list(line)):
        print(i)
