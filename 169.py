# 有一种o（n）的算法，前提是必须求majority element 的占比超过百分之五十，那么该数也肯定是序列中最长的一串，没有之一。
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return nums[len(nums)/2]

r = Solution().majorityElement([1,2,3,4,2,5,2,2,2,3])
print r