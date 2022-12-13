import pathlib
import numpy as np
import math

def read_input():
    with open(f"{pathlib.Path(__file__).parent.resolve()}/input2.txt", "r") as f:
        return [x.strip().split(" ") for x in f.readlines()]

def part1():    
    res = 0
    grid = np.ndarray((1000,1000), np.int32)
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
            if math.sqrt((x - xt)**2 + (y - yt)**2) > 1:
                xt,yt = xprev,yprev
                if grid[xt][yt] == 0:
                    res += 1
                grid[xt][yt] += 1
        
    return res
            
def part2():
    return None

if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
