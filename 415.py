# 不难
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            c = num1
            num1 = num2
            num2 = c
        s = ''
        ret = ''
        for i in range(len(num1)-len(num2)):
            s += '0'
        num2 = s + num2
        flag = 0
        for i in range(1,len(num1)+1):
            m = int(num1[-i])+int(num2[-i])+flag
            if m >= 10:
                m = m%10
                flag = 1
            else:
                flag = 0
            ret += str(m)
        if flag:
            ret += '1'
        ret = ret[::-1]
        return ret

r = Solution().addStrings('408','5')
print r