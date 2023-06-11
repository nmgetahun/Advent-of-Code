"""
Written by Nat Getahun
Github username: nmgetahun
Email: nmgetahun@uchicago.edu

Advent of Code Day 9 Challenge:
https://adventofcode.com/2022/day/9
"""
# ------------------------------------------------------------------------------
import math

MOVES = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}

# Move head according to instruction and validate rope after each step
def execute(instruction, head, tail, visited):
    direction, count = MOVES[instruction[0]], instruction[1]
    for _ in range(count):
        head[0] += direction[0]
        head[1] += direction[1]
    
    validate_rope(head, tail)
    visited.add(tuple(tail))

# Ensure rope length = 1 unit (head, tail not too far apart)
def validate_rope(head, tail):
    hx, hy = head[0], head[1]
    tx, ty = tail[0], tail[1]
    dx, dy = abs(hx - tx), abs(hy - ty)

    if dx + dy > 1:
        if dx + dy > 2:
            x = (head[0] + tail[0]) / 2.0
            y = (head[1] + tail[1]) / 2.0
            tail[0] = math.ceil(x) if x >= 0 else math.floor(x)
            tail[1] = math.ceil(y) if y >= 0 else math.floor(y)
        elif hx == tx or hy == ty:
            tail
    elif dx + dy == 2


def not_touching(head, tail):
    
    return dx > 1 or dy > 1 or dx + dy > 2

# Main
if __name__ == "__main__":
    head, tail = [0, 0], [0, 0]
    visited = {(0, 0)}

    with open("input.txt") as file:
        for line in file:
            line = line.split()
            execute((line[0], int(line[1])), head, tail, visited)
    
    print("Part 1:", len(visited))
    print("Part 2:")
