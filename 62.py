# 走出独一无二的路径的个数，采用组合C，编程简单但是不好想。
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if n == 1 or m == 1:
            return 1
        p = n-1
        q = m+n-2
        r = 1
        for i in range(p+1,q+1):
            r *= i
        for i in range(1,q - p + 1):
            r /= i
            print(i)
        return r
print(Solution().uniquePaths(3,7))