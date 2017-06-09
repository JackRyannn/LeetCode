# all 是判断所有的元组都满足x<y则返回True，zip是合成新的元组，其实就是前一位和后一位组成新元组，再用all判断。这是用简洁的方法判断是否递增
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    l = []
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.helper(root)
        if  all(x<y for x, y in zip(self.l, self.l[1:])):
            return True
        else:
            return False

    def helper(self,node):
        if node:
            self.helper(node.left)
            self.l.append(node.val)
            self.helper(node.right)


t1 = TreeNode(0)
# t2 = TreeNode(0)
# t1.left = t2
print(Solution().isValidBST(t1))
