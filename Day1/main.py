import pathlib

def read_input():
    data = []
    with open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", "r") as f:
        cur = 0
        for line in f.readlines():
            if cur+1 > len(data):
                data.append(list())
            if line == "\n":
                cur += 1
                continue
            data[cur].append(int(line.strip()))
        return data
                
def part1():
    return max([sum(x) for x in read_input()])

def part2():
    top3 = [0,0,0]
    for elf in read_input():
        for i,x in enumerate(top3):
            if sum(elf) > x:
                top3[i] = sum(elf)
                break
    return sum(top3)

if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
