# public class Solution {
# public int maxProfit(int[] prices) {
#     int total = 0;
#     for (int i=0; i< prices.length-1; i++) {
#         if (prices[i+1]>prices[i]) total += prices[i+1]-prices[i];
#     }
#
#     return total;
# }
# 极其简单的方法，只是不符合题目逻辑，比如3，4，5。我3买入，5卖出，最划算，但是我只考虑每两天的，3买入4卖出4买入5卖出，结果是相同的。
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