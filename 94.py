# 中序遍历
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    l = []
    def func(self, node):
        if not node:
            return
        self.func(node.left)
        self.l.append(node.val)
        self.func(node.right)

    def inorderTraversal(self, root):
        self.l = []
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.func(root)
        return self.l


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n = TreeNode(4)
n1.right = n2
n2.left = n3
print(Solution().inorderTraversal(n))