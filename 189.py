# 题目中Rotate an array of n elements to the right by k steps.是说从右算k个元素，而且实际上超过len，会从1再次开始。
import copy
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < k:
            k = k-len(nums)
        if len(nums) == 1 or len(nums)<=k:
            return
        n2 = copy.deepcopy(nums)
        t = nums[len(nums)-k:]
        for i in range(k,len(nums)):
            nums[i] = n2[i-k]
        for j in range(k):
            nums[j] = t[j]
l = [1,2,3,4,5,6,7]
r = Solution().rotate(l,3)
print l