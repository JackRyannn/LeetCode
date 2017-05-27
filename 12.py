# 罗马数字像五进制，特殊的地方在于 比如 4 的表示是 5-1 （IV）
# 因此转换成整数的时候IV里的I是-1，下面第二个循环就是解决这个问题的
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        l = list(s)
        num = []
        for c in l:
            if c == 'I':
                t = 1
            elif c == 'V':
                t = 5
            elif c == 'X':
                t = 10
            elif c == 'L':
                t = 50
            elif c == 'C':
                t = 100
            elif c == 'D':
                t = 500
            elif c == 'M':
                t = 1000
            num.append(t)
        for i in range(len(num)):
            for j in range(i,len(num)):
                if num[i]<num[j]:
                    num[i] = -num[i]
                    break
        for s in num:
            r += s
        return r

print(Solution().romanToInt("MMMCDLXXXV"))