# In Order traversal of Binary tree

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        delf.val = val
        self.left = left
        self.right = right

    def InorderTraversal(root):
        if not root:
            return
        print(root.val)
        InorderTraversal(root.left)
        InorderTraversal(root.right)


# Binary Tree : [3,9,20,null,null,15,7]

node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

root = node1

InorderTraversal(root)