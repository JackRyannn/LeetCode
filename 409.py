# 409好好利用Counter
import collections
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = collections.Counter(s);
        num = 0
        flag = 0
        for i in c.values():
            if i % 2 == 0:
                num += i
            else:
                num += i-1
                flag = 1
        return num + flag

print(Solution().longestPalindrome('ccc'))