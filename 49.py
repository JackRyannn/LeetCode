# 用dict来简化，非常好用，不然这题出现time limit exceeded
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = dict()
        for s in strs:
            ls = tuple(sorted(s))
            if not ls in d:
                d[ls] = []
            d[ls].append(s)
        r = []
        for i in d.values():
            r.append(i)
        return r



print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))