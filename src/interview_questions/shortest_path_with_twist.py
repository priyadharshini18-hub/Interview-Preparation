# BFS in undirected Graph

# Question:
# A country has multiple cities which are represented as vertices of a graph and cities are interconnected.
# These roads are represented as undirected edges between the vertices with unit weight (same weight for all roads).
# Now calculate the shortest path between 'A' to 'B' such that you are travelling in a car with a capacity of 'c'.
# There are only few cities which have fuel stations where you can fill the car to complete capacity (when you visit that vertex).
# When you travel from one city to another you consume a unit of fuel and at the source city you start with full capacity of fuel.


# Sample Input:
# Roads: [[1,2],[2,3],[3,4],[4,5],[4,6],[6,7]]
# A: 1, B: 7, capacity 'c': 4
# fuel stations: [5]

# Sample Output:
# 7 (as shortest path is 1-2-3-4-5-4-6-7)

from collections import defaultdict
from queue import Queue

def add_edge_using_dict(neighbours, e1, e2):
    neighbours[e1].append(e2)
    neighbours[e2].append(e1)

def bfs(node, dest, visited_nodes, neighbour_list, fuel_stations, capacity):
    q = Queue()
    q.put((node, capacity, []))

    while not q.empty():
        curr_node, curr_cap, path = q.get()

        path = path + [curr_node]

        if curr_node == dest:
            print('Shortest Path is ', path)
            print('Length of Shortest Path :', len(path)-1)
            return

        visited_nodes.add((curr_node, curr_cap))

        for neighbour in neighbour_list[curr_node]:
            if neighbour in fuel_stations:
                new_cap = capacity
            else:
                new_cap = curr_cap - 1

            # print('new cap : ', new_cap, 'neighbour : ', neighbour)
            if new_cap > 0 and (neighbour, new_cap) not in visited_nodes:
                q.put((neighbour, new_cap, path))

vertices = 5
edges =  [(1,2),(2,3),(3,4),(4,5),(4,6),(6,7)]
# edges = [(1, 2), (2, 11), (11, 12), (12, 13), (13, 14), (2, 3), (3, 4), (4, 5), (4, 6), (6, 7)]

neighbours = defaultdict(list)

for e in edges:
    add_edge_using_dict(neighbours, e[0], e[1])

visited_nodes = set()

print('BFS of the Graph :')
bfs(1, 7, visited_nodes, neighbours, [5], 4)








