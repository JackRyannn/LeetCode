# 做的很乱没有头绪，不停给自己挖坑然后再补，效率很低。
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        flag =False
        lo,hi = 0,len(nums)-1
        ret = [lo,hi]
        if len(nums) == 0:
            return [-1,-1]
        if lo == hi:
            return [0,0] if nums[0] == target else [-1,-1]
        while lo<=hi-1:
            mid = (lo+hi)/2
            if nums[mid]<target:
                lo = mid
            if nums[mid]>=target:
                hi = mid
            if lo == hi - 1:
                break
        if nums[hi-1] == target and hi>0:
            hi -= 1
        ret[0] = hi
        lo,hi = 0,len(nums)-1
        while lo<=hi-1:
            mid = (lo+hi)/2
            if nums[mid]>target:
                hi = mid
            if nums[mid]<=target:
                lo = mid
            if lo == hi - 1:
                break
        if nums[lo+1] == target and lo<len(nums)-1:
            lo += 1
        ret[1] = lo
        print ret
        if nums[ret[0]]==target and nums[ret[1]]==target:
            return ret
        else:
            return [-1,-1]


l = [2,2]
r = Solution().searchRange(l,2)
print r