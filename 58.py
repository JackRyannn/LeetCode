# 返回最后一个单词的长度
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if s == '':
            return 0
        s = s.split(' ')
        while s[-1] == '':
            s.pop()
        return len(s[-1])
print Solution().lengthOfLastWord('  ')