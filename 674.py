# 简单
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        item = nums[0]
        count = 0
        m = 0
        for i in nums:
            if i > item:
                count += 1
            else:
                count = 0
            item = i
            print m,count
            m = count if count > m else m
        return m+1
print Solution().findLengthOfLCIS([1,3,5,4,2,3,4,5])