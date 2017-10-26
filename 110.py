# 通过深度遍历，访问每个节点并通过左右高度判断该点是否平衡，把该点高度返回给父节点
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    flag = True

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return self.flag
        self.dfs(root)
        return self.flag

    def dfs(self, node):
        if not node:
            return 0
        l, r = 0, 0
        if node.left:
            l = self.dfs(node.left)
        if node.right:
            r = self.dfs(node.right)
        if abs(l - r) > 1:
            self.flag = False
        return max(l, r) + 1

