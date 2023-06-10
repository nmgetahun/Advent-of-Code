"""
Written by Nat Getahun
Github username: nmgetahun
Email: nmgetahun@uchicago.edu

Advent of Code Day 10 Challenge:
https://adventofcode.com/2022/day/10
"""
# ------------------------------------------------------------------------------

# increment_cycle() helper
def draw_pixel(cpu):
    x, row, cycle = cpu["x"], (cpu["cycle"] - 1) // 40, cpu["cycle"] % 40 - 1
    #print(x, cpu["cycle"], row, cycle, cycle in (x-1, x, x+1))
    
    if x - 1 <= cycle <= x + 1:
        cpu["screen"][row][cycle] = "#"

# run_clock_circuit() helper
def increment_cycle(cpu):
    if (cpu["cycle"] / 20) % 2 == 1:
        cpu["signal_strength"] += cpu["x"] * cpu["cycle"]
    draw_pixel(cpu)
    cpu["cycle"] += 1


# Parts 1 & 2
def run_clock_circuit(instructions):
    cpu = {"x": 1,
           "cycle": 1,
           "signal_strength": 0,
           "screen": [["." for _ in range(40)] for _ in range(6)]}

    for instruction in instructions:
        increment_cycle(cpu)
        v = 0
        if instruction != "noop":
            increment_cycle(cpu)
            v = int(instruction)
        cpu["x"] += v

    screen = "\n".join(["".join(line) for line in cpu["screen"]])
    return (cpu["signal_strength"], screen)


# Main
if __name__ == "__main__":
    # Get data from today's AoC input file
    with open("input.txt") as file:
        instructions = [line.strip().split(" ")[-1] for line in file]

    # Solve both parths
    signal_strength, screen = run_clock_circuit(instructions)

    # Part 1 - 14620
    print(signal_strength)
    
    # Part 2 - BJFRHRFU
    print(screen)
