# DFS in undirected Graph

def add_edge(adj, s, t):
    adj[s].append(t)
    adj[t].append(s)

def dfs(node, visited, adj):
    visited[node] = 1
    print(node)

    for link in adj[node] :
        if visited[link] != 1 :
            dfs(link, visited, adj)

# Input for Graph

vertices = 5
edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]

adj = [[] for _ in range(vertices)] # Adjacent list representing the links / connections from each node
visited = [0]*vertices

for e in edges:
    add_edge(adj,e[0],e[1])

print('DFS of the Graph :')

dfs(1, visited, adj)



