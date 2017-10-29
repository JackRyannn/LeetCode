# 一次做对，深度遍历
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    flag = False
    ss = 0

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.ss = sum
        self.dsf(root, 0)
        return self.flag

    def dsf(self, node, s):
        if not node:
            return
        s += node.val
        if not node.left and not node.right and s == self.ss:
            self.flag = True
        if node.left:
            self.dsf(node.left, s)
        if node.right:
            self.dsf(node.right, s)
        return
