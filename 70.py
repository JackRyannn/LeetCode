# 这道题很巧妙，其实就是斐波那契饿数列
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        p,q = 1,1
        t = 1
        for i in range(n-1):
            t = q
            q = p + q
            p = t
        return q
print Solution().climbStair9s(1)