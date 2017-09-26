# ^异或满足交换律，3^5^3 = 5 可以消去所有成对出现的元素！
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        for i in nums:
            s ^= i
        return s

print Solution().singleNumber([1,2,1,2,3])