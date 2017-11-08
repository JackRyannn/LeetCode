# 哇，做的第一道hard题，但这题很简单。。也就easy水平
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1 + nums2
        num.sort()
        r = 0
        if len(num) % 2 == 0:
            r = (num[len(num) / 2 - 1] + num[len(num) / 2] + 0.0) / 2
        else:
            r = num[len(num) / 2]
        return r
