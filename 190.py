# 用bin（）转成二进制，注意把前面0b去掉，然后补到32位标准型，通过【：：-1】翻转，再转换成int型10进制
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = str(bin(n))[2:]
        for i in range(32-len(s)):
            s = '0'+s
        s = s[::-1]
        t = int(s,2)
        return t

print Solution().reverseBits(43261596)