# 就是简单的一位一位算
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        ret = ['']
        for i in range(2*n):
            rets = []
            for r in ret:
                if r.count('(')<n:
                    if r.count('(') > r.count(')'):
                        r_new = r+')'
                        r = r+'('
                        rets.append(r)
                        rets.append(r_new)
                    else:
                        r = r + '('
                        rets.append(r)
                else:
                    while r.__len__()<2*n:
                        r = r+')'
                        rets.append(r)
            ret = rets
        return ret
print(Solution().generateParenthesis(3))
