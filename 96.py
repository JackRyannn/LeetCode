# 用catalan公式C(2n,n)/(n+1)来计算二叉树的种类，除此之外，Catalan公式还可以计算很多关于种类的问题。
import math
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = (math.factorial(2*n)/pow(math.factorial(n),2))/(n+1)
        return int(ret)
print(Solution().numTrees(3))