from aoc_lib import Vec, read_file
import matplotlib.pyplot as plt
from math import sqrt
import numpy as np

room_x = 101
room_y = 103


class Robot:
    def __init__(self, init_pos: Vec, init_vel: Vec, dims: tuple[int, int]):
        self.position: Vec = init_pos
        self.velocity: Vec = init_vel
        self.room_x: int = dims[0]
        self.room_y: int = dims[1]

    def sim_march_n_seconds(self, n: int) -> Vec:
        new_pos: Vec = self.position + self.velocity * n
        return new_pos

    def march_n_seconds(self, n: int):
        new_pos: Vec = self.position + self.velocity * n
        self.position = new_pos
        
    def get_pos(self) -> Vec:
        x = self.position.x
        y = self.position.y
        return Vec(x % (self.room_x), y % (self.room_y))

    def __repr__(self) -> str:
        pos_repr = self.position.__repr__ ()
        vel_repr = self.velocity.__repr__()
        return '\n' + pos_repr + '--->' + vel_repr

def parse_contents(contents: list[str]) -> list[Robot]:
    robots: list[Robot] = []
    for line in contents:
        p, v = line.split()
        x0, y0 = p.lstrip('p=').split(',')
        vx0, vy0 = v.lstrip('v=').split(',')
        robot = Robot(Vec(int(x0), int(y0)), Vec(int(vx0), int(vy0)), (room_x, room_y))
        robots.append(robot)
    return robots


def calc_com(robots):
    com = Vec(0,0)
    for robot in robots:
        com += robot.get_pos()
    return com / len(robots)

def calc_moi(com, robots):
    coi_y, coi_x = 0, 0
    for robot in robots:
        pos = robot.get_pos()
        x, y = pos.x, pos.y
        xc, yc = com.x, com.y
        coi_y += (y-yc)**2
        coi_x += (x-xc)**2
    return coi_x/len(robots), coi_y/len(robots)


def variance(robots):
    xs, ys = [], []
    for robot in robots:
        pos = robot.get_pos()
        x, y = pos.x, pos.y
        xs.append(x); ys.append(y)

    avg_x = sum(xs)/len(robots)
    avg_y = sum(ys)/len(robots)
    std_x = sqrt(sum([(x - avg_x)**2 for x in xs])/len(robots))
    std_y = sqrt(sum([(y - avg_y)**2 for y in ys])/len(robots))
    return std_x, std_y


def danger_metric(robots) -> int:
    quad_counts = [0, 0, 0, 0]
    for robot in robots:
        robot.march_n_seconds(100)
        pos = robot.get_pos()
        px, py = pos.x, pos.y
        if px < mid_x and py < mid_y:
            quad_counts[0] += 1
        elif px >= mid_x + 1 and py < mid_y:
            quad_counts[1] += 1
        elif px < mid_x and py >= mid_y+1:
            quad_counts[2] += 1
        elif px >= mid_x+1 and py >= mid_y+1:
            quad_counts[3] += 1
        else:
            pass
    return int(np.prod(quad_counts))



if __name__ == '__main__':
    contents = read_file(r'inputs/d14alt.txt')

    mid_x = room_x // 2
    print(mid_x)
    mid_y = room_y // 2
    print(mid_y)

    robots = parse_contents(contents)
    iter = 0
    coi_y = []
    coi_x = []
    dangers = []
    while iter <= 100_000:
        iter += 1
        for robot in robots:
            robot.march_n_seconds(1)
        var = variance(robots)
        coi_x.append(var[0])
        coi_y.append(var[1])
        dangers.append(danger_metric(robots))

    fig, ax = plt.subplots(nrows=3)
    ax[1].plot(tot_var := np.sqrt(np.array(coi_y)*np.array(coi_x)), color='#333333', label='tot var')
    ax[2].plot(dangers, color='red', label='danger metric')
    ax[0].plot(coi_y, label='var y', linewidth=1, color='red')
    ax[0].plot(coi_x, label='var x', linewidth=1, color='blue')
    ax[1].semilogy()
    ax[0].legend(frameon=False)
    ax[1].legend(frameon=False)
    ax[2].legend(frameon=False)
    ax[0].semilogy()
    plt.savefig(r'sols_d14.png')
    #
    idx = tot_var.argmin()
    robots = parse_contents(idx + 1)
    for robot in robots:
        robot.march_n_seconds(6620)
    print('='*101, iter)
    for jj in range(103):
        row = []
        for ii in range(101):
            cnt = ' '
            for robot in robots:
                if robot.get_pos() == Vec(ii, jj):
                    cnt = '#'
                    break
            row.append(cnt)
        print(' '.join([str(r) for r in row]))



    # sec = 0
    # while sec < 101:
    #     print('\n')
    #     for jj in range(7):
    #         row = []
    #         for ii in range(11):
    #             cnt = 0
    #             for robot in robots:
    #                 if robot.get_pos() == Vec(ii, jj):
    #                     cnt += 1
    #             row.append(cnt)
    #         print(' '.join([str(r) for r in row]))
    #     for robot in robots:
    #         robot.march_n_seconds(1)
    #     print('\n')
    #     sec += 1
