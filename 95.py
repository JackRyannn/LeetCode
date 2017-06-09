# 动态规划问题，采用递归的方法，把每个点左右可能出现的情况组合在一起，自底向上。注意边界问题。
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n<=0:
            return []
        return self.genTree(1,n)
    def genTree(self,start,end):
        ret = []
        if start>end:
            ret.append(None)
            return ret
        for i in range(start,end+1):
            leftchild = self.genTree(start,i-1)
            rightchild = self.genTree(i+1,end)
            for item in leftchild:
                for item2 in rightchild:
                    root = TreeNode(i)
                    root.left = item
                    root.right = item2
                    ret.append(root)
        return ret
print(Solution().generateTrees(0))