# 利用2的次方的二进制结构都是1后面接n个零
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = str(bin(n))
        if n > 0 and s.count('1')==1 and len(s)>2:
            return True
        return False
print Solution().isPowerOfTwo(-16)