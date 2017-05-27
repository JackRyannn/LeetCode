class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        for i in s:
            if i =='(' or i == '[' or i =='{':
                l.append(i)
            else:
                p = l.pop()
                if p == '(' and i == ')':
                    continue
                elif p == '[' and i == ']':
                    continue
                elif p == '{' and i == '}':
                    continue
                else:
                    return False
        if l:
            return False
        else:
            return True
print(Solution().isValid('[}'))