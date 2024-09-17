# Tree DFS - can be inorder / preorder / postorder

class TreeNode :
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def dfs(self, root):
        if not root :
            return
        print(root.val)
        self.dfs(root.left)
        self.dfs(root.right)

# Binary Tree : [3,9,20,null,6,15,7]

node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)
node6 = TreeNode(6)

node1.left = node2
node1.right = node3
node2.right = node6
node3.left = node4
node3.right = node5

print("DFS of the tree :")
node1.dfs(node1)

