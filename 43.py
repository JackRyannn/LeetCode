# 计算大数乘法，就是说两个数超过了整数类型取值范围，做法就是简化成我们平时按位计算然后相加。
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l = []
        sum = 0
        for i in range(1,len(num2)+1):
            l.append(int(num1)*int(num2[-i]))
        for j in range(0,len(l)):
            sum = sum + l[j] * 10 ** j
        return str(sum)


r = Solution().multiply('123','456')
print r