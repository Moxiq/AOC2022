import pathlib


def read_input():
    pairs = []
    with open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", "r") as f:
        return f.readlines()

#returns start stack and line nbr
def build(lines) -> tuple:
    stack = [list() for x in range(10)]
    basenbr = 0
    for i, line in enumerate(lines):
        if '1' in line:
            basenbr = i
            break
    
    for i, line in enumerate(lines):
        if i >= basenbr:
            break
        for col, ch in enumerate(line): 
            if ch.isalpha():
                stack[int(lines[basenbr][col])].append(ch)
    [x.reverse() for x in stack]
    return (stack, basenbr)


                
def part1():
    inp = read_input()
    stack,start = build(inp)

    i = start+2
    while i < len(inp):
        line = inp[i]
        splitted = line.strip().split(" ")
        cnt,src,dst = int(splitted[1]),int(splitted[3]),int(splitted[5])
        for _ in range(cnt):
            stack[dst].append(stack[src].pop())
        i += 1
    return ''.join([x[-1] for x in stack if len(x) > 0])


def part2():
    inp = read_input()
    stack,start = build(inp)

    i = start+2
    while i < len(inp):
        line = inp[i]
        splitted = line.strip().split(" ")
        cnt,src,dst = int(splitted[1]),int(splitted[3]),int(splitted[5])
        stack[dst] += stack[src][len(stack[src])-cnt::1]
        [stack[src].pop() for _ in stack[src][len(stack[src])-cnt::1]]
            
        i += 1
    return ''.join([x[-1] for x in stack if len(x) > 0])

if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
