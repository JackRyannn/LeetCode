# 一次做对
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        while(i<len(nums)):
            if nums[i] == 0:
                j = i
                while(j<len(nums)):
                    if nums[j] != 0:
                        nums[i] ^= nums[j]
                        nums[j] ^= nums[i]
                        nums[i] ^= nums[j]
                        break
                    j += 1
            i += 1





print Solution().moveZeroes([0,1,0,3,12,0])