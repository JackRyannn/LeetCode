# HappyNum 是 每位平方后相加，反复重复如果结果为1，就是HappyNum，如果无限循环，就不是。
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        t = n
        flag = False
        j = 0
        while j != 100:
            s = str(t)
            t = 0
            for i in s:
                t += int(i) ** 2
            if t == 1:
                return True
            j += 1
        return False
