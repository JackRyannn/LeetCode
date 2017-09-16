class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        flag = True
        mi = prices[0]
        ma = 0
        profit = 0
        last = 0
        for i in prices[1:]:
            last = i
            if i<mi:
                if flag and ma>=mi:
                    profit += ma - mi
                    ma = 0
                mi = i
                flag = True
                continue
            ma = max(ma, i)
            if i < ma:
                profit += ma - mi
                mi,ma = i,0
                flag = True
        if flag:
            profit += last - mi
        return profit if profit>0 else 0

l = [9,9,0,3,0,7,7,7,4,1,5,0,1,7]
r = Solution().maxProfit(l)
print r