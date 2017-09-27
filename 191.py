# 超简单一次过
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(bin(n))
        return s.count('1')

print Solution().hammingWeight(11)