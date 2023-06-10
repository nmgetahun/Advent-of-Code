"""
Written by Nat Getahun
Github username: nmgetahun
Email: nmgetahun@uchicago.edu

Advent of Code Day 7 Challenge:
https://adventofcode.com/2022/day/7
"""
# ------------------------------------------------------------------------------
import json

# Part 1 Primary
# Store home directory into dictionary
def add_directory(file, size):
    dir = {}
    line = next_line(file)

    while line[0] != "$":
        dir[line[1]] = {} if line[0] == "dir" else int(line[0])
        line = next_line(file)

    while line[2] != "..":
        if line[1] != "ls":
            dir[line[2]] = add_directory(next_line(file, True), size)

            # Part 1
            dir_size = get_size(dir[line[2]])
            size[0] += dir_size if dir_size <= 100000 else 0

        line = next_line(file)

    return dir


# Part 1 Helper
# Get OR skip next line in input file; terminates at file end
def next_line(file, skip = False):
    line = file.readline().strip().split()
    return file if skip else line if line != [] else ["$", "cd", ".."]


# Parts 1 & 2 Helper
# Get total size of a directory
def get_size(dir):
    size = 0
    for sub_dir in dir.values():
        size += get_size(sub_dir) if type(sub_dir) == dict else sub_dir

    return size


# Part 2 Primary
# Find smallest directory (size AND name) with enough space to create minimum unused space if deleted
def find_optimal_directory(dir, size, optimal_directory):
    for name, sub_dir in dir.items():
        if type(sub_dir) == dict:
            optimal_directory = find_optimal_directory(sub_dir, size, optimal_directory)
            sub_dir_size = get_size(sub_dir)

            if sub_dir_size > size and sub_dir_size < optimal_directory[0]:
                optimal_directory = [sub_dir_size, name]

    return optimal_directory


# Main
if __name__ == "__main__":
    # Get data from today's AoC input file + Part 1
    with open("input.txt") as file:
        small_dirs = [0] # Total size of dirs <= 100000
        home = {next_line(file)[2]: add_directory(next_line(file, True), small_dirs)}
        print(json.dumps(home, indent = 4)) # Print home directory (pretty though)

    # Part 2
    TOTAL_DISK_SPACE = 70000000
    MINIMUM_UNUSED_SPACE = 30000000
    home_size = get_size(home)

    space_needed = MINIMUM_UNUSED_SPACE - TOTAL_DISK_SPACE + home_size
    optimal_directory = find_optimal_directory(home, space_needed, [home_size, None]) # Size, name

    # Display
    print("Part 1: ", small_dirs[0]) # 1582412
    print("Part 2: ", optimal_directory[0]) # 3696336
