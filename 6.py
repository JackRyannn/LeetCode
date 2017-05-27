# zigzag是蛇形排列，然后要把数据横着读出来，我是每行创造一个数组，按顺序填进去，然后横着读出来

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        a = []
        for r in range(numRows):
            a.append([])
        i = 0
        flag = True
        if numRows == 1:
            return s
        for item in s:
            if i == numRows :
                flag = False
                i -= 2
            elif i == -1:
                flag = True
                i += 2
            a[i].append(item)
            if flag:
                i += 1
            else:
                i -= 1
        ret = []
        for b in a:
            ret += b
        return "".join(ret)

s = Solution()
print(s.convert("abc",2))