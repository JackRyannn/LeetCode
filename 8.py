class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        j = 0
        while j < len(str):
            if str[j] != ' ':
                break
            j += 1
        s = str.replace(' ','',j)
        sign = True
        if s.startswith('+') or s.startswith('-'):
            if s.startswith('-'):
                sign = False
            i += 1
            if i >= len(s) or s[i] < '0' or s[i] > '9':
                return 0
        flag = True
        flag2 = True
        flag3 = True
        start = 0
        end = len(s)
        while i < len(s):
            if flag and (s[i] < '0' or s[i] > '9'):
                return 0
            if flag and s[i] == '0':
                i += 1
                continue
            flag = False
            if flag2:
                start = i
                flag2 = False
            if flag3 and (s[i] < '0' or s[i] > '9'):
                end = i
                flag3 = False
            i += 1
        ret = s[start:end]
        if start == end:
            return 0
        if sign:
            ret = int(ret)
        else:
            ret = -int(ret)
        if ret > 2147483647:
            ret = 2147483647
        if ret < -2147483648:
            ret = -2147483648
        return ret
print(Solution().myAtoi(''))