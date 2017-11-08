# 利用collection的Counter来找到第一个不重复的字母，即value = 1
import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        c = collections.Counter(s)
        for i in s:
            if c[i] == 1:
                return s.index(i)
        return -1

print Solution().firstUniqChar('loveleetcode')