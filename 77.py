# 采用递归的思想，路径是自上而下传递，结果是在最底下保存，leetcode有问题，java这么做就不报错（time limited）
class Solution(object):
    def combine(self, n, k):
        r = []
        self.func(n,1,k,[],r)
        return r
    def func(self,n,left,count,path,ret):
        if count == 0:
            ret.append(path)
            return
        for i in range(left,n+1):
            self.func(n,i+1,count-1,path+[i],ret)