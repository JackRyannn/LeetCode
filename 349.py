# 找出交集，用set去重复
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        r = []
        for i in nums1:
            if i in nums2:
                r.append(i)
        r = list(set(r))
        return r
