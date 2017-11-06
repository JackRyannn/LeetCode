# 穷举前10个数找到规律
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n % 4 == 0 else True
