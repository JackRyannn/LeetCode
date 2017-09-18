class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = False
        if digits[-1] == 9:
            digits[-1] = 0
            flag = True
        else:
            digits[-1] += 1
        i = 2
        while flag and i <= len(digits):
            if digits[-i] == 9:
                digits[-i] = 0
            else:
                digits[-i] += 1
                flag = False
            i += 1
        if flag:
            digits.insert(0,1)
        return digits
l = [1,0,0]
r = Solution().plusOne(l)
print r