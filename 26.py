# 不能申请新的空间，就要充分利用给定空间。每出现一个非重复元素就依次存到前面，反正不会覆盖有用的数据
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        c = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if c != nums[i]:
                c = nums[i]
                nums[count] = nums[i]
                count+=1
        return count
n = [1,1,2,2,2,3,3]
print(Solution().removeDuplicates(n))
print(n)