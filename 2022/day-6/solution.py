"""
Written by Nat Getahun
Github username: nmgetahun
Email: nmgetahun@uchicago.edu

Advent of Code Day 6 Challenge:
https://adventofcode.com/2022/day/6
"""
# ------------------------------------------------------------------------------

PART_1_MARKER_LENGTH = 4
PART_2_MARKER_LENGTH = 14

# Parts 1 & 2 Primary
def find_start_marker_idx(marker_len):
    # Find end index of the first X character unit with no repeating letters
    for idx in range(marker_len, len(data) + 1):
        unit = data[idx - marker_len:idx]
        if len(set(unit)) == marker_len:
            return idx


# Main
if __name__ == "__main__":
    # Get data from today's AoC input file
    with open("input.txt") as file:
        data = file.read()

    # Part 1: X = 4 -> 1647
    print("Part 1:", str(find_start_marker_idx(PART_1_MARKER_LENGTH)))

    # Part 2: X = 14 -> 2447
    print("Part 2:", str(find_start_marker_idx(PART_2_MARKER_LENGTH)))
