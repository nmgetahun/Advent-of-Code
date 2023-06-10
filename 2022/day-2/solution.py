"""
Written by Nat Getahun
Github username: nmgetahun
Email: nmgetahun@uchicago.edu

Advent of Code Day 2 Challenge:
https://adventofcode.com/2022/day/2
"""
# ------------------------------------------------------------------------------

strategy_scores1 = {"A": {"X": 4, "Y": 8, "Z": 3},
                   "B": {"X": 1, "Y": 5, "Z": 9},
                   "C": {"X": 7, "Y": 2, "Z": 6}}

strategy_scores2 = {"A": {"X": 3, "Y": 4, "Z": 8},
                   "B": {"X": 1, "Y": 5, "Z": 9},
                   "C": {"X": 2, "Y": 6, "Z": 7}}

score1, score2 = 0, 0

with open("input.txt") as f:
    for line in f:
        you, me = tuple(line.split())
        score1 += strategy_scores1[you][me] # test 1
        score2 += strategy_scores2[you][me] # test 2

print("part 1: ", score1) # 11475
print("part 2: ", score2) # 16862
