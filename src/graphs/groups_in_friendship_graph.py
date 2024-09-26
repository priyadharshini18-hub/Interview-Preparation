# Given n friends and their friendship relations
# Find the total number of groups that exist
# And the number of ways of new groups that can be formed consisting of people from every existing group.
# If no relation is given for any person then that person has no group and singularly forms a group.

from collections import defaultdict

def create_adj(adj, f1, f2):
    adj[f1].append(f2)
    adj[f2].append(f1)

def dfs(index, adj, visited_friend):
    count = 1
    for friend in adj[index] :
        if friend not in visited_friend :
            visited_friend.add(friend)
            count = count + dfs(friend, adj, visited_friend) # Counts the number of friends in the current DFS
    return count

# Input

n = 6
friendships =[(1,2), (3,4), (5,6)]

adj = defaultdict(list)
visited_friend = set()

for i in friendships :
    create_adj(adj, i[0], i[1])

for i in adj.items() :
    print(i)

existing_group = 0
new_group = 1

for i in range(1,n+1):
    if i not in visited_friend : # Call DFS until all the items are visited
        visited_friend.add(i)
        existing_group += 1
        grp_size = dfs(i, adj, visited_friend)
        new_group = new_group * grp_size # New groups that can be formed : Product of size of each group


if existing_group == 1 :
    new_group = 0

print("Existing friends group : " , existing_group)
print("New friends group : " , new_group)

