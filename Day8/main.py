import pathlib
import sys

def read_input():
    with open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", "r") as f:
        return [[int(ch) for ch in line.strip()] for line in f.readlines()]

def view_dist(this, trees):
    for i, val in enumerate(trees):
        if val >= this:
            return i + 1
        
    return len(trees)

def part1():
    inp = read_input()
    res = 0

    for row in range(len(inp)):
        for col in range(len(inp[row])):
            if row == 0 or col == 0 or row == len(inp)-1 or col == len(inp)-1:
                res += 1
                continue
            if inp[row][col] > max(inp[row][:col]): # left
                res += 1
                continue
            if inp[row][col] > max([x[col] for x in inp[:row]]): # top
                res += 1
                continue
            if inp[row][col] > max(inp[row][col+1:]): # right
                res += 1
                continue
            if inp[row][col] > max([x[col] for x in inp[row+1:]]): # bottom
                res += 1
                continue
    return res
            
def part2():
    inp = read_input()
    res = 0

    for row in range(len(inp)):
        for col in range(len(inp[row])):
            p = 1
            p *= view_dist(inp[row][col], inp[row][:col][::-1]) # left
            p *= view_dist(inp[row][col], [x[col] for x in inp[:row]][::-1]) # top
            p *= view_dist(inp[row][col], inp[row][col+1:]) # right
            p *= view_dist(inp[row][col], [x[col] for x in inp[row+1:]]) # bottom
            res = max(res, p)
    return res

if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
