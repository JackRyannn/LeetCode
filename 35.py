# 一次成功
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        return i+1
l = [1,3,4,5]
r = Solution().searchInsert(l,20)
print r