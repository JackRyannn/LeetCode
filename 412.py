# 非常像之前酒桌上玩的游戏，遇到倍数说别的词来代替
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []
        for i in range(1,n+1):
            item = ''
            if i % 3 != 0 and i % 5 != 0:
                item += str(i)
            else:
                if i % 3 == 0:
                    item += 'Fizz'
                if i % 5 == 0:
                    item += 'Buzz'
            l.append(item)
        return l


print Solution().fizzBuzz(20)