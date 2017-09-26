# 之前学到的套路贼好用，用异或来找出唯一没有重复的！
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        k = 0
        for i in s:
            k ^= ord(i)
        for j in t:
            k ^= ord(j)
        return chr(k)

print Solution().findTheDifference('abcd','abecd')