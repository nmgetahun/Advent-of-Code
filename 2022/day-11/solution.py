"""
Written by Nat Getahun
Github username: nmgetahun
Email: nmgetahun@uchicago.edu

Advent of Code Day 10 Challenge:
https://adventofcode.com/2022/day/11
"""
# ------------------------------------------------------------------------------

class Monkey:
    def __init__(self, items, operation, divisor):
        self.items = items
        self.divisor = divisor
        self.operation = operation
        self.receivers = None
        self.inspections = 0


    def add_item(self, item):
        self.items.append(item)
    

    def update_receivers(self, t_monkey, f_monkey):
        self.receivers = (t_monkey, f_monkey)


    def has_items(self):
        return len(self.items) != 0


    def operate(self):
        item = self.operation(self.items[-1])
        del self.items[-1]
        self.test(item)


    def test(self, item):
        if item % self.divisor == 0:
            self.receivers[0].add_item(item)
        else:
            self.receivers[0].add_item(item)
        



# Main
if __name__ == "__main__":
    with open("input.txt") as file:
        file.seek(0, 2)
        eof = file.tell()
        file.seek(0, 0)

        monkeys = []
        while file.tell() != eof:
            for _ in range(6):
                file.readline()
                items_raw = file.readline().replace(',', '').split()[2:]
                items = [int(item) for item in items_raw]
                
