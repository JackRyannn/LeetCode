# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.recursion(root)

    def recursion(self,node):
        if not node:
            return 0
        return max(self.recursion(node.left),self.recursion(node.right))+1



n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(2)
n1.right = n2
n2.left = n3
print(Solution().maxDepth(n1))