# BFS in undirected Graph

from collections import defaultdict
from queue import Queue

def add_edge_using_dict(neighbours, e1, e2):
    neighbours[e1].append(e2)
    neighbours[e2].append(e1)

def bfs(node, visited_nodes, neighbour_list):
    q = Queue()
    q.put(node)

    while not q.empty() :
        curr_node = q.get()
        print(curr_node)
        visited_nodes.add(curr_node) # Adding the first node to visited

        for neighbour in neighbour_list[curr_node] :
            if neighbour not in visited_nodes :
                q.put(neighbour)
                visited_nodes.add(neighbour) # Don't forget to add the new node inserted into the queue to the visited_nodes

vertices = 5
edges = [(1, 2), (1, 0), (2, 0), (2, 3), (2, 4)]

neighbours = defaultdict(list)

for e in edges:
    add_edge_using_dict(neighbours, e[0], e[1])

visited_nodes = set()

print('BFS of the Graph :')
bfs(1, visited_nodes, neighbours)