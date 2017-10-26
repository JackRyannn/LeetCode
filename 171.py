#其实就是26进制转10进制而已
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss = s[::-1]
        sum = 0
        for i in range(len(ss)):
            sum += (ord(ss[i])-ord('A')+1)*(26**i)
        return sum


print Solution().titleToNumber('AB')