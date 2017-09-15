# 我要计算一个数组中任何数字能组合成target的序列（可以重复），用递归的思维，每次从数组中挑一个数，满足则接着进行，不满足则return。好好理解递归。
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        candidates = sorted(candidates)
        self.func(candidates,target,0,[],ret)
        return ret
    def func(self,l,target,index,path,ret):
        if target < 0 :
            return
        if target == 0:
            ret.append(path)
            return
        for i in range(index,len(l)):
            self.func(l,target-l[i],i,path+[l[i]],ret)


l = [2, 3, 6, 7]
r = Solution().combinationSum(l,7)
print r