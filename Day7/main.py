import pathlib
import sys

def read_input():
    with open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", "r") as f:
        return f.readlines()

class Node():
    def __init__(self, parent) -> None:
        self.parent = parent
        self.children = []
        self.files = []

    def get_size(self) -> int:
        size = 0
        for child in self.children:
            size += child.get_size()
        for file in self.files:
            size += file
        return size

def build_tree(root: Node):
    cur = root
    for line in read_input():
        split = line.strip().split(" ")
        if split[0] == "$":
            if split[1] == "cd" and split[2] == "..":
                cur = cur.parent
            elif split[1] == "cd" and split[2] == "/":
                cur = root
            elif split[1] == "cd" and split[2] != "ls":
                node = Node(cur)
                cur.children.append(node)
                cur = node
        elif split[0].isnumeric():
            cur.files.append(int(split[0]))

def find_files(node: Node):
    res = 0
    for node in node.children:
        size = node.get_size()
        if size <= 100000:
            res += size
        res += find_files(node)
    return res

def free_space(node: Node, space: int):
    res = sys.maxsize
    for node in node.children:
        size = node.get_size()
        if size >= space and min(size, res) == size:
            res = size
        res = min(free_space(node, space), res)
    return res

def part1():
    root = Node(None)
    build_tree(root)
    return find_files(root)        

def part2():
    root = Node(None)
    build_tree(root)
    space_available = 70000000 - root.get_size()
    needed = 30000000 - space_available
    return free_space(root, needed)

if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
