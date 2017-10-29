# 计算素数采用埃氏筛出法，把素数的倍数都挑选出来标记，要注意为了节省时间，范围通常是n的平方根，举个例子，24的素数筛出只需要计算到4而不是5，因为除非5*5才能超出24。。表述不清楚，自己再理解。
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        array = [True] * n
        array[0],array[1] = False,False
        for i in range(2,int(n**0.5)+1):
            if array[i]:
                j = i ** 2
                while j < n:
                    array[j] = False
                    j += i
        return array.count(True)
print Solution().countPrimes(10)