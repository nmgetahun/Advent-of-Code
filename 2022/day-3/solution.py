"""
Written by Nat Getahun
Github username: nmgetahun
Email: nmgetahun@uchicago.edu

Advent of Code Day 3 Challenge:
https://adventofcode.com/2022/day/3
"""
# ------------------------------------------------------------------------------

tot1, tot2, ct, badges = 0, 0, 0, set([chr(i) for i in range(65, 123)])

with open("input.txt") as f:
    for line in f:
        # part 1
        one, two = line[0:len(line)//2], line[len(line)//2:]
        char = [char for char in one if char in two][0]
        tot1 += (ord(char) - 38, ord(char) - 96)[char.lower() == char]

        # part 2
        ct += 1
        badges = badges.intersection(line)
        if ct == 3:
            badge = "".join(badges)
            tot2 += (ord(badge) - 38, ord(badge) - 96)[badge.lower() == badge]
            ct, badges = 0, set([chr(i) for i in range(65, 123)])

print("part 1:", tot1) # 7967
print("part 2:", tot2) # 2716
            