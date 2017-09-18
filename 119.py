# 简单
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]
        l = [[1]]
        for i in range(1,rowIndex+1):
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                    continue
                row.append(l[-1][j-1]+l[-1][j])
            l.append(row)
        return l[rowIndex]

r = Solution().getRow(3)
print r