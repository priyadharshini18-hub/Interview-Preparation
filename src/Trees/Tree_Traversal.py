# In Order traversal of Binary tree

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def PreorderTraversal(self, root):
        if not root:
            return
        print(root.val)
        self.PreorderTraversal(root.left)
        self.PreorderTraversal(root.right)

    def InorderTraversal(self, root):
        if not root:
            return
        self.InorderTraversal(root.left)
        print(root.val)
        self.InorderTraversal(root.right)

    def PostorderTraversal(self, root):
        if not root:
            return
        self.PostorderTraversal(root.left)
        self.PostorderTraversal(root.right)
        print(root.val)

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

print('PreorderTraversal of the Tree :')
node1.PreorderTraversal(node1)
print('InorderTraversal of the Tree :')
node1.InorderTraversal(node1)
print('PostorderTraversal of the Tree :')
node1.PostorderTraversal(node1)