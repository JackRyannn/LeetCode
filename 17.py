# 这是做了这么多leetcode里第一次一次性通过的题！Fighting！
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        l = ['']
        digit = list(digits)
        strs = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        for i in digit:
            ll = []
            for s in l:
                for item in strs[int(i)-2]:
                    k = s + item
                    ll.append(k)
            l = ll
        return l

print(Solution().letterCombinations('23'))