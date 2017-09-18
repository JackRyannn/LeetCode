# 二进制加法 【：：-1】这种切片可以实现翻转，三个参数分别为起始，终点，步长。
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ret = ''
        flag = 0
        if len(a) < len(b):
            c = a
            a = b
            b = c
        if len(a) > len(b):
            s = ''
            for i in range(len(a)-len(b)):
                s += '0'
            b = s+b
        for i in range(1,len(a)+1):
            s = int(a[-i])+int(b[-i])+flag
            if s == 3 :
                ret += '1'
                flag = 1
            elif s == 2:
                ret += '0'
                flag = 1
            elif s == 1:
                ret += '1'
                flag = 0
            elif s == 0:
                ret += '0'
                flag = 0
        if flag:
            ret += '1'
        ret = ret[::-1]
        return ret


a = '10'
b = '10'
r = Solution().addBinary(a,b)
print r