"""
Written by Nat Getahun
Github username: nmgetahun
Email: nmgetahun@uchicago.edu

Advent of Code Day 13 Challenge:
https://adventofcode.com/2022/day/13
"""
# ------------------------------------------------------------------------------

def compare(lst1, lst2, i = 0):
    while i < len(lst1):
        if (i == len(lst2)):
            return 0
    
        if type(lst1[i]) == type(lst2[i]) == int:
            if lst1[i] < lst2[i]:
                return 1
            elif lst1[i] > lst2[i]:
                return 0
        
        elif type(lst1[i]) == type(lst2[i]) == list:
            if compare(lst1[i], lst2[i]) == 0:
                return 0

        else:
            if type(lst1[i]) == list:
                if compare(lst1[i], [lst2[i]]) == 0:
                    return 0
            else:
                if compare([lst1[i]], lst2[i]) == 0:
                    return 0
            
        i += 1

    return 1

# Main
if __name__ ==  "__main__":
    with open("input.txt") as file:
        lists = [eval(line.strip()) for line in file if line != "\n"]
        sum = 0
        for i in range(0, len(lists), 2):
            sum += (i // 2 + 1) * compare(lists[i], lists[i + 1])
        
        print(sum)