"""
Written by Nat Getahun
Github username: nmgetahun
Email: nmgetahun@uchicago.edu

Advent of Code Day 8 Challenge:
https://adventofcode.com/2022/day/8
"""
# ------------------------------------------------------------------------------
import time

# Part 1 Function
def find_visible():
    visible_master = set()
    row_len = len(forest[0])
    for i, row in enumerate(forest):
        col = [line[i] for line in forest]
        visible_trees_horizontal = [((i, 0), row[0])]
        visible_trees_vertical = [((0, i), col[0])]

        # Traverse row left to right
        for k, tree in enumerate(row):
            if tree > visible_trees_horizontal[-1][1]:
                visible_trees_horizontal.append(((i, k), tree))

        # Traverse row right to left
        visible_trees_horizontal.append(((i, row_len - 1), row[-1]))
        for k, tree in enumerate(row[::-1]):
            if tree > visible_trees_horizontal[-1][1]:
                visible_trees_horizontal.append(((i, row_len - k - 1), tree))

        # Traverse col top to btm
        for k, tree in enumerate(col):
            if tree > visible_trees_vertical[-1][1]:
                visible_trees_vertical.append(((k, i), tree))

        # Traverse col btm to top
        visible_trees_vertical.append(((row_len - 1, i), col[-1]))
        for k, tree in enumerate(col[::-1]):
            if tree > visible_trees_vertical[-1][1]:
                visible_trees_vertical.append(((row_len - k - 1, i), tree))

        visible_master = visible_master | set(visible_trees_horizontal) | set(visible_trees_vertical)

    return len(visible_master)


# Part 2 Function
def calculate_scenic_scores():
    max_scenic_score = -1
    best_tree = None
    for i in range(1, len(forest) - 1):
        for k in range(1, len(forest[0]) - 1):
            tree = forest[i][k]
            scenic_score = [0, 0, 0, 0]

            # Look left
            for n in range(1, i + 1):
                scenic_score[0] += 1
                if tree <= forest[i - n][k]: break

            # Look right
            for n in range(i + 1, len(forest)):
                scenic_score[1] += 1
                if tree <= forest[n][k]: break

            # Look up
            for n in range(1, k + 1):
                scenic_score[2] += 1
                if tree <= forest[i][k - n]: break

            # Look down
            for n in range(k + 1, len(forest[0])):
                scenic_score[3] += 1
                if tree <= forest[i][n]: break

            score = scenic_score[0] * scenic_score[1] * scenic_score[2] * scenic_score[3]
            if score > max_scenic_score:
                max_scenic_score = score
                best_tree = ((i, k), tree)

    # print("Best Tree: ", best_tree)
    return max_scenic_score


# Main
if __name__ == "__main__":
    # Get data from today's AoC input file
    with open("input.txt") as file:
        forest = [[n for n in line.strip()] for line in file]
    
    # time my solution
    start = time.time()
    for _ in range(100):
        # Part 1 - 1814
        num_visible_trees = find_visible()
        # print("Part 1: ", num_visible_trees)

        # Part 2 - 330786
        highest_scenic_score = calculate_scenic_scores()
        # print("Part 2: ", highest_scenic_score)
        
    print("my time: ", time.time() - start) # 4.747s

    # time an alternate solution
    start = time.time()
    for _ in range(100):
        # Alternatively, could have transposed the forest and only traversed rows:
        forest2 = list(zip(*forest))

        # Part 1
        s = 0
        for i in range(len(forest[0])):
            for j in range(len(forest)):
                tree = forest[i][j]
                if all(x < tree for x in forest[i][0:j]) or \
                    all(x < tree for x in forest[i][j+1:]) or \
                    all(x < tree for x in forest2[j][0:i]) or \
                    all(x < tree for x in forest2[j][i+1:]):
                    s += 1
        # print(s)

        # Part 2
        s = 0

        def view_length(tree, view):
            view_length = 0
            for v in view:
                view_length += 1
                if v >= tree:
                    break
            return view_length

        for i in range(len(forest[0])):
            for j in range(len(forest)):
                tree = forest[i][j]

                s1 = view_length(tree, forest[i][0:j][::-1])
                s2 = view_length(tree, forest[i][j+1:])
                s3 = view_length(tree, forest2[j][0:i][::-1])
                s4 = view_length(tree, forest2[j][i+1:])
                score = s1 * s2 * s3 * s4
                if score > s:
                    s = score
        # print(s)

    print("alternate time: ", time.time() - start) # 8.026s
