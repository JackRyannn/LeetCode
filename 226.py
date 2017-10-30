# 非常有意思的是，homebrew的作者因为没写出反转二叉树，google叫他fuck off～
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.dsf(root)
        return root

    def dsf(self, node):
        if not node:
            return
        node.left, node.right = node.right, node.left
        if node.left:
            self.dsf(node.left)
        if node.right:
            self.dsf(node.right)

