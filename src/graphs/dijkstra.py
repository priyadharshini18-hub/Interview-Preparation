# Shortest path in weighted graph
from collections import defaultdict
import heapq

def dijkstra(dict_edges, source, destination):
    path = dict()
    pq = []
    distance = {i: float('inf') for i in dict_edges.keys()}

    # Assign distance=0 for source and add to PQ
    distance[source] = 0
    heapq.heappush(pq, (0, source))

    while pq :
        curr_dist, curr_v = heapq.heappop(pq)

        if curr_dist > distance[curr_v] :
            continue

        for edge in dict_edges[curr_v] :
            new_dist = edge[1] + distance[curr_v]
            if new_dist < distance[edge[0]] :
                distance[edge[0]] = new_dist
                path[edge[0]] = curr_v
                heapq.heappush(pq, (new_dist, edge[0]))

    return distance, path

vertices = [[0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 1, 1, 0],
         [0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0]]

edges = [[0, 4, 5, 2, 0, 0, 0],
         [0, 0, 0, 0, 3, 0, 0],
         [0, 0, 0, 0, 0, 3, 0],
         [0, 1, 0, 0, 5, 5, 0],
         [0, 0, 0, 0, 0, 0, 2],
         [0, 0, 0, 0, 0, 0, 3],
         [0, 0, 0, 0, 0, 0, 0]]

rows = len(edges)
cols = len(edges[0])
dict_edges = defaultdict(list) # Convert adjacency matrix into dict

for i in range(rows) :
    for j in range(cols):
        if edges[i][j] != 0 :
            dict_edges[i].append((j,edges[i][j]))

# Ensure all vertices are present as keys in dict_edges, even though there are no outgoing edges
for i in range(rows):
    if i not in dict_edges:
        dict_edges[i] = []

distance, paths = dijkstra(dict_edges, 0, 6)

print('Shortest distance from 0-6 is ', distance[6])

i = 6
shortest_path = [6]

while i != 0 : # Backtrack
    prev = paths[i]
    shortest_path.append(prev)
    i = prev

shortest_path.reverse()
print('Shortest path from 0-6 is ', shortest_path)







