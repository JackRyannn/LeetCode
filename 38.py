# 这道题的意思是读取上一行的数列，比如1211，那么这一行就为11 12 21，分别是统计上一行相同元素的个数
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        t = []
        t.append('1')
        for i in range(0,n):
            item = t[i][0]
            count = 0
            s = ''
            for j in t[i]:
                if j == item:
                    count += 1
                else:
                    s += str(count)+item
                    item = j
                    count = 1
            s += str(count) + item
            t.append(s)
        return t[n-1]


print Solution().countAndSay(5)