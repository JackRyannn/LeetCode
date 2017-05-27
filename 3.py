# 把出现过的字符和对应最新的位置都保存到字典里，然后循环遍历每个字符，当出现重复的字符，并且该字符在当前子字符串中出现过，则以此为新起点
# 否则计算当前子字符串长度，并保存最大长度。

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxLen = 0
        usedChar = {}
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLen = max(maxLen,i-start+1)
            usedChar[s[i]] = i
        return maxLen

s = Solution()
i = s.lengthOfLongestSubstring("pwwkew")
print(i)