# 运行时间很短
# 要求任意两个插板加x轴形成的容器装水量最少，关键是任意两个，最简单的方法是两次嵌套循环直接无脑计算，实际上由于求最小值的特殊性可以用复杂度为o（n）的算法。
# 把两个插板中较小的向中间移动，一次遍历即可

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m,n = 0,len(height)-1
        p = height[0]
        q = height[-1]
        r = min(p,q) * (n-m)
        while n>m:
            if p<q:
                m += 1
                while p>height[m]:
                    m += 1
                p = height[m]
            else:
                n -= 1
                while q>height[n]:
                    n -= 1
                q = height[n]
            t = min(height[m],height[n]) * (n-m)
            if t>r:
                r = t
        return r


print(Solution().maxArea([2,3,4]))