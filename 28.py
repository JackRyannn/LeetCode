# 边界好麻烦
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i,j = 0,0
        ret = -1
        if not haystack and needle:
            return -1
        if not needle:
            return 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                if j == 0:
                    ret = i
                j += 1
                if j == len(needle):
                    break
            else:
                if ret != -1:
                    i = ret
                j = 0
                ret = -1
            i += 1
        if j !=len(needle):
            return -1
        return ret
print(Solution().strStr('a','a'))


