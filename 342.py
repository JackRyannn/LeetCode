# 用4.00做除数就可以得到float类型的数
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num >= 4:
            num /= 4.00
        return num == 1
