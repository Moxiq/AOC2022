import pathlib

def get_prio(char: str):
    if char.isupper():
        return ord(char) - ord('A') + 27
    return ord(char) - ord('a') + 1

def read_input():
    with open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]
                
def part1():
    p = 0
    for line in read_input():
        half = len(line)//2
        c1,c2 = line[:half], line[half:]
        taken = []
        for ch in c1:
            if ch in c2 and ch not in taken:
                taken.append(ch)
                p += get_prio(ch)
    return p

def badge(l1, l2, l3):
    for ch in l1:
        if ch in l2 and ch in l3:
            return ch

def part2():
    lines = read_input()
    p = 0
    i = 0
    while i < len(lines):
        g1,g2,g3 = lines[i], lines[i+1], lines[i+2]
        p += get_prio(badge(g1, g2, g3))
        i += 3
    return p

if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
