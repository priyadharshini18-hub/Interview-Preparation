# Prims Minimum Spanning Tree

import heapq

def mst(adj_edges, start):
    explored = set()
    vertices = len(adj_edges.keys())
    mst_weight = 0
    mst_path = []
    pq = []

    heapq.heappush(pq, (0, start, -1))

    while pq and len(explored) < vertices :
        weight, node, parent = heapq.heappop(pq)

        if node in explored :
            continue

        explored.add(node)
        mst_weight += weight

        if parent != -1 :
            mst_path.append((weight, node, parent))

        for edge in adj_edges[node] :
            if edge[0] not in explored :
                heapq.heappush(pq, (edge[1], edge[0], node))

    return mst_path, mst_weight

adj_edges = {
    1 : [(2,28), (6,10)],
    2 : [(1,28), (3,16), (7,14)],
    3 : [(2,16), (4,12)],
    4 : [(3,12), (5,22), (7,18)],
    5 : [(6,25), (7,24), (4,22)],
    6 : [(1,10), (5,25)],
    7 : [(5,24), (2,14), (4,18)]
}

mst_path , mst_weight = mst(adj_edges, 1)

print('Minimum weight of the spanning tree is ', mst_weight)
print('Spanning Tree :')

for i in mst_path :
    print(i[1], '->', i[2], ' : ', i[0])