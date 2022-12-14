import pathlib
import numpy as np
import math
from dataclasses import dataclass
from pprint import pprint

def read_input():
    with open(f"{pathlib.Path(__file__).parent.resolve()}/input3.txt", "r") as f:
        return [x.strip().split(" ") for x in f.readlines()]

def part1():    
    res = 0
    grid = np.zeros((1000,1000), np.int32)
    x,y = len(grid)//2, len(grid[0])//2
    xt,yt = x, y
    for com in read_input():
        dx,dy = 0,0
        dir,dist = com[0],int(com[1])
        if dir == "U":
            dy = -1
        elif dir == "D":
            dy = 1
        elif dir == "L":
            dx = -1
        elif dir == "R":
            dx = 1
        else:
            assert(False)

        for _ in range(dist):
            xprev,yprev = x,y
            x += dx
            y += dy
            if int(math.sqrt((x - xt)**2 + (y - yt)**2)) > 1:
                xt,yt = xprev,yprev

            if grid[xt][yt] == 0:
                res += 1
            grid[xt][yt] += 1
        
    return res

class Knot():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def __repr__(self):
        return f"{self.x}, {self.y}"

def move(knots, x, y, head):
        knot = knots[0]
        xprev,yprev = knot.x,knot.y
        if head:
            knot.x += x
            knot.y += y
        else:
            knot.x = x
            knot.y = y

        if len(knots) == 1:
            return

        dist = math.sqrt((knot.x - knots[1].x)**2 + (knot.y - knots[1].y)**2)
        if dist == 2:
            move(knots[1:], xprev, yprev, False)
        elif dist > 2:
            move(knots[1:], int(math.copysign(1, knot.x - knots[1].x)), int(math.copysign(1, knot.y - knots[1].y)), True)

            
def part2():
    res = 0
    knots = [Knot(10, 10) for x in range(10)]
    visited = []


    for com in read_input():
        dx,dy = 0,0
        dir,dist = com[0],int(com[1])
        if dir == "U":
            dy = -1
        elif dir == "D":
            dy = 1
        elif dir == "L":
            dx = -1
        elif dir == "R":
            dx = 1
        else:
            assert(False)

        for _ in range(dist):
            if (knots[-1].x, knots[-1].y) not in visited:
                visited.append((knots[-1].x, knots[-1].y))
            move(knots, dx, dy, True)

            grid = []
            for i in range(20):
                row = []
                for j in range(20):
                    row.append('.')
                grid.append(row)

            for i,knot in enumerate(knots):
                grid[knot.y][knot.x] = str(i)
            print(np.matrix(grid))


    
    return len(visited)

if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
