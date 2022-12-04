import pathlib
from dataclasses import dataclass

@dataclass
class Pair:
    a1: int
    a2: int
    b1: int
    b2: int

def read_input():
    pairs = []
    with open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", "r") as f:
        for line in f.readlines():
            a,b = line.split(",")
            a1,a2 = a.strip().split("-")
            b1,b2 = b.strip().split("-")
            pairs.append(Pair(int(a1), int(a2), int(b1), int(b2)))
    return pairs
                
def part1():
    inp = read_input()
    p = 0
    for pair in inp:
        if pair.b1 >= pair.a1 and pair.b2 <= pair.a2:
            p += 1
        elif pair.a1 >= pair.b1 and pair.a2 <= pair.b2:
            p += 1

    return p


def part2():
    inp = read_input()
    p = 0
    for pair in inp:
        if pair.b1 <= pair.a1 and pair.b2 >= pair.a1:
            p += 1
        elif pair.b1 <= pair.a2 and pair.b2 >= pair.a2:
            p += 1
        elif pair.b1 >= pair.a1 and pair.b2 <= pair.a2:
            p += 1
        
    return p

if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
