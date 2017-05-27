class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = ['#']
        w = []
        for i in range(len(s)):
            l.append(s[i])
            l.append("#")
        for j in range(len(l)):
            p = j-1
            q = j+1
            count = 0
            while True:
                if p<0 or q>=len(l):
                    w.append(count)
                    break
                if l[p] == l[q]:
                    count += 1
                    p -= 1
                    q += 1
                else:
                    w.append(count)
                    break
        r = max(w)
        pos = w.index(max(w))
        ret = ''.join(l[pos-r+1:pos+r]).replace('#','')
        return ret

Solution().longestPalindrome("abcdedcbc")

