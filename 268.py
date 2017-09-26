# 简单，都没写例子
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        nums = sorted(nums)
        for i in nums:
            if i != k:
                return i-1
            k += 1
        return i+1