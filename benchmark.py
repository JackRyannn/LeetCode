# coding=utf-8
import copy
# 字典序排序方法： 因为从左到右依次递减的序列是无法找到更大的（下一个序列），所以方法是从右到左找小于右边的数，然后和右边比他大一点的数交换，然后把交换位置右边的数都reverse(这样序列是比刚刚大的最小的序列了）。
# i是右边比j大的数中最小的，j是不停和i比较的数,k是为了帮助找到那个正确的i
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i,j = len(nums)-1,len(nums)-1
        while j>0:
            j -= 1
            if nums[j]<nums[i]:
                k = len(nums)-1
                while k>j:
                    if nums[k]<nums[i] and nums[k]>nums[j]:
                        i = k
                    k -= 1
                nums[i] = nums[i]^nums[j]
                nums[j] = nums[j]^nums[i]
                nums[i] = nums[i]^nums[j]
                b = nums[j+1:len(nums)]
                b.reverse()
                for n in range(j+1,len(nums)):
                    nums[n] = b[n-j-1]
                return
            elif nums[j]>nums[i]:
                i = j
        nums.reverse()
l = [2,3,1,3,3]
ret = Solution().nextPermutation(l)
print(l)
