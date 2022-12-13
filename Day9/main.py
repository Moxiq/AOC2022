import pathlib
import numpy as np
import math
from dataclasses import dataclass

def read_input():
    with open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", "r") as f:
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

def move(grid, knots, x, y, head):
        knot = knots[0]
        xprev,yprev = knot.x,knot.y
        if head:
            knot.x += x
            knot.y += y
        else:
            we cant move to the previous x,y when using more tails 
            knot.x = x
            knot.y = y

        if len(knots) == 1:
            grid[x][y] += 1
            return

        if int(math.sqrt((knot.x - knots[1].x)**2 + (knot.y - knots[1].y)**2)) > 1:
            move(grid, knots[1:], xprev, yprev, False)

            
def part2():
    res = 0
    grid = np.zeros((1000,1000), np.int32)
    knots = [Knot(len(grid)//2, len(grid[0])//2) for x in range(10)]

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
            move(grid, knots, dx, dy, True)
    
    for x in grid:
        for y in x:
            if y > 0:
                res += 1
    return res + 1

if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
