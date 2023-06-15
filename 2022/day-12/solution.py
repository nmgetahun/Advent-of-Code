"""
Written by Nat Getahun
Github username: nmgetahun
Email: nmgetahun@uchicago.edu

Advent of Code Day 12 Challenge:
https://adventofcode.com/2022/day/12
"""
# ------------------------------------------------------------------------------
import math
from utils import Vertex, Graph, MinHeap

def a_star(gr, start, end):
    # Instantiate priority queue and visited set to maintain while iterating
    prio_queue = MinHeap()
    visited = set()
    current = start
    assign_costs(start, compute_costs(start, start, end))
    prio_queue.insert(start.f_cost, start)

    while not prio_queue.is_empty():
        current = prio_queue.remove_min()[1]
        visited |= {current}
        if current == end:
            # Found end vertex, can stop iterating
            break
        
        for neighbor in current.adjacent:
            if neighbor not in visited:
                h, g, f = compute_costs(neighbor, current, end, 1)
                if f < neighbor.f_cost:
                    # Only proceed if new costs are lower (more efficient path)
                    assign_costs(neighbor, (h, g, f))
                    neighbor.predecessor = current

                    # Add or change position of neighbor in priority queue
                    if neighbor in prio_queue.index_of_item:
                        #print("changing_prio: ", vertex.x, vertex.y, chr(vertex.elevation))
                        prio_queue.change_priority(neighbor, neighbor.f_cost)
                    else:
                        prio_queue.insert(neighbor.f_cost, neighbor)

    if current != end:
        # No path from start to end vertex
        return None

    min_distance = current.g_cost
    graph.reset_costs()
    return min_distance

def assign_costs(vertex, costs):
    h, g, f = costs
    vertex.h_cost = h
    vertex.g_cost = g
    vertex.f_cost = f

def compute_costs(vertex, current, end, distance = 1):
    h_cost = abs(end.x - vertex.x) + abs(end.y - vertex.y)
    g_cost = (current.g_cost + distance) if vertex != current else 0
    f_cost = h_cost + g_cost
    return (h_cost, g_cost, f_cost)



# Main
if __name__ == "__main__":
    raw_graph = []
    x, y = 0, 0
    start, end = None, None
    with open("input.txt") as file:
        for line in file:
            x = 0
            for char in line.strip():
                if char == 'S':
                    start = Vertex(x, y, ord('a'), True)
                    raw_graph.append(start)
                elif char == 'E':
                    end = Vertex(x, y, ord('z'), False, True)
                    raw_graph.append(end)
                else:
                    raw_graph.append(Vertex(x, y, ord(char)))

                x += 1
            y += 1

        graph = Graph(x, y)

        for vertex in raw_graph:
            graph.add_vertex(vertex)

        graph.validate_vertices()

        print(f"Part 1: {a_star(graph, start, end)}")
        
        
        min_a = math.inf
        for i, vertex in enumerate(graph.a_vertices):
            a = a_star(graph, vertex, end)
            if a is not None and a < min_a:
                min_a = a

        print(f"Part 2: {min_a}")
