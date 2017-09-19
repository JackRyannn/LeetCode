# 阶乘肯定有偶数，偶数和5就可以凑成一个十，所以只要计算5的个数就行了，但是有的数不止含有一个5，比如25，所以要不断除以5，再求和。
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = n
        t = 0
        while s >= 5:
            t += s/5
            s = s/5
        return t
print Solution().trailingZeroes(24)