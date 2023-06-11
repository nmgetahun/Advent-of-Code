"""
Written by Nat Getahun
Github username: nmgetahun
Email: nmgetahun@uchicago.edu

Advent of Code Day 9 Challenge:
https://adventofcode.com/2022/day/9
"""
# ------------------------------------------------------------------------------

ROPE_LEN = 10
MOVES = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}


# Move head according to instruction and validate rope after each step
def execute(direction, count, rope, visited1, visited2):
    for _ in range(count):
        rope[0][0] += direction[0]
        rope[0][1] += direction[1]

        for i, tail in enumerate(rope[1:]):
            validate_rope(rope[i], tail)
        
        visited1.add((rope[1][0] - 100000, rope[1][1] - 100000))
        visited2.add((rope[-1][0] - 100000, rope[-1][1] - 100000))
        # print_state(head, tail)

        
# Ensure rope length = 1 unit (head, tail not too far apart)
def validate_rope(head, tail):
    hx, hy = head[0], head[1]
    tx, ty = tail[0], tail[1]
    dx, dy = abs(hx - tx), abs(hy - ty)

    if dx + dy == 3:
        if dx == 1:
            tail[0] = head[0]
        else:
            tail[1] = head[1]

    if dx == 2:
        tail[0] = (head[0] + tail[0]) // 2
    if dy == 2:
        tail[1] = (head[1] + tail[1]) // 2


# Test method for 5 x 6 board with sample input (for part 1)
def print_state(head, tail):
    head = [head[0] - 100000, head[1] - 100000]
    tail = [tail[0] - 100000, tail[1] - 100000]
    for y in list(range(5))[::-1]:
        line = ""
        for x in range(6):
            if head[0] == x and head[1] == y:
                line += "H "
            elif tail[0] == x and tail[1] == y:
                line += "T "
            else:
                line += ". "
        print(line)
    print("\n")


# Main
if __name__ == "__main__":
    rope = [[100000, 100000] for _ in range(ROPE_LEN)]
    visited1 = {(0, 0)}
    visited2 = {(0, 0)}

    with open("input.txt") as file:
        for line in file:
            line = line.split()
            direction = MOVES[line[0]]
            count = int(line[1])
            execute(direction, count, rope, visited1, visited2)
    
    print("Part 1:", len(visited1))
    print("Part 2:", len(visited2))

