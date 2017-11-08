# 计算所有左叶子结点的和，深度遍历加一起即可。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    s = 0

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.dsf(root, False)
        return self.s

    def dsf(self, node, flag):
        if flag and not node.left and not node.right:
            self.s += node.val
        if node.left:
            self.dsf(node.left, True)
        if node.right:
            self.dsf(node.right, False)

