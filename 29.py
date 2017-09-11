# 不用乘除法和取余，可以用循环减除数的方法，但是效率低下，可以将除数翻倍（利用移位），计数也翻倍的方法，指数大大增加效率。
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        count = 0
        flag = True
        if abs(divisor) == 2:
            return dividend >> 1
        if dividend < 0:
            dividend = -dividend
            flag = -flag
        if divisor < 0:
            divisor = - divisor
            flag = -flag
        if abs(dividend)>2**31-2 and abs(divisor)==1:
            if flag==1:
                return 2**31-1
            else:
                return -2**31
        while dividend-divisor>=0:
            temp,i = divisor,1
            while dividend >= temp:
                dividend = dividend - temp
                count += i
                temp <<= 1
                i <<= 1
        if flag == -1:
            return -count
        return count

r = Solution().divide(1,1)
print(r)