class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        for i in range(l):
            for j in range(l):
                if i == j:
                    continue
                if target == (nums[i]+nums[j]):
                    List = []
                    List.append(i)
                    List.append(j)
                    print(i,j)
                    return List
# nums = [3,3]
# target = 6
# s = Solution()
# s.twoSum(nums,target)

