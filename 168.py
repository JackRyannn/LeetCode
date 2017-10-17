# 利用余数来判断A-Z，但是Z的余数是0，实际上应该为26，所以代码要转换
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ''
        num = n
        if num <= 26:
            s += chr(ord('A')+num-1)
        else:
            while(num>26):
                k = num%26
                if k == 0:
                    k = 26
                s += chr(ord('A')+k-1)
                num = (num-1)/26
            s += chr(ord('A') + num-1)
        return s[::-1]

print Solution().convertToTitle(53)