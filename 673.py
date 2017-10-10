# 动态规划非常好的一道题 这道题求最长递增序列有几条 在一串数列中，前后都有可能出现最长序列 而且每一点对应的最长序列都和前面点相关
# 这里记录了dp两个值，分别是当前index对应的最长序列，当前index对应的最长序列条数
# 最后要用sum把所有符合长度条件的点对应的条数相加即为所求。 注意下面的写法还是非常简洁，可以借鉴
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[1,1] for i in range(len(nums))]
        longest = 1
        for i,num in enumerate(nums):
            curr_longest, count = 1, 0
            for j in range(i):
                if num>nums[j]:
                    curr_longest = max(curr_longest,dp[j][0]+1)
            for j in range(i):
                if dp[j][0] == curr_longest - 1 and nums[j] < num:
                    count += dp[j][1]
            dp[i] = [curr_longest, max(count, dp[i][1])]
            longest = max(longest,curr_longest)
        return sum(item[1] for item in dp if item[0] == longest)




print Solution().findNumberOfLIS([1,2,4,3,5])