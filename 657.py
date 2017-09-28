# 设置横轴纵轴两个坐标，根据不同指令计算当前坐标，若坐标返回到（0，0）则可以返回
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x,y = 0,0
        for i in moves:
            if i == 'U':
                y += 1
            elif i == 'D':
                y -= 1
            elif i == 'L':
                x -= 1
            elif i == 'R':
                x += 1
        if x == 0 and y == 0:
            return True
        return False


print Solution().judgeCircle('UDDULRR')