# 
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        t = []
        s = list(s)
        v = ['a','e','i','u','o','A','E','I','U','O']
        for i in range(len(s)):
            if s[i] in v:
                t.append(s[i])
                s[i] = '$'
        t.reverse()
        for j in range(len(s)):
            if s[j] == '$':
                s[j] = t[0]
                t.pop(0)
        return ''.join(s)



print Solution().reverseVowels('leetcode')