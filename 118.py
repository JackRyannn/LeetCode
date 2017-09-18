# 简单
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        l = [[1]]
        for i in range(1,numRows):
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                    continue
                row.append(l[-1][j-1]+l[-1][j])
            l.append(row)
        return l

r = Solution().generate(0)
print r