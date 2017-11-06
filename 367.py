# 367,采用牛顿迭代法来逼近方程的解，这也是求平方根的简便方法，把平方根的求解变成数学模型计算。
from math import ceil
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r = num
        while(r ** 2 > num):
            r = r - ceil(((r ** 2)-num)/2/r)
        return r ** 2== num

print Solution().isPerfectSquare(16)