# 两层遍历即可
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(numbers)-1):
            if numbers[i] == 0 and target != 0:
                continue
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j] == target:
                    return [i+1,j+1]
                elif numbers[i]+numbers[j] >target:
                    break
        return []
print Solution().twoSum([-1,0],-1)