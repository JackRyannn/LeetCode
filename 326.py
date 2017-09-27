# 其中1162261467是大于int最大范围的，必能整出3的次方
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and 1162261467%n==0