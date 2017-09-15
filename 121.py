# 这应该就是动态规划的思想吧，每一步都计算状态，最后找到最好的状态。
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        mi = prices[0]
        profit = 0
        for i in prices[1:]:
            if i<mi:
                mi = i
                continue
            if profit < i - mi:
                profit = i - mi
        return profit

l = [7, 1, 5, 3, 6, 4]
r = Solution().maxProfit(l)
print r