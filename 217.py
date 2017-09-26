# 用不含重复元素的set类型转换，再比较长度
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        r = False
        if len(set(nums)) == len(nums):
            return False
        return True
print Solution().containsDuplicate([1,2,3])