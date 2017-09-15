# 求连续子序列的最大值，可以先求到i点的连续子序列之和的最大值，然后再求出每个点对应的最大值，即为所求。
class Solution:
    # @param A, a list of integers
    # @return an integer
    # 6:57
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum

l = [-2,1,-3,4,-1,2,1,-5,4]
r = Solution().maxSubArray(l)
print r
