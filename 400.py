# 挺麻烦的一道题，先确定n在哪个范围里，再确定n是范围内第几个数，再确定n是这个数的第几位。麻烦。
class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = 1
        s = 9
        while n > s:
            d += 1
            s += 9 * 10 ** (d-1) * d
        s -= 9 * 10 ** (d-1) * d - 1
        k = 10 ** (d-1) + (n - s)/d
        return int((str(k)[(n - s)%d]))

print Solution().findNthDigit(1000)