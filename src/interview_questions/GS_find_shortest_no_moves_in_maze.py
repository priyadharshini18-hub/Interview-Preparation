# Find min no. of moves to complete a maze

# min moves in which hacker man can reach the cell (n-1, m-1) starting from (0,0)
# Return -1 if its impossible
# Hacker man can cover k distance in one move

# Algorithm : Shortest moves - BFS
#
# Create a queue to store (x,y,moves) and a set visited to store (x,y)
# Initialize Directions : (right, down, left, up)
# Add (0,0,moves) in queue and (0,0) in visited
# Loop while queue is not empty :
#     Pop x,y,moves from queue
#     Loop through the directions to move to new x, new y :
#         Loop again k times - (1,k) :
#             Calculate new x, new y
#             Check if new x, new y are inside the range and the value == 0 :
#                 YES -> Add to queue(new x,y,moves+1), visited(new x,y)
#                 No -> Break
# Return -1 : If not found


from queue import Queue

def bfs(maze, n, m, k):
    visited = set() # Track the coordinated visited
    moves = 0
    q = Queue()
    q.put((0, 0, moves))
    visited.add((0,0))
    directions = [(1,0), (0,1), (-1,0), (0,-1)]

    if maze[0][0] == 1 or maze[n-1][m-1] == 1 :
        return -1

    while not q.empty() :
        x, y, moves = q.get()
        if x == n-1 and y == m-1 :
            return moves

        for dx, dy in directions :
            for step in range(1, k) :
                new_x = x + dx * step
                new_y = y + dy * step

                if new_x >= 0 and new_x < n and new_y >= 0 and new_y < m and maze[new_x][new_y] == 0 :
                    if (new_x, new_y) not in visited :
                        q.put((new_x, new_y, moves+1))
                        visited.add((new_x, new_y))
                else :
                    break
    return -1


maze = [[0,0,0],[1,0,0]]
n = len(maze)
m = len(maze[0])
k = 5

print('Min moves for the Hacker man to finish the maze : ', bfs(maze, n, m, k))


# Test case 1
# n=2, m=3
# maze = [[0,0,0],[1,0,0]]
# k=5
# res = 2

# Testcase 2
# n=2, m=2
# maze=[[0,0],[1,0]]
# k=2
# res=2



