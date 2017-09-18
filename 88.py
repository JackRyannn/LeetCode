class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        while len(nums1)>m:
            nums1.pop()
        for i in range(n):
            while j<len(nums1) and nums2[i]>nums1[j]:
                j += 1
            nums1.insert(j,nums2[i])

array1 = [0]
r = Solution().merge(array1,0,[1],1)
print array1