"""
Written by Nat Getahun
Github username: nmgetahun
Email: nmgetahun@uchicago.edu

Advent of Code Day 10 Challenge:
https://adventofcode.com/2022/day/11
"""
# ------------------------------------------------------------------------------
import math

FUNCS = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y
}


class Monkey:
    def __init__(self, items, operation, operand, divisor):
        self.items = items
        self.divisor = divisor
        self.operation = operation
        self.operand = operand
        self.receivers = None
        self.inspections = 0


    def add_item(self, item):
        self.items.append(item)
    

    def set_receivers(self, t_monkey, f_monkey):
        self.receivers = (t_monkey, f_monkey)


    def has_items(self):
        return len(self.items) != 0


    def operate(self, part2mod):
        if self.operand[0]:
            item = self.operation(self.items[-1], self.operand[1])
        else:
            item = self.operation(self.items[-1], self.items[-1])

        if part2mod == False:
            self.test(item // 3)
        else:
            self.test(item % part2mod)

        self.inspections += 1
        del self.items[-1]


    def test(self, item):
        if item % self.divisor == 0:
            self.receivers[0].add_item(item)
        else:
            self.receivers[1].add_item(item)


# Parts 1 & 2 Primary (general function)
def execute(monkeys, rounds, part2mod = False):
    for _ in range(rounds):
        for monkey in monkeys:
            while monkey.has_items():
                monkey.operate(part2mod)
    
    monkey_inspections = [monkey.inspections for monkey in monkeys]
    monkey_inspections.sort()

    return monkey_inspections[-1] * monkey_inspections[-2]


# Generate list of Monkeys with corresponding attributes according to input file
def parse_monkeys():
    with open("input.txt") as file:
        file.seek(0, 2)
        eof = file.tell()
        file.seek(0, 0)

        monkeys1, monkeys2 = [], []
        throws = []
        while True:
            # Line 1
            file.readline()

            # Line 2
            items_raw = file.readline().replace(',', '').split()[2:]
            items = [int(item) for item in items_raw]

            # Line 3
            operator, operand = file.readline().split()[-2:]
            operation = FUNCS[operator]
            operand = (False,) if operand == "old" else (True, int(operand))
            
            # Lines 4-6
            divisor = int(file.readline().split()[-1])
            throws.append((
                int(file.readline().split()[-1]), 
                int(file.readline().split()[-1])
            ))

            # Add Monkey
            monkeys1.append(Monkey(items, operation, operand, divisor))
            monkeys2.append(Monkey(items[:], operation, operand, divisor))
            
            if file.tell() == eof:
                break
            file.readline()
        
        for i, (t, f) in enumerate(throws):
            monkeys1[i].set_receivers(monkeys1[t], monkeys1[f])
            monkeys2[i].set_receivers(monkeys2[t], monkeys2[f])
    
    return monkeys1, monkeys2


# Main
if __name__ == "__main__":
    monkeys1, monkeys2 = parse_monkeys()

    # Part 1
    rounds = 20
    print(f"Part 1: {execute(monkeys1, rounds)}")

    # Part 2
    rounds = 10000
    part2mod = math.prod(monkey.divisor for monkey in monkeys2)
    print(f"Part 2: {execute(monkeys2, rounds, part2mod)}")
