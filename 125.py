# 可以利用string.punctuation来去掉str里的标点符号
import string
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for c in string.punctuation:
            s = s.replace(c,'')
        s = s.lower().replace(' ','')
        ss = s[::-1]
        for i in range(len(s)):
            if s[i] != ss[i]:
                return False
        return True
print Solution().isPalindrome('A man, a plan, a canal: Panama')