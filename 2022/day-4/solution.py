"""
Written by Nat Getahun
Github username: nmgetahun
Email: nmgetahun@uchicago.edu

Advent of Code Day 4 Challenge:
https://adventofcode.com/2022/day/4
"""
# ------------------------------------------------------------------------------

def get_range(r):
    n = tuple(int(c) for c in r.split("-"))
    return range(n[0], n[1] + 1)

def subset(x, y):
    return not(False in [z in y for z in x])

in_pairs, overlaps = 0, 0

with open("input.txt") as f:
    for line in f:
        ar, br = line.split(",")
        a, b = get_range(ar), get_range(br)

        if subset(a, b) or subset(b, a): # part 1
            in_pairs += 1

        if set(a).intersection(set(b)) != set(): # part 2
            overlaps += 1

print("part 1:", in_pairs) # 413
print("part 2:", overlaps) # 806