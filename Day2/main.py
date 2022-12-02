import pathlib
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2 
    SCISSORS = 3


    # true if p1 wins
    @staticmethod
    def winner(p1: type, p2: type) -> bool:
        if p1 == p2:
            return 0
        if p1 == RPS.ROCK and p2 == RPS.SCISSORS:
            return 1
        if p1 == RPS.PAPER and p2 == RPS.ROCK:
            return 1
        if p1 == RPS.SCISSORS and p2 == RPS.PAPER:
            return 1
        return -1

    @staticmethod
    def get_counter(p: type) -> type:
        if p == RPS.ROCK:
            return RPS.PAPER
        if p == RPS.PAPER:
            return RPS.SCISSORS
        if p == RPS.SCISSORS:
            return RPS.ROCK

    @staticmethod
    def get_loser(p: type) -> type:
        if p == RPS.ROCK:
            return RPS.SCISSORS
        if p == RPS.PAPER:
            return RPS.ROCK
        if p == RPS.SCISSORS:
            return RPS.PAPER

trnsl_map = {
    "A": RPS.ROCK,
    "B": RPS.PAPER,
    "C": RPS.SCISSORS,
    "X": RPS.ROCK,
    "Y": RPS.PAPER,
    "Z": RPS.SCISSORS
}

def read_input_frmt():
    data = []
    with open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", "r") as f:
        d1 = [line.strip().split(" ") for line in f.readlines()]
        for l in d1:
            data.append([trnsl_map[ch] for ch in l])

    return data

def read_input():
    with open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", "r") as f:
        return [line.strip().split(" ") for line in f.readlines()]
                
def part1():
    inp = read_input_frmt()
    points = 0
    for rnd in inp:
        if RPS.winner(rnd[0], rnd[1]) == -1:
            points += 6
        if RPS.winner(rnd[0], rnd[1]) == 0:
            points += 3
        points += rnd[1].value
    
    return points

def part2():
    inp = read_input()
    points = 0
    for rnd in inp:
        if rnd[1] == "X":
            points += RPS.get_loser(trnsl_map[rnd[0]]).value
        elif rnd[1] == "Y":
            points += trnsl_map[rnd[0]].value
            points += 3
        elif rnd[1] == "Z":
            points += RPS.get_counter(trnsl_map[rnd[0]]).value
            points += 6
    return points

def winner(p1: RPS, p2: RPS):
    return None

if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
