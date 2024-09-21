# Breadth First Search in Binary Tree

from queue import Queue
# Inbuilt Queue is used instead of python list because
# inserting and deleting at the beginning position is O(n) in list
# as the other elements needs to be shifted right/left

class treeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

    def bfs(self, root, q):
        if not root :
            return
        q.put(root)
        while not q.empty() :
            curr_node = q.get()
            print(curr_node.val)
            if curr_node.left :
                q.put(curr_node.left)
            if curr_node.right :
                q.put(curr_node.right)

# Binary Tree : [3,9,20,null,6,15,7]

node1 = treeNode(3)
node2 = treeNode(9)
node3 = treeNode(20)
node4 = treeNode(15)
node5 = treeNode(7)
node6 = treeNode(6)

node1.left = node2
node1.right = node3
node2.right = node6
node3.left = node4
node3.right = node5

q = Queue()

print("BFS of the tree :")
node1.bfs(node1,q)

# Other Queue() functions : maxsize(), full(), qsize()



