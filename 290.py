#模式匹配，我用了组合加去重复，还利用了深度拷贝deepcopy（）
import copy
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split(' ')
        if len(pattern) != len(str):
            return False
        strs = copy.deepcopy(str)
        for i in range(len(strs)):
            strs[i] += pattern[i]
        print(set(str))
        return len(set(pattern)) == len(set(str)) == len(set(strs))