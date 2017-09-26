# dic的index和set里的元素一样是不能重复的，而且dic可以记录对应的坐标
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False
print Solution().containsNearbyDuplicate([1,2,3,54,5,65,4543,423,43,3,324,23,4],3)