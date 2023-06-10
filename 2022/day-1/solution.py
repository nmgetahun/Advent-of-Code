"""
Written by Nat Getahun
Github username: nmgetahun
Email: nmgetahun@uchicago.edu

Advent of Code Day 1 Challenge:
https://adventofcode.com/2022/day/1
"""
# ------------------------------------------------------------------------------

with open("input.txt") as f:
    max_count, count = [0, 0, 0], 0
    for line in f:
        if len(line) != 1:
            count += int(line)
        else:
            if count > min(max_count):
                max_count[max_count.index(min(max_count))] = count
            count = 0

print("part 1: ", max(max_count)) # 66616
print("part 2: ", sum(max_count)) # 199172
