import pathlib


def read_input():
    with open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", "r") as f:
        return f.readlines()

def unique_hash(collection:enumerate):
    seen = {}
    for e in collection:
        if e in seen:
            return False
        seen[e] = 0
    return True


def unique(collection:enumerate):
    seen = []
    for e in collection:
        if e in seen:
            return False
        seen.append(e)
    return True
                
def part1():
    line = read_input()[-1]

    i = 4
    while True:
        mkr = line[i-4:i]
        if unique_hash(mkr):
            return i
        i += 1

def part2():
    line = read_input()[-1]

    i = 14
    while True:
        mkr = line[i-14:i]
        if unique_hash(mkr):
            return i
        i += 1

if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
