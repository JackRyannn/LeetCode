# 判断树是否对称，用递归的方式判断
#  Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.func(root.left,root.right)

    def func(self,l,r):
        if not l and not r:
            return True
        if (not l and r) or (l and not r) or l.val != r.val :
            return False
        return self.func(l.left,r.right) and self.func(l.right,r.left)



n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(2)
n1.right = n2
n1.left = n3
print(Solution().isSymmetric(n1))