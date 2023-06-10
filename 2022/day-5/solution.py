"""
Written by Nat Getahun
Github username: nmgetahun
Email: nmgetahun@uchicago.edu

Advent of Code Day 5 Challenge:
https://adventofcode.com/2022/day/5
"""
# ------------------------------------------------------------------------------

# Get data from today's AoC input file
def get_data():
    with open("input.txt") as file:
        data = file.readlines()

    # Clean and return data
    return [line.replace("\n", "") for line in data]


# Convert input data into a list of crates for every stack
def extract_stacks(data):
    crates_raw, crates, stacks = [], [], []
    set_of_crates = data[0]

    while set_of_crates[1] != "1":
        crates_raw.append(set_of_crates)
        del data[0]
        set_of_crates = data[0]
    
    # Clean up crates
    crates = [("   " + x)[::4][1:] for x in crates_raw[::-1]]
    
    # Sort crates into stacks
    num_of_crates = set_of_crates  
    stacks = [[] for _ in num_of_crates.split()]
    for i in range(int(num_of_crates.split()[-1])):
        for crate in crates:
            if crate[i] not in ("", " "):
                stacks[i].append(crate[i])

    # Identical (deep copied) stacks for each part
    return stacks, [stack[:] for stack in stacks]


# Move a set of crates from origin stack to destination stack
#   Part 1: One at a time
#   Part 2: All at once
def move_crates(origin_stack, destination_stack, moves, part):
    if part == 1:
        destination_stack += origin_stack[-1 * moves:][::-1]
    else:
        destination_stack += origin_stack[-1 * moves:]

    del origin_stack[-1*moves:]


# Execute all moves in input file and return top of finished stacks
def execute_moves(data, stacks_p1, stacks_p2):
    for procedure in data[1:]:
        moves, origin, destination = [int(n) for n in procedure.split()[1::2]]
        
        move_crates(stacks_p1[origin - 1], stacks_p1[destination - 1], moves, 1)
        move_crates(stacks_p2[origin - 1], stacks_p2[destination - 1], moves, 2)

    config_9000 = "".join([stack[-1] for stack in stacks_p1])
    config_9001 = "".join([stack[-1] for stack in stacks_p2])

    # Return final configurations for parts 1 and 2
    return config_9000, config_9001


# Main
def main():
    # Preliminary
    data = get_data()
    stacks_p1, stacks_p2 = extract_stacks(data)

    # Do parts 1 and 2
    config_9000, config_9001 = execute_moves(data, stacks_p1, stacks_p2)

    # Display top of stacks
    print("Part 1: " + config_9000) # WHTLRMZRC
    print("Part 2: " + config_9001) # GMPMLWNMG


if __name__ == "__main__":
    main()
